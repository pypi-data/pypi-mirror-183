import os
import yaml
import numpy as np
import inspect
from copy import copy
import pyqtgraph as pg
import matplotlib.pyplot as plt
from PyQt5.QtCore import QAbstractListModel, pyqtSignal, QObject, QModelIndex

try:
    CONFIG_FOLDER = os.path.split(__file__)[0]
except:
    CONFIG_FOLDER = os.getcwd()
from PyQt5.QtCore import Qt

CONFIG_FILE = os.path.join(CONFIG_FOLDER, 'presets.yml')
CONFIG = yaml.safe_load(open(CONFIG_FILE))


class QModelItem(QObject):
    _defaults = {}
    value_changed = pyqtSignal(list)

    def __init__(self, **kwargs):
        super().__init__()
        
        self.set_defaults()
        self.update(**kwargs)
    
    def __copy__(self):
        copy_dict = {}
        for key in self._defaults.keys():
            value = getattr(self, key)
            if isinstance(value, QModelItem):
                value = copy(value)
                
            copy_dict[key] = value
        return self.__class__(**copy_dict)
    
    def copy(self):
        return copy(self)
    
    def __str__(self):
        return(yaml.dump(dict(self)))
        
    def __iter__(self):
        for key in self._defaults.keys():
            value = getattr(self, key)
            if isinstance(value, QModelItem):
                value = dict(value)
            yield (key, value)
            
    def set_defaults(self):
        for key, value in self._defaults.items():
            if inspect.isfunction(value) or inspect.isclass(value):
                value = value()
            setattr(self, key, value)
            
    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    
 
    
    @classmethod
    def from_dict(cls, dct):
        return cls(**dct)
    
class ColorMap(QModelItem):
    COLOR_MAP    = 'colormap'
    NAME         = 'name'
    DEFAULT_NAME    = 'colormap'
    
    GREENS = 'greens'
    MAGENTAS = 'magentas'
    _greens = np.array([[0., 0., 0., 0.],
                          [0., 1., 0., 1.]])

    _magentas = np.array([[0., 0., 0., 0.],
                          [1., 0., 1., 1.]])
    
    _defaults = {NAME:          DEFAULT_NAME,
                 COLOR_MAP:     'gray'}
    
   
    
    @property
    def pg_colormap(self):
        return self.get_pg_colormap(self.colormap)    
    
    @classmethod
    def get_pg_colormap(cls, cmap):
        if isinstance(cmap, pg.ColorMap):
            return cmap
        if cmap == cls.GREENS:
            return cls._get_cmap(cls._greens)
        elif cmap == cls.MAGENTAS:
            return cls._get_cmap(cls._magentas)
        elif cmap is None:
            cmap = 'gray'
            
        return pg.colormap.getFromMatplotlib(cmap)    

    @staticmethod
    def _get_cmap(col_data):
        return pg.ColorMap(pos=col_data[:,-1], color=255*col_data[:,:3]+0.5)
    
class ColorScale(QModelItem):
    #Keys
    #PARENT_KEY      = 'colorscales'
    COLOR_SCALE     = 'colorscale'
    NAME            = 'name'
    SCALE_TYPE      = 'scale_type'
    
    # Scale Types
    WINDOW_LEVEL             = 'window_level'
    RELATIVE_MIN_MAX         = 'relative_max'
    FIXED                    = 'fixed'
        
    DEFAULT_NAME    = 'colorscale'

    _defaults = {SCALE_TYPE:    RELATIVE_MIN_MAX,
                 NAME:          DEFAULT_NAME,
                 COLOR_SCALE:   ['0%', '100%']}

    def has_valid_colorscale(self):
        if self.scale_type == self.FIXED:
            return self.colorscale[1] > self.colorscale[0]
        elif self.scale_type == self.WINDOW_LEVEL:
            return self.colorscale[0] > 0
        elif self.scale_type == self.RELATIVE_MIN_MAX:
           scale = self.get_fraction_max(self.colorscale)
           return scale[1] > scale[0] and scale[1] > 0 
       
    def get_fraction_max(self, scale):
        return [float(ii.replace('%', '')) if isinstance(ii, str) else ii\
                 for ii in scale]
            
    def get_clim(self, clim_range=None):
        scale = self.colorscale
        if self.scale_type == self.WINDOW_LEVEL:
            clim = [scale[1] - 0.5 * scale[0],
                    scale[1] + 0.5 * scale[0]]            
        elif self.scale_type == self.RELATIVE_MIN_MAX:
   
            scale = self.get_fraction_max(self.colorscale)
                     
            clim = [scale[0]/100 * clim_range[0],
                    scale[1]/100 * clim_range[1]]

        elif self.scale_type == self.FIXED:
            clim = [*scale]
    
        return clim    

 
