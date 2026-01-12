from PyQt6.QtWidgets import QWidget

ROWS = 20
COLS = 20
PIXEL_SIZE = 20

class Fire(QWidget):
    """ Class which represents fire """ 
    def __init__(self):
        super().__init__()
       
        # Configuration
        self.rows = ROWS
        self.cols = COLS
        self.pixel_size = PIXEL_SIZE

        self.fire_intensity = [0 for _ in range(self.cols)]

    def get_update(self):
       pass 
