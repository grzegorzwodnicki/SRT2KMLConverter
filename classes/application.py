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

