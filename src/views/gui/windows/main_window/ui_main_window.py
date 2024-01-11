from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        parent.resize(1200, 600)
        parent.setMinimumSize(960, 540)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282A36")
        
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475A")
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)
        
        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")
        
        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
        
        # TOP BTNS
        self.toggle_button = PyPushButton(
            text="Ocultar menu"
            )
        self.btn_1 = PyPushButton(
            text="Página Inicial",
            is_active=True
        )
        self.btn_2 = PyPushButton(
            text="Página 2"
        )
        
        # ADD TOP BTNS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        
        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red; }")

        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        # BOTTOM BTNS
        self.settings_btn = PyPushButton(
            text="Configurações"
        )
        
        # ADD BOTTOM BTNS TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)
        
        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #C3CCDF")
        
        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282A36")
        
        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232D; color: #6272A4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        # TOP LEFT LABEL
        self.top_label_left = QLabel("Essa é a minha primeira tela")
        
        # TOP SPACER
        self.top_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # TOP RIGHT LABEL
        self.top_label_right = QLabel("Mensagem à direita")
        
        # ADD TO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #F8F8F8")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        
        # BOTTOM BAR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232D; color: #6272A4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)
        
        # BOTTOM LEFT LABEL
        self.bottom_label_left = QLabel("Parte inferior da tela")
        
        # BOTTOM SPACER
        self.bottom_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # BOTTOM RIGHT LABEL
        self.bottom_label_right = QLabel("Mensagem à direita")
        
        # ADD TO LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # ADD TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)