class ImageFusionPreset(QModelItem):
    IMAGE_SCALE     = 'image_colorscale'
    FUSION_SCALE    = 'fusion_colorscale'
    IMAGE_COLORMAP  = 'image_colormap'
    ALPHA           = 'alpha'
    FUSION_COLORMAP = 'fusion_colormap'
    NAME = 'name'
    DEFAULT_NAME = 'preset'
    _defaults = {IMAGE_SCALE:       'Min-Max',
                 FUSION_SCALE:      'Min-Max',
                 IMAGE_COLORMAP:    'jet',
                 FUSION_COLORMAP:   'jet',
                 ALPHA:              1,
                 NAME:              'ImageFusionPreset'}


class QModelItemList(QAbstractListModel):
    PARENT_KEY = 'item_list'
    
    ITEM_CLASS = QModelItem
   
    DISPLAY_ROLE_KEY = 'name'
    
    NAME = 'name'
    
    
    presetChanged = pyqtSignal(str)
    nameChanged = pyqtSignal(str, str)
    
    _index = 0
    
    def __init__(self, *args, item_list=None, **kwargs):
        QAbstractListModel.__init__(self, *args, **kwargs)
        self.item_list = item_list or []
        
    def __str__(self):
        return(yaml.dump(self.to_list()))
        
    def __iter__(self):
        return self.item_list.__iter__()
    
    def __getitem__(self, indices):
        return self.item_list.__getitem__(indices)
    
    def __len__(self):
        return len(self.item_list)
    
    def __copy__(self):
        return self.__class__.from_list([copy(item)\
                                         for item in self.item_list])
    
    def update(self, model_list, *args, **kwargs):
        for item in model_list:
            copy_item = self.ITEM_CLASS.from_dict(dict(item), *args, **kwargs)
            self.item_list.append(copy_item)
        self.layoutChanged.emit()
    
    def get_names(self):
        return [item.name for item in self]
    
    def get_index(self):
        return self.index(0).column()
    
    def copy(self):
        return copy(self)
        
    def clear(self):
        self.beginResetModel()
        while len(self) > 0:
            self.delete(0)
        self.endResetModel()
    
    def get_new_name(self):
        name = self.ITEM_CLASS.DEFAULT_NAME 
        i = 0
        while name in [item.name for item in self]:
            i += 1
            name = self.ITEM_CLASS.DEFAULT_NAME  + str(i)
        return name
    
    def new_item(self):
        item = self.ITEM_CLASS(name=self.get_new_name())
        return item
    
    def data(self, index, role): 
        if index.isValid() and role==Qt.DisplayRole:            
            value =  getattr(self.item_list[index.row()], 
                             self.DISPLAY_ROLE_KEY)
            return value
        
    def setData(self, index, value, role=Qt.EditRole):
        if not isinstance(index, QModelIndex):
            index = self.createIndex(index, 0)
        if index.isValid():
            if role == Qt.EditRole and value is not None:    
                value = dict(value)
                if self.NAME in value.keys():
                    old_name = self.data(index, role=Qt.DisplayRole)
                self.item_list[index.row()].update(**value)
                self.dataChanged.emit(index, index, [Qt.EditRole])
                if self.NAME in value.keys():
                    self.nameChanged.emit(old_name, value[self.NAME])
                    
    def rowCount(self, index):
        return len(self.item_list)
    
    def add(self, index=None, item=None):
        if item is None:
            item = self.new_item()
       
        if index is None:
            self.item_list.append(item)
        else:
            self.item_list.insert(index, item)
       
        self.layoutChanged.emit()
        return item
    
    def delete(self, index):
        if isinstance(index, QModelItem):
            index = [i for i, item in enumerate(self.item_list)\
                     if item.name == index.name][0]
        

        del self.item_list[index]    

                
        self.layoutChanged.emit()
        

    def roleNames(self):
        return self.Roles
    
    @classmethod
    def from_list(cls, item_list):  
        obj_list = []
        for item in item_list:
            if isinstance(item, dict):
                item = cls.ITEM_CLASS.from_dict(item)
            elif isinstance(item, cls.ITEM_CLASS):
                pass
            else:
                raise TypeError(f'Cannot Load Type {type(item)}')
            obj_list.append(item)
                    
        return cls(item_list=obj_list)
    
    
    def to_list(self):
        return [dict(item) for item in self.item_list]
    
    def get_item_by_value(self, attr, value):
        items = [item for item in self.item_list\
                 if getattr(item, attr) == value]
        
        if len(items) == 0:
            return None
            #raise IndexError(f'No Item has value {value} for attr {attr}')
        
        return items[0]
    
    def get_item_by_name(self, name):
        return self.get_item_by_value('name', name)
    
    @classmethod
    def from_defaults(cls):
        return cls.from_list(CONFIG[cls.PARENT_KEY])
    

class ColorScales(QModelItemList):    
    ITEM_CLASS = ColorScale
    PARENT_KEY = 'colorscales'    
    # NAME = 'name'
    
