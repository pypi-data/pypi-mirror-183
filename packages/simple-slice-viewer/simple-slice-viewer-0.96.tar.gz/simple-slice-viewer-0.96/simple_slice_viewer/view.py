import SimpleITK as sitk
import sitk_tools
import pyqtgraph as pg
import numpy as np
from pyqtgraph import Point
from PyQt5.QtWidgets import (QLabel, QRadioButton, QApplication, QPushButton, 
                             QScrollBar, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QStatusBar, QSizePolicy)
                                                 
from pyqtgraph import InfiniteLine
from PyQt5.QtCore import Qt, pyqtSignal, QPointF
import qtawesome as qta

from simple_slice_viewer.view_base import WidgetBase
from simple_slice_viewer import model
from simple_slice_viewer.preset_model import ColorMap
from simple_slice_viewer import Logger

LOG_LEVEL = Logger.LEVEL_DEBUG





    
class ColorBarItemMouse(pg.ColorBarItem):    
    _saved_levels = None
    
    right_clicked = pyqtSignal()
    
    def __init__(self, *args, plot_item=None, **kwargs):
        self.plot_item = plot_item
        super().__init__(*args, **kwargs)
    
    # def __init__(self, *args, **kwargs):
    #     self.parent = kwargs.pop('parent')
    #     pg.ColorBarItem.__init__(self, *args, **kwargs)
    
    def set_alpha(self, alpha):    
        alpha = alpha/100
        self.plot_item.setOpacity(alpha)
    
 
    def SaveLevels(self):
        self._saved_levels = self.levels()
        
    def RestoreLevels(self):
        if self._saved_levels is not None:
            self.setLevels(self._saved_levels)
        
    def mouseClickEvent(self, event):
        if event.button() == 2:
            # show context menu
            self.right_clicked.emit()

    def setColorMap(self, cmap):
        cmap = ColorMap.get_pg_colormap(cmap)
        # if sum(cmap[0].getRgb()) == 4:
        #     self.parent.plot_item.getViewBox().setBackgroundColor('w')
        # else:
        #    self.parent.plot_item.getViewBox().setBackgroundColor('k')
           
        super().setColorMap(cmap)
        
class ViewBoxMouse(pg.ViewBox):
    key_pressed = pyqtSignal(int)
    right_clicked = pyqtSignal()
    left_clicked = pyqtSignal()
    mouseScroll = pyqtSignal(int)

    def keyPressEvent(self, ev):
        self.key_pressed.emit(ev.key())
     

    def wheelEvent(self, event, axis=None):     

        event.accept()
        delta = event.delta() // 120
        self.mouseScroll.emit(delta)

 #   def mouseClickEvent(self, ev):
        
    
    def mouseDragEvent(self, ev):
    
        if ev.button() == Qt.LeftButton:
            return
        else:
            super().mouseDragEvent(ev)
            
    # def mouseDragEvent(self, ev, axis=None):
    #     if ev.button() == Qt.LeftButton:
    #         print('drag')
    #     else:
    #         return super().mouseDragEvent(ev, axis=axis)

class ImageItemMouse(pg.ImageItem):
    left_clicked = pyqtSignal(object)
    right_clicked = pyqtSignal(object)
    mouseScroll = pyqtSignal(int)
    
    def mouseClickEvent(self, event, axis=None):

        if event.button() == Qt.RightButton:            
            self.right_clicked.emit(event.pos())
        elif event.button() == Qt.LeftButton:
            self.left_clicked.emit(event.pos())
    


class InfiniteLine(InfiniteLine):
    _drag_position = QPointF(0, 0)
    _hoverEvent = pyqtSignal(bool)
    
    # def mousePressEvent(self, ev):
    #     print('click')
    #     super().mousePressEvent(ev)
    
    def setMouseHover(self, hover): 
        if self.moving:
            hover = True
        emit =  self.mouseHovering != hover
            
        super().setMouseHover(hover)
        
        if emit:
            self._hoverEvent.emit(hover)
            
    def mouseDragEvent(self, ev):
        self._drag_position = self.getViewBox().mapSceneToView(ev.scenePos())        
        super().mouseDragEvent(ev)
        
   
                
