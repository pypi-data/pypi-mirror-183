from PyQt5.Qt import QCursor
from PyQt5.QtWidgets import QMessageBox
from copy import copy


from simple_slice_viewer.controller_base import (ControllerBase, 
                                                 StyleControllerBase)
from simple_slice_viewer.preset_model import ColorScale, ColorMap, ColorMaps
from simple_slice_viewer.preset_view import (ImageFusionPresetDialog, 
                                             AvailableColorScaleDialog, 
                                             ColorScaleDialog)
from simple_slice_viewer.menus import ColorBarContextMenu, ItemMenu


def delete_warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setText("Warning")
    msg.setInformativeText(('Please confirm to delete preset, this action '
                            'cannot be undone!.'))
    msg.setWindowTitle("Warining")
    button = msg.exec()
    return button

class PresetDialogController(ControllerBase):
    def __init__(self, view=None,  presets=None, model=None, parent=None):
        self.presets = presets
        self.original_presets = copy(presets)
        super().__init__(view=view, model=model, parent=parent)
        
    def reject(self):
        self.presets.reset(self.original_presets)
        super().reject()
        
    def set_widgets(self):

        self.view.combo.setModel(self.presets)
        self.view.set_preset(self.presets[0])
        
    def delete(self):
        button = delete_warning()
        if button == QMessageBox.Ok:
            index = self.view.combo.currentIndex()
           
            self.presets.delete(index)
            self.view.accept()
    
    def new(self):
        new = self.presets.add()
        self.view.set_preset(new)
        self.view.new_button.setEnabled(False)
        self.view.combo.setEnabled(False)  
        
    def update(self, _=None):
        name = self.view.combo.currentText()
        preset =self.presets.get_item_by_name(name)
        self.view.set_preset(preset)
        enabled = name != self.presets[0].name
        self.view.setEnabled(enabled)
        
    def set_view_callbacks(self):
        self.view.new_button.clicked.connect(self.new)
        self.view.combo.currentIndexChanged.connect(self.update)
        self.view.delete_button.clicked.connect(self.delete)
        

class ImageFusionPresetController(PresetDialogController):
    ViewClass = ImageFusionPresetDialog
    
    def set_widgets(self):
        self.view.image_colorscale_combo.setModel(self.model.colorscales)
        self.view.image_colormap_combo.setModel(self.model.colormaps)
        
        self.view.fusion_colorscale_combo.setModel(self.model.colorscales)
        self.view.fusion_colormap_combo.setModel(self.model.colormaps)
        super().set_widgets()


class ColorScalePresetController(PresetDialogController):  
    ViewClass = ColorScaleDialog
    
    def update(self):
        super().update()
        
        used_colorscales = [p.image_colorscale\
                            for p in self.model.image_fusion_presets]
        used_colorscales += [p.fusion_colorscale\
                             for p in self.model.image_fusion_presets]
        
        
        enabled = self.view.combo.currentText() not in used_colorscales
        self.view.delete_button.setEnabled(enabled)
        
  
    def set_view_callbacks(self):    
        self.view.combo.currentTextChanged.connect(self.update)
        self.view.new_button.clicked.connect(self.new)
        self.view.delete_button.clicked.connect(self.delete)
        


        


class ColorScaleController(StyleControllerBase):
    PRESET_CLASS = ColorScale
    
    def model_update_image_callback(self):
        if self._preset is not None:
            self.set_preset(self._preset)
            
    def set_preset(self, preset):   
        if isinstance(preset, str):
            return self.set_preset_by_name(preset)
        
        super().set_preset(preset)
        
        preset = self.get_preset()
        
        if preset is None:
            preset = self.presets[0]
        elif isinstance(preset, self.PRESET_CLASS):
            pass
        else:
            raise TypeError(f'type {preset}')
    
        clim = preset.get_clim(clim_range=self.model.get_clim())
        
        self.view.setLevels(clim)

                                    
