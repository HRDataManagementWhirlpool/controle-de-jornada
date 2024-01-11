import sys
import os

from qt_core import *

from gui.windows.main_window.ui_main_window import *

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tela Principal")
        
        # SETUP MAIN WINDOW
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        
        # TOGGLE BUTTON
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
        # EXIBIR APLICAÇÃO
        self.show()
        
    def toggle_button(self):
        
        # GET MENU WIDTH
        menu_width = self.ui.left_menu.width()
        
        # CHECK WITH
        width = 50
        if menu_width == 50:
            width = 240
        
        # START ANIMATION
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())