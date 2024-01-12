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
        
        # BTN HOME
        self.ui.btn_1.clicked.connect(self.show_page_1)
        
        # BTN WIDGET
        self.ui.btn_2.clicked.connect(self.show_page_2)
        
        # BTN SETTINGS
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        
        # CHANGE TEXT
        self.ui.ui_pages.btn_change_text.clicked.connect(self.change_text)
        
        # EXIBIR APLICAÇÃO
        self.show()
        
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
        
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)
        
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)
        
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)
        
    # CHANGE TEXT
    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = f"Olá, {text}"
        self.ui.ui_pages.label_3.setText(new_text)
        
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