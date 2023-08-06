from PyQt5.QtWidgets import  (QLabel, QComboBox, QLineEdit, QDoubleSpinBox, 
                             QRadioButton, QPushButton, QCheckBox, QGridLayout)
                               
from PyQt5.QtCore import  pyqtSignal

from simple_slice_viewer.preset_model import (ImageFusionPreset, ColorScale, 
                                              ColorMap, ColorMaps)
from simple_slice_viewer.view_base import WidgetBase, QDialogBase
from simple_slice_viewer.view import HorizontalSLider


PERCENTAGE_MAX_OPTIONS = ['0%', '1%', '5%', '10%', '30%', '50%', 
                          '70%', '90%', '95%', '99%', '100%']


class AvailableColorScaleDialog(QDialogBase):
    nrows = 15
    def create_widgets(self):
        cmaps = ColorMaps.get_available_colormaps()
        self.checkboxes = {}
        for cmap in cmaps:            
            self.checkboxes[cmap.colormap] = QCheckBox(cmap.colormap)
            
        self.apply_button = QPushButton('Apply')
        self.cancel_button = QPushButton('Cancel')
        self.setWindowTitle('Available Colormaps')
    
    def from_list(self, cmaps):
        for box in self.checkboxes.values():
            box.setChecked(False)
            
        for cmap in cmaps:
            # if cmap not in self.checkboxes.keys():
            #     raise KeyError(f'{cmap} not a valid colormap!')   
            self.checkboxes[cmap.colormap].setChecked(True)
            
    def to_list(self):
        cmaps = []
        for cmap, box in self.checkboxes.items():
            if box.isChecked():
                cmaps += [cmap]
        return ColorMaps.from_list([ColorMap(colormap=cmap, name=cmap)\
                                    for cmap in cmaps])
                                    
    
    def set_callbacks(self):
        self.apply_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
    
    def create_layout(self):
        col = 0
        row = 0
        for cbox in self.checkboxes.values():
            self.layout.addWidget(cbox, row, col)
            row += 1
            if row == self.nrows:
                col += 1
                row = 0
                
        row = self.layout.rowCount()
        
        self.layout.addWidget(self.apply_button, row, 0)
        self.layout.addWidget(self.cancel_button, row, 1)
      
class PresetSaveDialog(QDialogBase):
    def create_widgets(self):
        self.existing_radio = QRadioButton('Overwrite Existing Preset')
        self.existing_combo = QComboBox()
        
        self.new_radio = QRadioButton('Create New Preset')
        self.new_label = QLabel('Preset Name: ')
        self.new_input = QLineEdit()
        
        self.apply_button = QPushButton('Save')
        # self.cancel_button = QPushButton('Cancel')
        
    def set_widgets(self):
        self.new_radio.setChecked(True)
        
    def set_callbacks(self):
        # self.apply_button.clicked.connect(self.accept)
        # self.cancel_button.clicked.connect(self.reject)
        
        self.existing_radio.toggled.connect(self.toggle)
        self.new_radio.toggled.connect(self.toggle)
        
    def toggle(self):
        new_checked = self.new_radio.isChecked()
        existing_checked = self.existing_radio.isChecked()
        
        self.new_label.setEnabled(new_checked)
        self.new_input.setEnabled(new_checked)
        
        self.existing_combo.setEnabled(existing_checked)
        
    def get_preset_name(self):
        if self.new_radio.isChecked():
            return self.new_input.text()
        elif self.existing_radio.isChecked():
            return self.existing_combo.currentText()
        
    def set_existing_presets(self, presets):
        self.existing_combo.addItems(presets)
        self.existing_combo.setCurrentIndex(0)

    def create_layout(self):
        row = 0
        self.layout.addWidget(self.existing_radio, row, 0)

        row += 1
        
        self.layout.addWidget(self.existing_combo, row, 0)
        
        row += 1
        
        self.layout.addWidget(self.new_radio, row, 0)
                              
        row += 1
        
        self.layout.addWidget(self.new_label, row, 0)
        
        row += 1
        
        self.layout.addWidget(self.new_input, row, 0)
        
        row += 1
       
        self.layout.addWidget(self.apply_button, row, 0)
    
        # row += 1
        
        # self.layout.addWidget(self.cancel_button, row, 0)


                
        
