from PyQt6.QtWidgets import QApplication
from src.window import Window
import sys

def main():
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    try:
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
