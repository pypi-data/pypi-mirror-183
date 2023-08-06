from PyQt5.QtWidgets import QMenu, QWidget
from PyQt5.QtCore import pyqtSignal

class StyleMenu(QMenu):
    _actions = None
    action_triggered = pyqtSignal(list)
    def __init__(self, name, presets=None):
        super().__init__(name)
        self.set_presets(presets)
    
    def set_presets(self, presets):
        self._presets = presets
        self._presets.layoutChanged.connect(self.update_preset_menu)
        self.update_preset_menu()
    
    def get_presets(self):
        return self._presets
        
    def update_preset_menu(self):
        if self._actions is not None:     
            for action in self._actions:
                self.removeAction(action)            
        self._actions = []
        
        
        for preset in self.get_presets():
            action =self.addAction(preset.name)
            callback = lambda _, name=self.title(), preset_name=preset.name:\
                self.action_triggered.emit([name, preset_name])
            action.triggered.connect(callback)
            self._actions += [action]
            
        
class ItemMenu(QMenu):
    action_triggered = pyqtSignal(str)
    
    def __init__(self, *args, item_names=None, **kwargs):
        super().__init__(*args, **kwargs)
        
       
            
        self._actions = []
        
        for item_name in item_names:
            action = self.addAction(item_name)
            cbk = lambda _, item_name=item_name: \
                self.action_triggered.emit(item_name)
            action.triggered.connect(cbk)
            self._actions += [action]
            

class ColorBarContextMenu(QMenu):
    edit_colormaps_clicked = pyqtSignal()
    edit_colorscales_clicked = pyqtSignal()
    
    def __init__(self, *args, colormaps=None, colorscales=None, 
                 label='', **kwargs):
        self.colormaps = colormaps
        self.colorscales = colorscales
        
        super().__init__(*args, **kwargs)
        
        
        self.label = label
        
        cmaps = [cmap.colormap for cmap in self.colormaps]
        if cmaps is not None:
            self.cmap_menu = ItemMenu(f'Set {self.label} colormap', 
                                      item_names=cmaps)        
            action = self.cmap_menu.addAction('Edit Colormaps')
            self.select_cmap_action = action
            cbk = self.edit_colormaps_clicked
            self.select_cmap_action.triggered.connect(cbk)
            
        cscales = [cscale.name for cscale in self.colorscales]

        if cscales is not None:
            self.cscale_menu = ItemMenu(f'Set {self.label} colorscale', 
                                        item_names=cscales)    
            action = self.cscale_menu.addAction('Edit Colorscales')
            action.triggered.connect(self.edit_colorscales_clicked)
            self.select_cscale_action = action
            
     
        
        self.addMenu(self.cmap_menu)
        self.addMenu(self.cscale_menu)
        
    
        

class MenuBar(QWidget):
    IMAGE = 'Image'
    FUSION = 'Fusion'
    EXPORT = 'Export'
    
    OPEN_FILE = 'Open File'
    SAVE_FILE = 'Save File'
    LOAD_DICOM_FOLDER = 'Load Dicom Folder'
    LOAD_PET = 'Load PET From Dicom'
    REMOVE_FUSION = 'Remove Fusion'
    MAKE_MOVIE = 'Export Movie of Slices'
    MAKE_MOVIE_OF_FRAMES = 'Export Movie of Frames'
    PRESET_MENU = 'Presets'
    IMAGE_PRESETS = 'Image Presets'
    FUSION_PRESETS = 'Fusion Presets'
    EDIT_PRESETS = 'Edit Presets'
    COLORMAPS = 'Select Available Colormaps'
    SETTINGS = 'Settings'
    SHOW_CROSSHAIR = 'Show CrossHair'
    SAVE_PRESETS = 'Save Presets'
    RESET_PRESETS = 'Reset Presets to Defaults'
    
    IMAGE_MENU = [OPEN_FILE, 
                  SAVE_FILE,
                  LOAD_DICOM_FOLDER, 
                  LOAD_PET]
                 
    
    FUSION_MENU = [OPEN_FILE, 
                  SAVE_FILE,
                  LOAD_DICOM_FOLDER, 
                  LOAD_PET,
                  REMOVE_FUSION]
                
    
    SETTINGS_MENU = [COLORMAPS, SHOW_CROSSHAIR, SAVE_PRESETS, RESET_PRESETS]
    
    MOVIE_MENU = [MAKE_MOVIE, MAKE_MOVIE_OF_FRAMES]
    
    MENUS = {IMAGE: IMAGE_MENU,
             FUSION: FUSION_MENU,
             # PRESET_MENU: None,
             EXPORT: MOVIE_MENU,
             SETTINGS: SETTINGS_MENU}
    
    action_triggered = pyqtSignal(list)
    def __init__(self, menubar=None, presets=None):
        super().__init__()
        self.menubar = menubar
        self.presets = presets
        self.populate_menubar()
        self.set_menus()
        
    def set_image_enabled(self, enabled):        
        self._menus[self.FUSION].setEnabled(enabled)
       
        actions = [self.SAVE_FILE]
        for name in actions:
            action = self.get_action_by_name(self.IMAGE, name)
            action.setEnabled(enabled)
            
    def set_fusion_enabled(self, enabled):        
        if enabled:
            self._menus[self.FUSION].setEnabled(True)
        
        actions = [self.SAVE_FILE, self.REMOVE_FUSION]
        for name in actions:
            action = self.get_action_by_name(self.FUSION, name)
            action.setEnabled(enabled)
            
    def get_action_by_name(self, menu_name, name):
        actions = [action for action in self._actions[menu_name]\
                   if action.text()==name]
        if len(actions) == 0:
            return None
        else:
            return actions[0]

    def populate_menubar(self):
        self._menus = {}
        self._actions = {}

        for name, items in self.MENUS.items():
            self._actions[name] = []
             
            menu = QMenu(name)
    
            for item in items:
                callback = lambda _, name=name, aname=item:\
                    self.action_triggered.emit([name, aname])
                    
                action = menu.addAction(item)
                action.triggered.connect(callback)
                self._actions[name] += [action]
                    
            self.menubar.addMenu(menu)
            self._menus[name] = menu

    def set_menus(self):
        action = self.get_action_by_name(self.SETTINGS,
                                         self.SHOW_CROSSHAIR)
        action.setCheckable(True)
        action.setChecked(True)