class CrossHairView(WidgetBase):
    positionChanged = pyqtSignal(Point)
    visibleChanged = pyqtSignal(bool)
    # def __init__(self, *args, view_item=None, **kwargs):
    #     self.view_item = view_item
        
    def __init__(self, *args, plot_item=None, **kwargs):        
        super().__init__(*args, **kwargs)        
        plot_item.addItem(self.vertical_line)
        plot_item.addItem(self.horizontal_line)

        self.plot_item = plot_item
        self.set_viewbox_callbacks()
        
        
        
    def get_lines(self):
        return [self.horizontal_line, self.vertical_line]
    
    def set_viewbox_callbacks(self):
        self.vertical_line.getViewBox().key_pressed.connect(self.key_press)
    def set_callbacks(self):         
        for line in self.get_lines():
            line.sigDragged.connect(self.drag)                       
            line.sigPositionChangeFinished.connect(self.drag_finished)            
            line._hoverEvent.connect(self.update_hover)
            line.sigPositionChanged.connect(self.position_changed)
            
    def key_press(self, key):
        if key == Qt.Key_C:
            self.set_visible()
            
    def drag(self, line):        
        self.horizontal_line.moving = True
        self.vertical_line.moving = True
        pos = line._drag_position
        if line == self.horizontal_line:
            self.vertical_line.setValue(pos.x())
        elif line == self.vertical_line:
            self.horizontal_line.setValue(pos.y())
        self.position_changed()
        
    def drag_finished(self, line):
        self.drag(line)
        self.vertical_line.moving = False
        self.horizontal_line.moving = False
                
        
    def create_widgets(self):
        self.horizontal_line = InfiniteLine(angle=0, movable=True)
        self.vertical_line = InfiniteLine(angle=90, movable=True)

    def update_hover(self, hover):
        
        lines = [self.horizontal_line, self.vertical_line]

        for line in lines:
            line.setMouseHover(hover)
    
    def is_visible(self):
        return self.horizontal_line.isVisible()
        
    def set_visible(self, visible=None):
        if visible is None:
            visible = not self.is_visible()
        
        if visible == self.is_visible():
            return
            
        for line in self.get_lines():
            line.setVisible(visible)
        
        self.visibleChanged.emit(self.is_visible())
        
    def set_position(self, pos):
        self.vertical_line.setValue(pos[0])
        self.horizontal_line.setValue(pos[1])
    
    def get_position(self):
        return Point(self.vertical_line.value(), 
                       self.horizontal_line.value())
    
    def position_changed(self, obj=None):
        self.positionChanged.emit(self.get_position())
        

        
