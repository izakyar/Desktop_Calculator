import PyQt6 as gui
import sys
from output import *
from initalize import *
from PyQt6.QtWidgets import QApplication
from PyQt6 import *

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('CalculatorYZ')
    window.setGeometry(100, 100, 400, 700)
    # Create a QLabel for your text
    text_label = QLabel("Output:", parent=window)
    text_label.move(20, 20) # Position the label (x, y) from top-left of the window

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