class ColorMaps(QModelItemList):
    ITEM_CLASS = ColorMap
    PARENT_KEY = 'colormaps'
    # NAME = 'name'
 
    @classmethod
    def get_available_colormaps(cls):
        cmaps = plt.colormaps()
        cmaps += ['greens', 'magentas']        
        cmaps = sorted(list(set(cmaps)))
        
        
        
        return cls.from_list([ColorMap(colormap=cmap, name=cmap) \
                              for cmap in cmaps])


    

class ImageFusionPresets(QModelItemList):
    PARENT_KEY = 'image_fusion_presets'
    ITEM_CLASS  = ImageFusionPreset


 
            

class PresetModel:
    FOLDER = '.simple-slice-viewer'
    FILE = 'presets.yml'
    def __init__(self, colorscales=None, image_fusion_presets=None,
                  colormaps=None):
        
        if colormaps is None:
            colormaps = []
            
       
        if colorscales is None:
            colorscales = ColorScales()
                        
        if image_fusion_presets is None:
            image_fusion_presets = ImageFusionPresets()
        
        self.colormaps = colormaps
        
        self.colorscales = colorscales
        self.image_fusion_presets = image_fusion_presets
        self.set_callbacks()
    
    def __copy__(self):
        return PresetModel.from_dict(self.to_dict())
    
    
    def reset(self, presets=None):
        if presets is None:
            presets = self.load_from_disk(load_defaults=True)
        if isinstance(presets, PresetModel):
            presets = presets.to_dict()
        
        colormaps = presets[ColorMaps.PARENT_KEY]
        colorscales = presets[ColorScales.PARENT_KEY]
        image_fusion_presets = presets[ImageFusionPresets.PARENT_KEY]
        
        self.colormaps = ColorMaps.from_list(colormaps)
        self.colorscales = ColorScales.from_list(colorscales)
        self.image_fusion_presets = ImageFusionPresets.from_list(
            image_fusion_presets)
        self.set_callbacks()
       
    
    def set_callbacks(self):        
        self.colorscales.nameChanged.connect(self.scale_name_changed)
        
    
    def scale_name_changed(self, old_name, new_name):
        for item in self.image_fusion_presets:
            if item.image_scale == old_name:
                item.image_scale = new_name
        for item in self.image_fusion_presets:
            if item.fusion_scale == old_name:
                item.fusion_scale = new_name
  
                    
   
    def get_used_scales(self):
        used = [preset.image_scale for preset in self.image_fusion_presets]
        used += [preset.fusion_scale for preset in self.image_fusion_presets]        
        return sorted(list(set(used)))
    
    
    
    def clear(self):
        self.image_fusion_presets.clear()
        self.scales.clear()        
        self.colormaps.clear()
        
    def to_dict(self):
        dct = {}

        dct[ColorScales.PARENT_KEY] = self.colorscales.to_list()
        
        dct[ColorMaps.PARENT_KEY] = self.colormaps.to_list()
        
        key = ImageFusionPresets.PARENT_KEY                           
        dct[key] = self.image_fusion_presets.to_list()
       
        
       
        return dct

    @classmethod
    def from_dict(cls, dct):
        colormaps               = dct[ColorMaps.PARENT_KEY]
        colorscales             = dct[ColorScales.PARENT_KEY]       
        image_fusion_presets    = dct[ImageFusionPresets.PARENT_KEY]
        
        
        colormaps = ColorMaps.from_list(colormaps)
        colorscales = ColorScales.from_list(colorscales)                                             
        presets = ImageFusionPresets.from_list(image_fusion_presets)
                                               
        return cls(colorscales=colorscales,
                   image_fusion_presets=presets,
                   colormaps=colormaps)
    
    @classmethod
    def get_folder(cls):
        user_folder = os.path.expanduser('~')
        folder = os.path.join(user_folder, cls.FOLDER)
        return folder
    
    @classmethod
    def get_filename(cls):
        return os.path.join(cls.get_folder(), cls.FILE)
        
    def save_to_disk(self):
        os.makedirs(self.get_folder(), exist_ok=True)
        yaml.dump(self.to_dict(), open(self.get_filename(), 'w'))
    
    def restore_defaults(self):
        self.clear()
        file = CONFIG_FILE
        dct = yaml.safe_load(open(file))
        self.update(dict(self.from_dict(dct)))
        return self
    

    @classmethod
    def load_from_disk(cls, load_defaults=False):        
        file = cls.get_filename()
        if not load_defaults:
            try:
                dct = yaml.safe_load(open(file))
                print('Presets Loaded From Disk!')
            except:
                print('Loading Defaults')
                dct = yaml.safe_load(open(CONFIG_FILE))
        else:
            dct = yaml.safe_load(open(CONFIG_FILE))
            
        return cls.from_dict(dct)
  
    
    
    
    

    