class RadioButtonGroup(WidgetBase):
    toggled = pyqtSignal(str)
    def __init__(self, *args, ncols=None):
        self.ncols = ncols
        self.title = args[0]
        self.button_names = args[1:]
        super().__init__()

    def create_widgets(self):
        self.radio_buttons = []
        self.title_label = QLabel(self.title)
        for name in self.button_names:
      
            self.radio_buttons += [QRadioButton(name)]
            
    def set_callbacks(self):
        for button in self.radio_buttons:
            button.toggled.connect(self.toggle)
            
    def toggle(self):
        self.toggled.emit(self.str_value())
        
    def create_layout(self):
        self.layout.addWidget(self.title_label, 0, 0)
        if self.ncols is None:
            self.ncols = 1
            
        col = 0
        for index, button in enumerate(self.radio_buttons):
            
            row = int(index/self.ncols)        
   
            self.layout.addWidget(button, row + 1, col)
            col += 1
            if col == self.ncols:
                col = 0
            
    def setValue(self, value):
        if not isinstance(value, str):
            value = int(value)
            value = str(value)
        if value[-1] != '%':
            value += '%'
        if value not in self.button_names:
            msg = f'{value} not in {self.button_names}!'
            raise ValueError(msg)
        for name, radio in zip(self.button_names, self.radio_buttons):
            if name == value:
                radio.setChecked(True)
                
    def str_value(self):
        for index, radio in enumerate(self.radio_buttons):
            if radio.isChecked():
                return self.button_names[index]
    
    def value(self):        
        value = float(self.str_value().replace('%', ''))
        return value
            
            
class MinMaxRangeWidget(WidgetBase):
    VALUES = PERCENTAGE_MAX_OPTIONS
    
    def create_widgets(self):
        self.min_radios = RadioButtonGroup('Minimum', *self.VALUES, ncols=3)
        self.max_radios = RadioButtonGroup('Maximum', *self.VALUES, ncols=3)
        
    def create_layout(self):
        row = 0
        
        self.layout.addWidget(self.min_radios, row, 0)
        self.layout.addWidget(self.max_radios, row, 1)
    
    def min_set(self, value):
        index = self.min_radios.button_names.index(value)
        for i, button in enumerate(self.max_radios.radio_buttons):
            button.setEnabled(i > index)
    
    def set_widgets(self):
        self.min_radios.radio_buttons[-1].setEnabled(False)
        self.max_radios.radio_buttons[0].setEnabled(False)
    def max_set(self, value):
        index = self.max_radios.button_names.index(value)
        for i, button in enumerate(self.min_radios.radio_buttons):
            button.setEnabled(i < index)

    def set_callbacks(self):
        
        self.min_radios.toggled.connect(self.min_set)
        self.max_radios.toggled.connect(self.max_set)
        
    def setValues(self, values):
        self.min_radios.setValue(values[0])
        self.max_radios.setValue(values[1])
        
    def values(self):
        return [self.min_radios.value(), self.max_radios.value()]

        
        
class FixedScaleWidget(WidgetBase):
    def __init__(self, *labels):
        self.labels = labels
        super().__init__()
        
    def create_widgets(self):
        self.qlabels = {}
        self.qvalues = {}
        for label in self.labels:
            self.qlabels[label] = QLabel(label)
            self.qvalues[label] = QDoubleSpinBox()
            
    def create_layout(self):
        for row, (qlabel, qvalue) in enumerate(zip(self.qlabels.values(), 
                                                   self.qvalues.values())):
            self.layout.addWidget(qlabel, row, 0)
            self.layout.addWidget(qvalue, row, 1)
    
    def setMinimum(self, value):
        for qvalue in self.qvalues.values():
            qvalue.setMinimum(value)
    
    def setMaximum(self, value):
        for qvalue in self.qvalues.values():
            qvalue.setMaximum(value)
    
    def setRange(self, minval, maxval):
        for qvalue in self.qvalues.values():
            qvalue.setRange(minval, maxval)
            
    def setValues(self, values):
        for value, qvalue in zip(values, self.qvalues.values()):
            qvalue.setValue(value)

    def values(self):
        return [qvalue.value() for qvalue in self.qvalues.values()]
    
        