class ImageWidget(WidgetBase):    

    _image = None
    _fusion = None

    def __init__(self, parent=None, image=None):
        
        
        self._image = image
            
        WidgetBase.__init__(self, parent=parent)
        
        self.refresh()
            
    def get_position(self):                
        return self.crosshair.get_position()
    
    def set_position(self, pos_index):      
        self.crosshair.set_position(pos_index)
    
    def create_widgets(self):
        self.view_box = ViewBoxMouse()

        self.plot_item = pg.PlotItem(viewBox=self.view_box,
                                     mouse_enabled=False)
        self.plot_item.setMenuEnabled(False)
        
        vb = self.plot_item.getViewBox()
        vb.setBackgroundColor('k')
        
        
        self.image_item = ImageItemMouse(image=self.get_np_image(), 
                                         parent=self.plot_item)
                                            
        
        
        
        self.fusion_item = pg.ImageItem(image=self.get_np_fusion(), 
                                        parent=self.plot_item,
                                        mouse_enabled=False)
        
        self.fusion_item.setZValue(10)
        
        self.colorbar_image = ColorBarItemMouse(plot_item=self.image_item)
        self.colorbar_fusion = ColorBarItemMouse(plot_item=self.fusion_item)
        
        self.colorbar_image.setImageItem(self.image_item)
        self.colorbar_fusion.setImageItem(self.fusion_item)
        
        
        self.plot_item.hideAxis('bottom')
        self.plot_item.hideAxis('left')
        
        self.plot_item.addItem(self.image_item)
        self.plot_item.addItem(self.fusion_item)
        self.crosshair = CrossHairView(plot_item=self.plot_item)
        

    def create_layout(self):
     
        self.layout = QHBoxLayout()
        self.glayout = pg.GraphicsLayoutWidget()
        
        self.glayout.addItem(self.plot_item, row=0, col=0)
        self.glayout.addItem(self.colorbar_image, row=0, col=1)
        self.glayout.addItem(self.colorbar_fusion, row=0, col=2)
        
        
    
        self.layout.addWidget(self.glayout)
        
        self.setLayout(self.layout)
    
    def refresh(self):
        self.image_item.setImage(self.get_np_image())
        self.fusion_item.setImage(self.get_np_fusion())
        
        #self.set_clim_image(self.get_image_min_max())
        #self.set_clim_fusion(self.get_fusion_min_max())
        
        self.plot_item.setAspectLocked(True, ratio=self.get_ratio())
        
    def clear(self):
        self.set_image(self.get_empty_image())
        self.set_fusion(self.get_empty_fusion())
        self.refresh()
        
    def clear_fusion(self):
        image = self.get_image()
        fusion = self.get_empty_fusion()
    
        self.set_image_and_fusion(image, fusion)
        
        self.refresh()
        
    def get_ratio(self):
        spacing = self.get_image().GetSpacing()
        aspect = spacing[0] / spacing[1]
        return aspect
    
    def get_image_min_max(self):
        image = self.get_image()
        return [sitk_tools.min(image), sitk_tools.max(image)]
    
    def get_fusion_min_max(self):
        image = self.get_fusion()
        return [sitk_tools.min(image), sitk_tools.max(image)]
    
    def get_empty_image(self):
        return sitk.GetImageFromArray(np.zeros((10, 10)) )
    
    def get_empty_fusion(self):
        return sitk_tools.zeros_like_image(self.get_image())
   
    def get_image(self):
        if self._image is None:
            self._image = self.get_empty_image()
        return self._image
    
    def set_image_and_fusion(self, image=None, fusion=None):

        self.colorbar_image.SaveLevels()
        self.colorbar_fusion.SaveLevels()
        
        self._set_image(image)
        self._set_fusion(fusion)
        
        self.colorbar_image.RestoreLevels()
        self.colorbar_fusion.RestoreLevels()



        self.plot_item.setAspectLocked(True, ratio=self.get_ratio())
    
        
    def _set_image(self, image):
        self._image = image
        self.image_item.setImage(self.get_np_image())
        
        
    def get_fusion(self):
        if self._fusion is None:        
            self._fusion = sitk_tools.zeros_like_image(self.get_image())
        
        image = self.get_image()
        
        if image is not None:
            if not sitk_tools.same_space(image, self._fusion):
                self._fusion = sitk_tools.resample_to_image(self._fusion, image)
            
        return self._fusion
        
    def _set_fusion(self, fusion):
      
        self._fusion = fusion
        self.fusion_item.setImage(self.get_np_fusion())
        
        
    def get_np_image(self):
        return sitk.GetArrayFromImage(self.get_image()).T
    
    def get_np_fusion(self):
        return sitk.GetArrayFromImage(self.get_fusion()).T
    


        
