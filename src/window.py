""" Main File for Window management """
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QColor, QPixmap
from src.fire import Fire
from src.engine import RandomEngine

WINDOW_TITLE = "Fire animation"
TIMER = 30

class Window(QMainWindow):
    """ Window class to interact with """
    def __init__(self):
        super().__init__()

        # Core objects
        self.fire = Fire()
        self.engine = RandomEngine()

        # Window configs
        self.setWindowTitle(WINDOW_TITLE)
        self.setStyleSheet("background-color: black;")      

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 
        self.main_layout = QVBoxLayout(self.central_widget)

        # Fire Layout
        self.fire_label = QLabel()
        self.fire_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.fire_label)
    
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(TIMER)

    def update_ui(self):
        """ Updates the whole window """
        
        # Get the fire drawing
        self.fire.intensity = self.engine.get_random(self.fire.cols)
        self.fire.update()
        
        # Draw it
        image = QImage(self.fire.cols, self.fire.rows, QImage.Format.Format_RGB888)

        for r in range(self.fire.rows):
            for c in range(self.fire.cols):
                image.setPixelColor(c, r, self.fire.grid[r][c])

        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(
            self.fire_label.width(),
            self.fire_label.height(),
            Qt.AspectRatioMode.IgnoreAspectRatio, # Estica pra preencher
            Qt.TransformationMode.FastTransformation # Mantém pixelado
        )

        self.fire_label.setPixmap(scaled_pixmap)

