""" Main File for Window management """
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QGridLayout)
from PyQt6.QtCore import QTimer
from src.fire import Fire
from src.engine import RandomEngine

WINDOW_TITLE = "Fire animation"
WIDTH = 1000
HEIGHT = 800
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
        self.resize(WIDTH, HEIGHT)
        self.setStyleSheet("background-color: black;")      

        # PyQt6 shit
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget) 
        self.main_layout = QVBoxLayout(self.central_widget)

        # Fire Grafic
        self.fire_widget = QWidget()
        self.fire_layout = QGridLayout(self.fire_widget)
        self.main_layout.addWidget(self.fire_widget, stretch=1)
    
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(TIMER)

    def update_ui(self):
        """ Updates the whole window """
        
        # Get the fire intensity vector
        self.fire.intensity = self.engine.get_random(10)

        # Draw the fire image
        

