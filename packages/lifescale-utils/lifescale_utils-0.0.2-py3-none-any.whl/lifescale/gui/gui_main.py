import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow

from lifescale.gui.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window of the application."""

    def __init__(self):
        """Initializer."""

        # GUI:
        super().__init__()
        self.setupUi(self)

        # Connect signals and slots:

        # Set up GUI items and widgets:

        # Init models:


def main():
    """Main program to start the GUI."""
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the application's main window
    main_window = MainWindow()
    main_window.show()
    # Run the application's main loop:
    sys.exit(
        app.exec())  # exit or error code of Qt (app.exec_) is passed to sys.exit. Terminates pgm with standard python method


if __name__ == "__main__":
    """Main Program."""
    main()
