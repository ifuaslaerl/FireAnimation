from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor

ROWS = 20
COLS = 20
PIXEL_SIZE = 20

FIRE_COLORS = [
    (7, 7, 7), (31, 7, 7), (47, 15, 7), (71, 15, 7), (87, 23, 7), (103, 31, 7),
    (119, 31, 7), (143, 39, 7), (159, 47, 7), (175, 63, 7), (191, 71, 7),
    (199, 71, 7), (223, 79, 7), (223, 87, 7), (223, 87, 7), (215, 95, 7),
    (215, 95, 7), (215, 103, 15), (207, 111, 15), (207, 119, 15), (207, 127, 15),
    (207, 135, 23), (199, 135, 23), (199, 143, 23), (199, 151, 31), (191, 159, 31),
    (191, 159, 31), (191, 167, 39), (191, 167, 39), (191, 175, 47), (183, 183, 47),
    (183, 183, 55), (207, 207, 111), (223, 223, 159), (239, 239, 199), (255, 255, 255)
]

class Fire(QWidget):
    """ Class which represents fire """ 
    def __init__(self):
        super().__init__()
       
        # Configuration
        self.rows = ROWS
        self.cols = COLS
        self.pixel_size = PIXEL_SIZE

        self.intensity = [0 for _ in range(self.cols)]
        self.grid = self.update()

    def update(self):
        """ Updates the grid using the fire intensity"""
        grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for c in range(self.cols):
            for r in range(self.rows):
                intensity = max(0, self.intensity[c] - (self.rows - r))
                print(intensity)
                color_tuple = FIRE_COLORS[intensity]
                grid[r][c] = QColor(*color_tuple)
                assert grid[r][c]
        return grid         
         