class ImageFusionPresetDialog(QDialogBase):

    def create_widgets(self):
        self.combo = QComboBox()
        self.preset_label = QLabel('Preset')
        
        self.name_label = QLabel('Name')
        self.preset_name = QLineEdit('Preset')
        
        self.image_colorscale_label = QLabel('Image Colorscale')
        self.image_colorscale_combo = QComboBox()
        
        self.image_colormap_label = QLabel('Image Colormap')
        self.image_colormap_combo = QComboBox()
        
        self.fusion_colorscale_label = QLabel('Fusion Colorscale')
        self.fusion_colorscale_combo = QComboBox()
        
        self.fusion_colormap_label = QLabel('Fusion Colormap')
        self.fusion_colormap_combo = QComboBox()
        
        self.alpha_slider = HorizontalSLider()
        

        self.apply_button = QPushButton('Apply')
        self.cancel_button = QPushButton('Cancel')
        self.new_button = QPushButton('New Preset')
        self.delete_button = QPushButton('Delete Preset')
        
        self.widgets_enabled = [self.name_label,
                                self.preset_name,
                                self.image_colormap_label,
                                self.image_colorscale_combo,
                                self.fusion_colormap_label,
                                self.fusion_colormap_combo,
                                self.alpha_slider,
                                self.apply_button,
                                self.delete_button]
        
    def setEnabled(self, enabled):
        for widget in self.widgets_enabled:
            widget.setEnabled(enabled)
        
    def create_layout(self):
        row = 0
        self.layout.addWidget(self.preset_label, row, 0)
        self.layout.addWidget(self.combo,row , 1)
        
        row += 1
        
        self.layout.addWidget(self.name_label, row, 0)
        self.layout.addWidget(self.preset_name, row, 1)
        
        row += 1
        self.layout.addWidget(self.image_colorscale_label, row, 0)
        self.layout.addWidget(self.image_colorscale_combo, row, 1)
        row += 1
        
        self.layout.addWidget(self.image_colormap_label, row, 0),
        self.layout.addWidget(self.image_colormap_combo, row, 1)
        
        row += 1
        
        self.layout.addWidget(self.fusion_colorscale_label, row, 0)
        self.layout.addWidget(self.fusion_colorscale_combo, row, 1)
        
        row += 1
        
        self.layout.addWidget(self.fusion_colormap_label, row, 0)
        self.layout.addWidget(self.fusion_colormap_combo, row, 1)
       
        
        row += 1
        
        self.layout.addWidget(self.alpha_slider, row, 0, 1, 2)
        
        row += 1
        
        self.button_layout = QGridLayout()
        

        
        self.button_layout.addWidget(self.new_button, 0, 0)
        self.button_layout.addWidget(self.delete_button, 0, 1)
        
        
        
        self.button_layout.addWidget(self.apply_button, 1, 0)
        self.button_layout.addWidget(self.cancel_button, 1, 1)
        
        self.layout.addLayout(self.button_layout, row, 0, 1, 2)
        
    def set_callbacks(self):
        
        self.apply_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
    def set_widgets(self):
        self.setWindowTitle('Image Fusion Presets')
        self.alpha_slider.scrollbar.setMinimum(0)
        self.alpha_slider.scrollbar.setMaximum(100)
    
    def get_preset(self):
       
        preset = ImageFusionPreset(
            name=self.preset_name.text(),
            image_colormap=self.image_colormap_combo.currentText(),
            image_colorscale=self.image_colorscale_combo.currentText(),
            fusion_colormap=self.fusion_colormap_combo.currentText(),
            fusion_colorscale=self.fusion_colorscale_combo.currentText(),
            alpha=self.alpha_slider.value())
 
                             
        return preset
    
    def set_preset(self, preset):
        self.combo.setCurrentText(preset.name)
        self.preset_name.setText(preset.name)
        self.image_colormap_combo.setCurrentText(preset.image_colormap)
        self.image_colorscale_combo.setCurrentText(preset.image_colorscale)
        
        self.fusion_colormap_combo.setCurrentText(preset.fusion_colormap)
        self.fusion_colorscale_combo.setCurrentText(preset.fusion_colorscale)
        
        self.alpha_slider.setValue(preset.alpha)
        
