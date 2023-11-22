from PySide2.QtWidgets import QFileDialog, QApplication, QMainWindow
from PySide2.QtCore import Qt
import sys
from classes.application import ConverterApplication
from ui.SARTopoKMLConverter import Ui_SARTopoKMLConverter
import time
import os
from classes.settings import SettingsClass

class SARTopoKMLConverterWindow(QMainWindow):

    errors = None

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        #self.converter = SARTopoConverter()
        self.ui = Ui_SARTopoKMLConverter()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.config = SettingsClass(os.path.join(os.path.dirname(__file__),'config.ini'))
        
        self.ui.btnChooseSource.clicked.connect(self.chooseSource)
        self.ui.btnChooseOutput.clicked.connect(self.chooseOutput)
        #self.buttons_extensions_dict = {
        #    self.ui.btnDJI:DRONE_FORMAT_DJI,
        #    self.ui.btnKMZ:DRONE_FORMAT_KMZ,
        #    self.ui.btnGPX:DRONE_FORMAT_GPX,
        #    self.ui.btnJSON:DRONE_FORMAT_JSON
        #    }
        #self.extensions_buttons_dict = {v: k for k, v in self.buttons_extensions_dict.items()}
        #for button in self.buttons_extensions_dict:
        #    button.clicked.connect(self.changeOutputFileExtension)
        #self.loadSettings()
        
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnClose.clicked.connect(self.close)
        self.show()
    def chooseSource(self):
        last_open_dir = os.path.dirname(self.ui.txtOutputFile.text())
        if not os.path.exists(last_open_dir):
            last_open_dir = self.config.config_input_path
        #output_format = self.getOutputFormat()
        QFileDialog.getExistingDirectory(self,'')
        #output_file, mask = QFileDialog.getSaveFileName(self,
        #     self.tr("Choose saving destination").format(output_format.upper()),
        #     os.path.join(last_open_dir, self.tr('Locations')+'.'+output_format),
        #     "{} "+self.tr("files")+" (*.{})".format(output_format.upper(), output_format))
        #if output_file:
        #    self.ui.txtOutputFile.setText(output_file)

    def chooseOutput(self):
        last_open_dir = os.path.dirname(self.ui.txtOutputFile.text())
        if not os.path.exists(last_open_dir):
            last_open_dir = self.config.config_input_path
        #output_format = self.getOutputFormat()
        QFileDialog.getExistingDirectory(self,'')
        #output_file, mask = QFileDialog.getSaveFileName(self,
        #     self.tr("Choose saving destination").format(output_format.upper()),
        #     os.path.join(last_open_dir, self.tr('Locations')+'.'+output_format),
        #     "{} "+self.tr("files")+" (*.{})".format(output_format.upper(), output_format))
        #if output_file:
        #    self.ui.txtOutputFile.setText(output_file)


    def start(self):
        self.errors = None
#        source_path = self.ui.txtSource.text()
#        output_path = self.ui.txtOutputFile.text()
#        output_format = self.getOutputFormat()
#        self.t = threading.Thread(target=self.converter.start, args=(source_path, output_path, output_format), daemon=True)
#        self.t.start()
#        self.ui.btnStart.setStyleSheet(
#            "QPushButton#btnStart {"
#            "   border-color: orange;"
#            "   color: orange;"
#            "   background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #202020, stop:0.5 #1D1D1D, stop:1 #242424);"
#            "}"
#        )
#        self.ui.btnStart.setText("Stop")
#        self.ui.btnStart.clicked.disconnect()
#        self.ui.btnStart.clicked.connect(self.end)
#        self.ui.progressBar.setMaximum(0)
        
        while True:
            time.sleep(.1)
            QApplication.instance().processEvents()
            if not self.t.is_alive():
                self.end()
                break

    def end(self):
        print("End application")
        self.ui.btnStart.setText("Start")
        self.ui.btnStart.clicked.disconnect()
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        self.ui.btnStart.setStyleSheet(
            "QPushButton#btnStart {"
            "    border: 2px solid black;"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #333, stop: 0.5 #292929, stop: 1 #1D1D1D);"
            "}"
            "QPushButton#btnStart:hover {"
            "    color: orange;"
            "    border: 2px solid rgba(255, 157, 10, 1);"
            "}"

            "QPushButton#btnStart:pressed {"
            "    border-color: orange;"
            "    color: orange;"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #202020, stop: 0.5 #1D1D1D, stop: 1 #242424);"
            "}"
        )
        self.converter.stop()




if __name__ == '__main__':
    app = ConverterApplication([])
    w = SARTopoKMLConverterWindow()
    sys.exit(app.exec_())

    

