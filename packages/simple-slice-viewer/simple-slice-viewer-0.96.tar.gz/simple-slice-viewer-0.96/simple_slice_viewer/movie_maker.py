import os
import cv2
import imageio
import qimage2ndarray
from PyQt5.QtWidgets import (QLabel, QFileDialog, QSpinBox, QPushButton,
                             QCheckBox, QProgressBar)

from simple_slice_viewer.controller_base import ControllerBase
from simple_slice_viewer.view_base import QDialogBase

DEFAULT_FPS = 10

class MovieMakerView(QDialogBase):
    def create_widgets(self):
        self.setWindowTitle('Export Movie')
        self.start_label = QLabel('Start index: ')
        self.start_value = QSpinBox()
        self.end_label = QLabel('End index: ')
        self.end_value = QSpinBox()
        self.colorbar_check = QCheckBox('Show Colorbar')
        self.colorbarfusion_check = QCheckBox('Show Fusion Colorbar')
        self.file_label = QLabel('Select File...')
        self.file_button = QPushButton('Export Movie')
        self.fps_label = QLabel('Frames per second: ')
        self.fps_value = QSpinBox()
        self.fps_value.setMaximum(60)
        self.fps_value.setMinimum(1)
        self.fps_value.setValue(DEFAULT_FPS)
        self.progressbar = QProgressBar()
        
        
    def create_layout(self):
        row = 0
        
        self.layout.addWidget(self.start_label, row, 0)
        self.layout.addWidget(self.start_value, row, 1)
        
        row += 1
        
        self.layout.addWidget(self.end_label, row, 0)
        self.layout.addWidget(self.end_value, row, 1)
        
        row += 1
        self.layout.addWidget(self.colorbar_check, row , 0)
        self.layout.addWidget(self.colorbarfusion_check, row , 1)
        
        row += 1
        
        self.layout.addWidget(self.fps_label, row, 0)
        self.layout.addWidget(self.fps_value, row, 1)
        
        row += 1
        
        self.layout.addWidget(self.file_label, row, 0, 1, 2)
        
        
        row += 1
        
        self.layout.addWidget(self.file_button, row, 0, 1, 2)
        
        row += 1
        
        self.layout.addWidget(self.progressbar, row, 0, 1, 2)
        self.progressbar.setVisible(False)
        
         
class MovieMaker(ControllerBase):
    FRAMES = 'frames'
    SLICES = 'slices'
    filename = None
    def __init__(self, view=None, model=None, image_view=None,
                 movie_type='slices'):
        
        
        self.model = model
        self.image_view = image_view
        self.movie_type = movie_type
        if view is None:
            view = MovieMakerView(parent=self.image_view)
        self.view = view
        
        self.set_view()
    
    def get_show_image_colorbar(self):
        return self.view.colorbar_check.isChecked()
    
    def get_show_fusion_colorbar(self):
        return self.view.colorbarfusion_check.isChecked()
        
    def get_start(self):
        return self.view.start_value.value()
    
    def get_end(self):
        return self.view.end_value.value()
    
    def get_fps(self):
        return self.view.fps_value.value()
    
    def get_file_to_write(self):
       
        
        extension = "MP4 (*.mp4);; GIF (*.gif)"
        filename = QFileDialog.getSaveFileName(self.view, 'Select a file:', 
                                           'movie.mp4',
                                            filter=extension)
       
        filename = filename[0]
       
        if not filename:
            return

        self.view.file_label.setText(filename)

        if self.movie_type == self.SLICES:
            frame_setter = self.model.set_slice_index
            
        elif self.movie_type == self.FRAMES:
            frame_setter = self.model.set_frame_index
            
        extension = os.path.splitext(filename)[1]
        
        self.prepare()
        
        if extension == '.mp4':
            self.write_movie(filename, frame_setter=frame_setter)
            
        elif extension == '.gif':

            self.write_gif(filename, frame_setter=frame_setter)
        else:            
            raise IOError(f'Cannot write to a {extension} file!')
        
        self.finish()
        
        
        
            
        
    def set_view(self):
        
        if self.movie_type == self.SLICES:
            movie_frames = self.model.get_number_of_slices()            
        else:
            movie_frames = self.model.get_number_of_frames()
        
        self.view.end_value.setMaximum(movie_frames)
        self.view.end_value.setValue(movie_frames)
        
        
        enabled = self.image_view.colorbar_image.isVisible()
            
        self.view.colorbar_check.setEnabled(enabled)
        self.view.colorbar_check.setChecked(enabled)
        
        enabled = self.image_view.colorbar_fusion.isVisible()
        self.view.colorbarfusion_check.setEnabled(enabled)
        self.view.colorbarfusion_check.setChecked(enabled)

        self.view.file_button.clicked.connect(self.get_file_to_write)
      
    def write_gif(self, filename='movie.gif', frame_setter=None):
        
        frames = []
        for index in range(self.get_start(), self.get_end()):
            frame_setter(index)    
            frames.append(self.get_nparray())
            self.view.progressbar.setValue(index)
        
        
        imageio.mimsave(filename, frames, format='GIF', fps=self.get_fps())
        

    
    
        
       
                
    def write_movie(self, filename='movie.mp4', frame_setter=None):

        video_writer = self.get_video_writer(filename=filename, 
                                             fps=self.get_fps())

        for index in range(self.get_start(), self.get_end()):       
            self.view.progressbar.setValue(index)
            frame_setter(index)
            video_writer.write(cv2.cvtColor(self.get_nparray(), 
                                            cv2.COLOR_RGB2BGR))                                
            
        video_writer.release()
        
        
        
        
    def prepare(self):
        cbars = [self.image_view.colorbar_image,
                 self.image_view.colorbar_fusion]
        
        visible = [self.get_show_image_colorbar(), 
                   self.get_show_fusion_colorbar()]
        
        self.cbar_was_visible = [cbar.isVisible() for cbar in cbars]
        
        for cbar, vis in zip(cbars, visible):
            cbar.setVisible(vis)
        
        self.view.progressbar.setMinimum(self.get_start())
        self.view.progressbar.setMaximum(self.get_end())
    
        self.view.progressbar.setVisible(True)
            
    def finish(self):
        cbars = [self.image_view.colorbar_image,
                 self.image_view.colorbar_fusion]
        
        for cbar, vis in zip(cbars, self.cbar_was_visible):
            cbar.setVisible(vis)
        
        self.view.progressbar.setVisible(False)  
        
    
        
    def get_video_writer(self, filename='movie.mp4', fps=1):
        # FourCC is a 4-byte code used to specify the video codec.
        extension = os.path.splitext(filename)[1]
        if extension == '.mp4':            
            fourcc = cv2.VideoWriter_fourcc(*"mp4v") 
        else:
            raise IOError(f'Cannot write to {extension} file!')
            
        dummy_array = self.get_nparray()
        shape = dummy_array.shape[0:2]

        writer = cv2.VideoWriter(filename, fourcc, float(fps),
                                 (shape[1], shape[0]))
        return writer
        
    def get_qtimage(self):
        return self.image_view.glayout.grab().toImage()
    
    def get_nparray(self):
        return qimage2ndarray.rgb_view(self.get_qtimage())
    
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from simple_slice_viewer.model import SyncedImageSlicers
    app = QApplication([])

    view = MovieMaker(model=SyncedImageSlicers(), view=MovieMakerView())
    view.show()
    view.exec_()