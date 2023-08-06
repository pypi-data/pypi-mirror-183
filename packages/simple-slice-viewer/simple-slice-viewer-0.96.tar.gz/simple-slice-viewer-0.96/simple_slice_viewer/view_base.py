from PyQt5.QtWidgets import QDialog, QGridLayout, QWidget

class WidgetBase(QWidget):
    _layout = None
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.create_widgets()
        self.create_layout()
        self.create_bottom_layout()
        self.set_callbacks()
        self.setLayout(self.layout)
        self.set_widgets()
        
    def create_widgets(self):
        pass
    
    def create_layout(self):
        pass
    
    def create_bottom_layout(self):
        pass
    
    def set_callbacks(self):
        pass
    
    def set_widgets(self):
        pass

    @property
    def layout(self):
        if self._layout is None:
            self._layout = self._get_layout_object()
        return self._layout
    
    @layout.setter
    def layout(self, layout):
        self._layout = layout
        
    
    def _get_layout_object(self):
        return QGridLayout()
    
    @staticmethod
    def set_combo_to_text(combo, text):
        combo.setCurrentIndex(combo.findText(str(text)))


class QDialogBase(QDialog):
    _layout = None
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.create_widgets()
        self.create_layout()
        self.create_bottom_layout()
        self.set_callbacks()
        self.setLayout(self.layout)
        self.set_widgets()
        
    def create_widgets(self):
        pass
    
    def create_layout(self):
        pass
    
    def create_bottom_layout(self):
        pass
    
    def set_callbacks(self):
        pass
    
    def set_widgets(self):
        pass

    @property
    def layout(self):
        if self._layout is None:
            self._layout = self._get_layout_object()
        return self._layout
    
    @layout.setter
    def layout(self, layout):
        self._layout = layout
        
    
    def _get_layout_object(self):
        return QGridLayout()
    
    @staticmethod
    def set_combo_to_text(combo, text):
        combo.setCurrentIndex(combo.findText(str(text)))
