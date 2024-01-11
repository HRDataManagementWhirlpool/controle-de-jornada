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
        
        # EXIBIR APLICAÇÃO
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())