class ColorScaleDialog(QDialogBase):
    new_preset_event = pyqtSignal()
    delete_preset_event = pyqtSignal()
    
   
    def create_widgets(self):
        super().create_widgets()
        self.combo       = QComboBox()
        self.colorscale_combo_label = QLabel('Colorscale')
        
        self.preset_label   = QLabel('Colorscale Name')
        self.preset_name    = QLineEdit('Name')
        
        self.type_minmax    = QRadioButton('Relative to Maximum')
        self.type_wl        = QRadioButton('Window - Level')
        self.type_fixed     = QRadioButton('Fixed Value')
        
        
        self.widget_fixed   = FixedScaleWidget('Minimum', 'Maximum')
        self.widget_fixed.setRange(-float('inf'), float('inf'))
        
        self.widget_wl   = FixedScaleWidget('Window', 'Level')
        self.widget_wl.setRange(-float('inf'), float('inf'))
        
        self.widget_minmax =  MinMaxRangeWidget()
        self.new_button = QPushButton('New')
        self.delete_button = QPushButton('Delete')
        self.apply_button = QPushButton('Apply')
        self.cancel_button = QPushButton('Cancel')
        
        #self.colorscale_buttons = ColorscaleButtons()
      
        self.widgets_enabled = [self.preset_label,
                                self.preset_name,
                                self.type_minmax,
                                self.type_wl,
                                self.type_fixed,
                                self.widget_fixed,
                                self.widget_wl,
                                self.widget_minmax,
                                self.delete_button,
                                self.apply_button]
        self.setWindowTitle('Image Preset')
        
        
    def setEnabled(self, enabled):
        for widget in self.widgets_enabled:
            widget.setEnabled(enabled)
        
    def create_layout(self):

        super().create_layout()
       
        row = self.layout.rowCount() + 1
        
        self.layout.addWidget(self.colorscale_combo_label, row, 0)
        self.layout.addWidget(self.combo, row, 1)
            
        row += 1
        
        self.layout.addWidget(self.preset_label, row, 0)
        
        self.layout.addWidget(self.preset_name, row, 1)
        
        row += 1
               
        self.layout.addWidget(self.type_wl, row, 0, 1, 2)
                
        row += 1
        
        self.layout.addWidget(self.widget_wl, row, 0, 1, 2)
        
        row += 1
        
        self.layout.addWidget(self.type_fixed, row, 0, 1, 2)
        
        row += 1
        
        self.layout.addWidget(self.widget_fixed, row, 0, 1, 2)
        
        row += 1
        
        self.layout.addWidget(self.type_minmax, row, 0, 1, 2)
        
        row += 1
        
        self.layout.addWidget(self.widget_minmax, row, 0, 1, 2)
     
       
        row += 1
        self.button_box = QGridLayout()
        self.button_box.addWidget(self.new_button, 0, 0)
        self.button_box.addWidget(self.delete_button, 0, 1)
        self.button_box.addWidget(self.apply_button, 1, 0)
        self.button_box.addWidget(self.cancel_button, 1, 1)
        self.layout.addLayout(self.button_box, row, 0, 1, 2)
        
    def _get_scale_types(self):
        return [ColorScale.WINDOW_LEVEL, ColorScale.FIXED, 
                ColorScale.RELATIVE_MIN_MAX]
    
    def _get_radios(self):
        return [self.type_wl, self.type_fixed, self.type_minmax]
    
    def _get_widgets(self):
        return [self.widget_wl, self.widget_fixed, self.widget_minmax]

    def set_callbacks(self):        
        super().set_callbacks()        
        
        self.type_wl.toggled.connect(self.toggle)
        self.type_minmax.toggled.connect(self.toggle)
        self.type_fixed.toggled.connect(self.toggle)
        self.apply_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def toggle(self, *args, **kwargs):
        for radio, widget in zip(self._get_radios(), self._get_widgets()):
            enabled = radio.isChecked()         
            widget.setEnabled(enabled)
            
    def set_preset(self, colorscale):
        self.preset_name.setText(colorscale.name)
        self.set_scale_type(colorscale.scale_type)
        self.set_scale(colorscale.colorscale)
    
    def get_preset(self):
        colorscale = ColorScale(scale_type=self.get_scale_type(),
                                colorscale=self.get_scale(),
                                name=self.preset_name.text())

        return colorscale
  
    def get_scale(self):
        for radio, widget in zip(self._get_radios(), self._get_widgets()):
            if radio.isChecked():
                return widget.values()
            
    def set_scale(self, scale):
        for radio, widget in zip(self._get_radios(), self._get_widgets()):
            if radio.isChecked():
                return widget.setValues(scale)
            
    def get_scale_type(self):
        for stype, radio in zip(self._get_scale_types(), self._get_radios()):
            if radio.isChecked():
                return stype
    
    def set_scale_type(self, scale_type): 
        for stype, radio in zip(self._get_scale_types(), self._get_radios()):
            if stype == scale_type:
                radio.setChecked(True)

                

    