class ColorMapController(StyleControllerBase):
    def set_preset(self, preset):    
        if isinstance(preset, str):
            return self.set_preset_by_name(preset)
        
        super().set_preset(preset)
        
        preset = self.get_preset()
        
        if preset is None:
            preset = self.presets[0]
        elif isinstance(preset, ColorMap):
            pass
        else:
            raise TypeError(f'type {type(preset)}')
    
      
        self.view.setColorMap(preset.pg_colormap)
    
class AlphaController(StyleControllerBase):
    def set_preset(self, preset):
        super().set_preset(preset)
        self.set_alpha(preset)
        
    def set_view_callbacks(self):
        self.view.alpha_slider.scrollbar.valueChanged.connect(self.set_alpha)

    def set_alpha(self, alpha):

        self.view.alpha_slider.scrollbar.setValue(int(round(alpha, 2)))
        self.view.image_view.fusion_item.setOpacity(round(alpha/100, 2))
        
        
    def get_alpha(self):
        return self.view.image_view.fusion_item.opacity() * 100
    
    def get_preset(self):
        return self.get_alpha()
    


class StyleController(StyleControllerBase):
    _preset = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    def create_subcontrollers(self):
        self.alpha_controller = AlphaController(view=self.view)
        self.alpha_controller.set_alpha(self.get_preset().alpha)
                                                
        
        cbars = (self.view.image_view.colorbar_image, 
                 self.view.image_view.colorbar_fusion)
        
        self.colormap_controllers = []
        self.colorscale_controllers = []
        
        for model, cbar in zip(self.model, cbars):
            contr = ColorScaleController(view=cbar, model=model,
                                         presets=self.presets.colorscales)
            
            self.colorscale_controllers.append(contr)
            
            contr = ColorMapController(view=cbar, model=model,
                                       presets=self.presets.colormaps)
                                     
            self.colormap_controllers.append(contr)

    def set_preset_by_name(self, preset_name):
        presets =  self.presets.image_fusion_presets
        preset = presets.get_item_by_name(preset_name)
        if preset is None:
            return
        self.set_preset(preset)

    def get_preset(self):
        if self._preset is None:
            self._preset = self.presets.image_fusion_presets[0]
        return self._preset
    
    def set_preset(self, preset):
        if preset is None:
            return 
        
        super().set_preset(preset)
        
        cmaps = [preset.image_colormap, preset.fusion_colormap]
        cscales = [preset.image_colorscale, preset.fusion_colorscale]
        
        for contr, cmap in zip(self.colormap_controllers, cmaps):
            contr.set_preset(cmap)
        
        for contr, cscale in zip(self.colorscale_controllers, cscales):
            contr.set_preset(cscale)
        
    def refresh(self):
        self.set_visibility_fusion_colorbar()
        
    def model_update_image_callback(self):
        super().model_update_image_callback()    
        self.set_visibility_fusion_colorbar()
        # self.set_enabled_context_menus() # 2DO
    
    def set_visibility_fusion_colorbar(self):
        visible = self.model[1].get_image() is not None
        self.view.image_view.colorbar_fusion.setVisible(visible)
        self.view.image_view.fusion_item.setVisible(visible)
        self.view.alpha_slider.setVisible(visible)   
        alpha = 0
        if visible:
            alpha = self.get_preset().alpha
            

        self.alpha_controller.set_alpha(alpha)