class ButtonView(WidgetBase):
    button_clicked = pyqtSignal(str)
    button_texts = ['Button1', 'Button2']
    label_text = 'Button Group Name'
    orientation = Qt.Horizontal

    def __init__(self, parent=None, button_texts=None, **kwargs):
        
        if button_texts is not None:
            self.button_texts = button_texts
        
        if 'label_text' in kwargs.keys():
            self.label_text = kwargs['label_text']
            
        WidgetBase.__init__(self, parent=parent)

    def create_widgets(self):
        if self.label_text:
            self.label = QLabel(self.label_text, self)
        else:
            self.label = None
            
        self._buttons = []
        for text in self.button_texts:
            button = self.create_button(text)
            self._buttons += [button]
            
    def create_button(self, text):
        button = QPushButton(text, self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        return button
    
    def create_vertical_layout(self):
        row = 0
        if self.label is not None:
            self.layout.addWidget(self.label, row, 0)
            row += 1
        
        for button in self._buttons:
            self.layout.addWidget(button, row, 0)
            row += 1
            
    def create_horizontal_layout(self):
        column = 0
        if self.label is not None:
            self.layout.addWidget(self.label, 0, column)#, alignment=Qt.AlignCenter)
            column += 1
        
        for button in self._buttons:
            self.layout.addWidget(button, 0, column)#, alignment=Qt.AlignCenter)
            column += 1
            
    def create_layout(self):
        if self.orientation == Qt.Horizontal:
            self.create_horizontal_layout()
        elif self.orientation == Qt.Vertical:
            self.create_vertical_layout()
        else:
            raise ValueError(f'Unknown orientation {self.orientation}')
        
    
    def set_callbacks(self):
        for i, button in enumerate(self._buttons):
            text = self.button_texts[i]
            callback = lambda _, text=text: self.button_clicked.emit(text)
            button.clicked.connect(callback)
            
    def disable(self, text=None):
        self._set_state(text=text, enabled=False)

    def enable(self, text=None):
        self._set_state(text=text, enabled=True)

    def _set_state(self, text=None, enabled=True):
        if text is None:
            for text in self.button_texts:
                self._set_state(text=text, enabled=enabled)
            return
        index = self.button_texts.index(text)
        self._buttons[index].setEnabled(enabled)

   
class RadioButtonView(ButtonView):
    label_text = 'Radiobutton Group Name'
    button_texts = ['RadioButton1', 'RadioButton2']
    
    def __init__(self, parent=None, button_texts=None, label_text=None,
                 selected_button=None):
        ButtonView.__init__(self, parent=parent, button_texts=button_texts, 
                            label_text=label_text)
        
        self.set_selected_button(selected_button)
        
    
    def get_selected_button(self):
        for text, button in zip(self.button_texts, self._buttons):
            if button.isChecked():
                return text

    def set_selected_button(self, button_name):
        if button_name is None:
            button_name = self.button_texts[0]
            
        self._selected_button = button_name
        
        for text, button in zip(self.button_texts, self._buttons):
            if text == button_name:
                button.setChecked(True)
            else:
                button.setChecked(False)
    
    def emit(self, event, button_name):
        super().emit(self.EVENT, button_name)
        
        # if event_name == self.EVENT:
        #     button_index = self.button_texts.index(event_data)
        #     button = self._buttons[button_index]
        #     if button.isChecked():
        #         super().emit(event_name, event_data=event_data)
        # else:
        #     super().emit(event_name, event_data=event_data)
            
    
    def create_button(self, text):
        button = QRadioButton(text, self)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        return button
        
    
    def set_callbacks(self):
        for text, button in zip(self.button_texts, self._buttons):
            callback = lambda _, text=text: self.button_clicked.emit(text)        
            button.toggled.connect(callback)
            


class ViewDirectionRadioButtons(RadioButtonView):
    button_texts = model.ORIENTATIONS 
    orientation = Qt.Horizontal
    label_text = None

    


    
class OperatorButtons(ButtonView):
    SUBTRACT     = 'Subtract'
    ADD          = 'Add'
    SAVE         = 'Save'
    
    button_texts = (ADD, SUBTRACT, SAVE)
    label_text = 'Image <operator> Fusion'
    
    

    
  
class HorizontalSLider(WidgetBase):
    ORIENTATION = Qt.Horizontal
    def __init__(self, parent=None, label='Alpha', unit='%', value=50):
        self.label = label
        self.unit = unit
        
        super().__init__(parent=parent)
        
        self.setValue(value)
    
    def value(self):
        return self.scrollbar.value()
    
   
    def setValue(self, value):
        value = str(value)
        self.scrollbar.setValue(int(value))
        self.update_label()


        
    def create_widgets(self):
        self.label = QLabel(self.label)
        self.top_label = QLabel(str(self.value))
        self.scrollbar = QScrollBar(orientation = self.ORIENTATION)
        
        
    def create_layout(self):
        if self.ORIENTATION == Qt.Vertical:
            self.layout = QVBoxLayout()
            alignment = Qt.AlignHCenter
        elif self.ORIENTATION == Qt.Horizontal:
            self.layout = QHBoxLayout()
            alignment=Qt.AlignVCenter
            
        self.layout.addWidget(self.label, 0, alignment=alignment)
        self.layout.addWidget(self.top_label, 0, alignment=alignment)
        self.layout.addWidget(self.scrollbar, 1,  alignment=alignment)
        
    def set_callbacks(self):
        self.scrollbar.valueChanged.connect(self.update_label)
        
    def update_label(self, event_data=None):
        self.top_label.setText(str(self.value()) + self.unit)
        

class VerticalSLider(HorizontalSLider):
    ORIENTATION = Qt.Vertical
    
    
        
class SliceViewerWidget(WidgetBase):
    _menu = None
    def __init__(self, *args, **kwargs):        
        WidgetBase.__init__(self, *args, **kwargs)
        
        
    def get_orientation(self):
        return self.orientation_buttons.get_selected_button()
    
    def create_widgets(self):
        
        self.image_view = ImageWidget()
        
        self.slicescroller = VerticalSLider(parent=self, label='Slice', unit='')
        
        self.framescroller = VerticalSLider(parent=self, label='Frame', unit='')
        
        self.orientation_buttons = ViewDirectionRadioButtons(parent=self)
        
        self.alpha_slider = VerticalSLider(parent=self, label='Alpha',
                                           unit='%')
       
    
        self.status_label = QLabel('Start')
        

            
    def create_layout(self):
       
       row = 0   
       
       self.layout.addWidget(self.orientation_buttons, row, 0, 1, 3)
       
       row += 1
      
       self.layout.addWidget(self.slicescroller, row, 0)
       self.layout.addWidget(self.framescroller, row, 1)
       self.layout.addWidget(self.image_view, row, 2)
       self.layout.addWidget(self.alpha_slider, row, 3) 
       
       row += 1
    
       
       self.layout.addWidget(self.status_label, row, 0, 1, 4)
       

        # self.alpha_slider.scrollbar.valueChanged.connect(self.alpha_changed)
        
    
    
    
    
        
    def set_enabled_image(self, enabled):
        self.orientation_buttons.setVisible(enabled)
        self.slicescroller.setVisible(enabled)
        self.menus.set_enabled_image(enabled)
        #self.fusion_menu.colormap_menu.setEnabled(enabled)
        
        #self.fusion_menu.colorscale_menu.setEnabled(enabled)

       
    def set_enabled_fusion(self, enabled):
        raise
        self.image_view.colorbar_fusion.setVisible(enabled)
        self.image_view.fusion_item.setVisible(enabled)
        self.alpha_slider.setVisible(enabled)
        self.menus.set_enabled_fusion(enabled)
        

    def show_image(self, scroll=True):
        self.set_enabled_image(True)
        
        if scroll:
            self.slicescroller.setVisible(True)
            self.orientation_buttons.setVisible(True)
        else:
            self.scrollbar.setVisible(False)
            self.orientation_buttons.setVisible(False)
    
    def clear_image(self):
        self.image_view.clear()
        self.set_enabled_image(False)
        self.set_enabled_fusion(False)
        self.scrollbar.setVisible(False)
        self.orientation_buttons.setVisible(False)
    
     
    def show_fusion(self):
        self.set_enabled_fusion(True)
        
    def hide_fusion(self):
        self.set_enabled_fusion(False)
   
    def clear_fusion(self):
        self.image_view.clear_fusion()
        self.set_enabled_fusion(False)


class MainView(QMainWindow):    
   
    
    def __init__(self):
        QMainWindow.__init__(self)
     
        
        self.create_widgets()
        
        
        
        self.setWindowTitle('Simple Slice Viewer')
        icon = qta.icon('fa5s.pizza-slice', color='#ff4000')
        self.setWindowIcon(icon)
    

    # def set_enabled_image(self, enabled):
    #     self.image_view.set_enabled_image(enabled)
    #     self.image_view.menus.fusion_menu_bar.setEnabled(enabled)
        
        
    # def set_enabled_fusion(self, enabled):
    #     self.image_view.set_enabled_fusion(enabled)
    #     s#elf.fusion_menu_actions[self.CLEAR_FUSION].setEnabled(enabled)
        
    # def clear_fusion(self):
    #     self.image_view.clear_fusion()
    #     self.set_enabled_fusion(False)

        
    def create_widgets(self):
        self.image_view = SliceViewerWidget(parent=self)
        self.setCentralWidget(self.image_view)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.menu_bar = self.menuBar()
        #self.statusBar.addWidget(self.status_label)
  
  

        
             
if __name__ == "__main__":
    #import qdarkstyle

    app = QApplication([])
    
    color = app.palette().color(app.palette().Background)
    pg.setConfigOption('background', color)
    pg.setConfigOption('foreground', 'k')
    #app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # widget = pg.GraphicsLayoutWidget()
    # widget.addItem(ImageItem())
    # window = widget
    #window = WindowLevelWidget()
    window = MainView()
    #window.set_enabled_image(False)
    #window.set_enabled_fusion(False)
    #window.set_enabled_fusion(True)
    #window.show_image()
    
    
    #window.connect(window, window.SLICE_SCROLL_EVENT, callback)
   
    
    
    window.show()    
    app.exec_()
    
    
 