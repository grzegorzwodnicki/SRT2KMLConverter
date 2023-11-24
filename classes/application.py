from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon, QFontDatabase
from PySide2.QtCore import QDir, QPoint, Qt, QRect
import os
import sys
from constants import *

class ConverterApplication(QApplication):
    resolution = RES_DESKTOP
    icon_path = LOGO_PATH
    g2_stylesheet = ''
    scale_factor = 1.0
    
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        QApplication.setWindowIcon(QIcon(self.icon_path))
        QDir.addSearchPath("images", os.path.join(os.path.abspath(sys.executable), os.path.abspath("assets/g2/")))
        self.setG2StyleSheet()

    def setG2StyleSheet(self):
        general_font_size = round(14 * self.scale_factor)
        label_font_size = round(16 * self.scale_factor)
        gray_label_font_size = round(12 * self.scale_factor)
        title_label_font_size = round(22 * self.scale_factor)
        combobox_height = round(40 * self.scale_factor)
        main_background_png = "main_background.png"

        if not self.g2_stylesheet:
            self.g2_stylesheet = f"""

           QWidget {{
                background: transparent;
                color: white;
                font: {label_font_size}px "Saira Medium";
            }}
    
            QWidget#centralwidget {{
                border-image: url("assets/g2/desktop/{main_background_png}");
            }} 
            
            QDialog {{
                background-image: url("assets/g2/desktop/background-viewer.png");
            }}
            
            QWidget#MainWindow_centralwidget {{
                background-image: url("assets/g2/desktop/{main_background_png}") 0 0 0 0;
                background-repeat: no-repeat;
                background-position: 0px;
                background-origin: content;
                padding-top: -{30*self.scale_factor}px;
            }}
            
            QMenu {{
                color: white;
                font: {general_font_size}px "Saira";
                background: #19232D;
            }}
            
            QMenuBar::item:selected, QMenu::item:selected {{
                background-color: #1A72BB;
            }}
           
            QToolButton {{
                background: transparent;
                border-image: url("assets/g2/unique-button-states/toolbutton.png");
                text-decoration: underline;
            }}
            
            QToolButton:hover {{
                color: orange;
            }}
            QToolButton:pressed {{
               margin:1 1 1 1;               
            }}
            
            Loc8G2PushButton {{
                min-width: 10px;
            }}
            
            QLineEdit{{
                background: rgba(22, 22, 22, 1);
                font: 14px "Saira Regular";
                border: rgba(22, 22, 22, 1);
                color: white;
                border-radius: 12px;
                padding-left: {0 if self.scale_factor<1 else 10}px;
            }}
            
            QComboBox {{
                border-image: url("assets/g2/text-field-3d-effect.png") 0 0 0 0 stretch stretch;
                font: {general_font_size}px "Saira";
                border: transparent;
                color: white;
                padding-left: 10px;
            }}

            QCheckBox {{
                font-size: 14px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #333333, stop: 0.4 #292929, stop:1 #1D1D1D);
                color: white;
                border-radius: 12px;
                border: 2px solid black;
                padding-left: 10px;
                padding-right: 10px;
                spacing: 0px;
            }}

            QCheckBox:hover {{
                color: #FF9D0A;
                border: 2px solid #FF9D0A;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #333333, stop: 0.4 #292929, stop:1 #1D1D1D);
            }}

            QCheckBox:checked {{
                color: #FF9D0A;
                border: 2px solid #FF9D0A;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #292929, stop:1 #121212);
            }}

            QCheckBox::indicator {{
                width: 20px;
                height: 21px;
                margin-right: 5px;
            }}
                        
            QCheckBox::indicator:checked {{
                border-image: url(assets/g2/checkbox/button_check.png) 0 0 0 0 stretch stretch;
                image: none;
            }}

            QCheckBox::indicator:unchecked {{
                border-image: url(assets/g2/checkbox/button_uncheck.png) 0 0 0 0 stretch stretch;
                image: none;
                
            }}

            QComboBox:hover {{
                color: red;
                padding-left:10px;
            }}

            QSpinBox, QDoubleSpinBox {{
                font: {general_font_size}px "Saira";
                color: white;
                background: black;
                border-radius: {12*self.scale_factor}px;
                border:2px solid black;
                min-height: {40*self.scale_factor}px;
            }}
                        
             QSpinBox::up-button, QDoubleSpinBox::up-button,
             QSpinBox::down-button, QDoubleSpinBox::down-button{{
                 subcontrol-origin: border;
                 height: {37*self.scale_factor}px;
                 width: {37*self.scale_factor}px;
             }}

             QSpinBox::up-button, QDoubleSpinBox::up-button {{
                 subcontrol-position: center right;
                  margin-right: 2px;
                 border-image: url(assets/g2/spinbox/spinbox-right.png) 0 0 0 0 stretch stretch;
             }}

             QSpinBox::down-button, QDoubleSpinBox::down-button {{
                  subcontrol-position: center left;
                  margin-left:2px;
                  border-image: url(assets/g2/spinbox/spinbox-left.png) 0 0 0 0 stretch stretch;
             }}
            
            QSpinBox::down-arrow, QSpinBox::up-arrow, QDoubleSpinBox::down-arrow, 
            QDoubleSpinBox::up-arrow {{
                width:0px;
                height:0px;
            }}

            .QFrame {{
                border-radius: 8px;
                border:2px solid #2D2E35;
                border-style: solid;
            }}

            QLabel {{
                padding: 0px;
                color: white;
                background: transparent;
            }}
            
            Loc8G2WhiteLabel {{
                font-size: {label_font_size}px;
            }}

            Loc8G2GrayLabel {{
                color: #5D616C;
                background: transparent;
                font: {gray_label_font_size}px "Saira";
                padding-left: 10px;
            }}
                        
            QLabel#lblTitle {{
                background: transparent;
                font: 13px "Audiowide";
                color: white;
            }}
            
            Loc8G2LineDisplay {{
                background: transparent;
                border: 2px solid #1C1E26;
                border-radius: {12*self.scale_factor}px;
                color:white;
                font: {general_font_size}px "Saira";
                padding:{0 if self.scale_factor<1 else 10}px;
            }}
            
            QPushButton {{
                background-image: url("assets/g2/button-states/back.png");
                border: 2px solid #181818;
                border-radius: 10px;
                font: 14px "Saira Medium";
            }}

            QPushButton#btnClose {{
                background-image: url("assets/g2/button-states/back.png") 0 0 0 0 stretch stretch;
                border: 2px solid #181818;
            }}
            
            QPushButton#btnClose:hover {{
                color: orange;
                border: 2px solid rgba(255, 157, 10, 1);
            }}

            QPushButton#btnClose:pressed {{
                border-color: orange;
                color: orange;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop: 0 #202020, stop: 0.5 #1D1D1D, stop: 1 #242424);
            }}

            QPushButton#btnStart {{
                border: 2px solid black;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop: 0 #333, stop: 0.5 #292929, stop: 1 #1D1D1D);
            }}

            QPushButton#btnStart:hover {{
                color: orange;
                border: 2px solid rgba(255, 157, 10, 1);
            }}

            QPushButton#btnStart:pressed {{
                border-color: orange;
                color: orange;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop: 0 #202020, stop: 0.5 #1D1D1D, stop: 1 #242424);
            }}

            QPushButton:hover {{
                color: orange;
                border: 2px solid rgba(255, 157, 10, 1);
            }}

            QPushButton:pressed {{   
                border-color: orange;
                color: orange;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop: 0 #202020, stop: 0.5 #1D1D1D, stop: 1 #242424);
            }}

            QProgressBar {{
                color: white;
                text-align: right;
                background: #161616;
                border-radius: 11px;
                font: 14px "Saira Regular";
            }}
            
            QProgressBar::chunk {{
                border-radius: 8px;
                margin: 3px;
                background: QLinearGradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(33, 207, 40, 0.56), stop: 1 #00E024 );
            }}

            QProgressBar#prgImagesProcessed {{
                color: #1FB029;
                background: transparent;
                padding: {round(10*self.scale_factor)} {round(40*self.scale_factor)} {round(10*self.scale_factor)} 0;
            }}
            
            QProgressBar#prgTargetsHit {{
                color: #F8564B;
                background: transparent;
                padding: {round(10*self.scale_factor)} {round(40*self.scale_factor)} {round(10*self.scale_factor)} 0;
            }}
            
            QProgressBar#prgImagesProcessed::chunk {{
                border-radius: 3px;
                background: transparent;
                background-image: url("assets/g2/GreenProgressBar.png");
            }}

            QProgressBar#prgTargetsHit::chunk {{
                border-radius: 3px;
                background: transparent;
                background-image: url("assets/g2/RedProgressBar.png");
            }}
            
            QListWidget::item::selected {{
                color:white;
            }}

            """
            qdarkstyle_stylesheet_elements = '''

            QAbstractScrollArea {
              background-color: #19232D;
              border: 1px solid #455364;
              border-radius: 4px;
              padding: 2px;
              color: #E0E1E3;
            }
            
            QAbstractScrollArea:disabled {
              color: #9DA9B5;
            }
            
            QScrollArea QWidget QWidget:disabled {
              background-color: #19232D;
            }
            
            QScrollBar:horizontal {
              height: 16px;
              margin: 2px 16px 2px 16px;
              border: 1px solid #455364;
              border-radius: 4px;
              background-color: #19232D;
            }
            
            QScrollBar:vertical {
              background-color: #19232D;
              width: 16px;
              margin: 16px 2px 16px 2px;
              border: 1px solid #455364;
              border-radius: 4px;
            }
            
            QScrollBar::handle:horizontal {
              background-color: #60798B;
              border: 1px solid #455364;
              border-radius: 4px;
              min-width: 8px;
            }
            
            QScrollBar::handle:horizontal:hover {
              background-color: #346792;
              border: #346792;
              border-radius: 4px;
              min-width: 8px;
            }
            
            QScrollBar::handle:horizontal:focus {
              border: 1px solid #1A72BB;
            }
            
            QScrollBar::handle:vertical {
              background-color: #60798B;
              border: 1px solid #455364;
              min-height: 8px;
              border-radius: 4px;
            }
            
            QScrollBar::handle:vertical:hover {
              background-color: #346792;
              border: #346792;
              border-radius: 4px;
              min-height: 8px;
            }
            
            QScrollBar::handle:vertical:focus {
              border: 1px solid #1A72BB;
            }
            
            QScrollBar::add-line:horizontal {
              margin: 0px 0px 0px 0px;
              border-image: url("assets/darkstyle/arrow_right_disabled.png");
              height: 12px;
              width: 12px;
              subcontrol-position: right;
              subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {
              border-image: url("assets/darkstyle/arrow_right.png");
              height: 12px;
              width: 12px;
              subcontrol-position: right;
              subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:vertical {
              margin: 3px 0px 3px 0px;
              border-image: url("assets/darkstyle/arrow_down_disabled.png");
              height: 12px;
              width: 12px;
              subcontrol-position: bottom;
              subcontrol-origin: margin;
            }
            
            QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {
              border-image: url("assets/darkstyle/arrow_down.png");
              height: 12px;
              width: 12px;
              subcontrol-position: bottom;
              subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:horizontal {
              margin: 0px 3px 0px 3px;
              border-image: url("assets/darkstyle/arrow_left_disabled.png");
              height: 12px;
              width: 12px;
              subcontrol-position: left;
              subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {
              border-image: url("assets/darkstyle/arrow_left.png");
              height: 12px;
              width: 12px;
              subcontrol-position: left;
              subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:vertical {
              margin: 3px 0px 3px 0px;
              border-image: url("assets/darkstyle/arrow_up_disabled.png");
              height: 12px;
              width: 12px;
              subcontrol-position: top;
              subcontrol-origin: margin;
            }
            
            QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {
              border-image: url("assets/darkstyle/arrow_up.png");
              height: 12px;
              width: 12px;
              subcontrol-position: top;
              subcontrol-origin: margin;
            }
            
            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
              background: none;
            }
            
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
              background: none;
            }
            
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
              background: none;
            }
            
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
              background: none;
            }

            QComboBox {
              selection-background-color: #346792;
            }
            
            QComboBox QAbstractItemView {
              background-color: #19232D;
              selection-background-color: #346792;
            }
            
            QComboBox QAbstractItemView:hover {
              background-color: #19232D;
              color: #E0E1E3;
            }
            
            QComboBox QAbstractItemView:selected {
              background: #346792;
              color: #455364;
            }
            
            QComboBox QAbstractItemView:alternate {
              background: #19232D;
            }
            
            QComboBox:disabled {
              background-color: #19232D;
              color: #9DA9B5;
            }
            
            
            QComboBox:on {
              selection-background-color: #346792;
            }
            
            QComboBox::indicator {
              border: none;
              border-radius: 0;
              padding-right: 0px;
              background-color: transparent;
              selection-background-color: transparent;
              color: transparent;
              selection-color: transparent;
            }
            
            QComboBox::indicator:alternate {
              background: #19232D;
            }
            
            QComboBox::item:alternate {
              background: #19232D;
            }
            
            QComboBox::drop-down {
              subcontrol-origin: padding;
              subcontrol-position: top right;
              width: 12px;
              border-left: 1px solid transparent;
            }

            QStatusBar::item { 
              border: 0px solid black 
            }
            '''
            self.g2_stylesheet += qdarkstyle_stylesheet_elements
            self.g2_stylesheet += f'''

            QDialog, QDialog:hover, QMainWindow #centralwidget {{
                border: 2px solid #666666;            }}
                
            Loc8G2PlainTextEdit {{
                color: white;
                background: transparent;
                border: transparent;
                font: {label_font_size}px "Saira";
            }}

            QComboBox::down-arrow {{
                image: url("assets/g2/unique-button-states/combobox-arrow.png");
                width: {combobox_height}px;
                height: {combobox_height}px;
                padding-right: {int(combobox_height/2)+10}px;
                padding-top: 5px;
                padding-bottom: 5px;
            }}
'''
        self.processEvents()
        self.setStyleSheet(self.g2_stylesheet)