class ColorBarMenuController(StyleControllerBase):
    
    def __init__(self, style_controller=None, *args, **kwargs):
        self.style_controller = style_controller
        super().__init__(*args, **kwargs)
    
    def set_view_callbacks(self):
        cback = lambda: self.show_color_menu(0)
        self.view.image_view.colorbar_image.right_clicked.connect(cback)
        cback = lambda: self.show_color_menu(1)
        self.view.image_view.colorbar_fusion.right_clicked.connect(cback)
        cback = self.show_preset_menu
        self.view.image_view.image_item.right_clicked.connect(cback)
    
    def show_preset_menu(self):
        item_names = self.presets.image_fusion_presets.get_names()
        menu = ItemMenu(item_names=item_names)
        menu.edit_action = menu.addAction('Edit Presets')
        menu.edit_action.triggered.connect(self.edit_presets)
        
        menu.action_triggered.connect(self.style_controller.set_preset_by_name)
        menu.exec_(QCursor().pos())
        
    def edit_presets(self):
        
        presets = self.presets.image_fusion_presets

        contr = ImageFusionPresetController(model=self.presets,
                                            presets=presets,
                                            parent=self.view)
        
        contr.view.set_preset(self.style_controller.get_preset())
        
        def finished(result):
            if contr.view.result() == contr.view.Accepted:
                print('accepted')
                
                preset = contr.view.get_preset()
                if preset.name not in presets.get_names():
                    preset = presets[0]
                else:
                    old_preset = presets.get_item_by_name(preset.name)
                    old_preset.update(**dict(preset))
                    
               
                self.style_controller.set_preset_by_name(preset.name)
                
        contr.view.finished.connect(finished)
        contr.view.exec_()
        
    def show_color_menu(self, index):   
        def select_color_maps():
            
            dlg = AvailableColorScaleDialog(parent=self.view)
            dlg.from_list(self.presets.colormaps)
            
            def dialog_finished():
                if dlg.result() == dlg.Accepted:        
                    self.presets.colormaps = dlg.to_list()
                    if len(self.presets.colormaps) == 0:
                        self.model.colormaps = ['gray']
                    
            dlg.finished.connect(dialog_finished)
            dlg.exec_()
            
        def select_color_scales():
            presets = self.presets.colorscales
            contr = ColorScalePresetController(model=self.presets,
                                               presets=presets,
                                               parent=self.view)
            
            preset = self.style_controller.get_preset()
            if index == 0:
                name = preset.image_colorscale
            else:
                name = preset.fusion_colorscale
            

            contr.view.set_preset(presets.get_item_by_name(name))
            
            def finished(result):
                if contr.view.result() == contr.view.Accepted:
                    print('accepted')
                    preset = contr.view.get_preset()
                    if preset.name not in presets.get_names():
                        preset = presets[0]
                    else:
                        old_preset = presets.get_item_by_name(preset.name)
                        old_preset.update(**dict(preset))
                        
                    scontrs =  self.style_controller.colorscale_controllers
                    scontrs[index].set_preset_by_name(preset.name)
                    
            contr.view.finished.connect(finished)
            contr.view.exec_()

        menu = ColorBarContextMenu(colorscales=self.presets.colorscales,
                                   label='image',
                                   colormaps=self.presets.colormaps)
        cback = lambda cmap, index=index: self.set_colormap(cmap, index)
        menu.cmap_menu.action_triggered.connect(cback)
        
        menu.edit_colormaps_clicked.connect(select_color_maps)
        
        cback = lambda cscale, index=index: self.set_colorscale(cscale, index)
        menu.cscale_menu.action_triggered.connect(cback)
        menu.edit_colorscales_clicked.connect(select_color_scales)
        
        menu.exec_(QCursor().pos())
        
    def set_colormap(self, cmap, index):
        colormaps = ColorMaps.get_available_colormaps()
        colormap = colormaps.get_item_by_value('colormap', cmap)
        self.style_controller.colormap_controllers[index].set_preset(colormap)
    
    def set_colorscale(self, colorscale_name, index):
        colorscales = self.presets.colorscales
        colorscale = colorscales.get_item_by_name(colorscale_name)
        contr = self.style_controller.colorscale_controllers[index]
        contr.set_preset(colorscale)
        
    def get_preset(self):
        if self._preset is None:
            self._preset = self.presets.image_fusion_presets[0]
        return self._preset

    def get_preset_by_name(self, preset_name):
        presets = self.presets.image_fusion_presets
        return presets.get_preset_by_name(preset_name)
    
    

    
    