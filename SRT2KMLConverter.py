from PySide2.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox
from PySide2.QtCore import Qt
import sys
from classes.Application import ConverterApplication
from ui.SRT2KMLConverter import Ui_SRT2KMLConverter
import time
import os
from classes.Settings import SettingsClass
from constants import *
from classes.ConverterEngine import SRT2KMLConverterEngine
import threading

CONVERT_NO_ERRORS = 0
CONVERT_ERROR_LOADING = 1
CONVERT_ERROR_CONVERTING = 2

class SRT2KMLConverter(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.converter = SRT2KMLConverterEngine(self.progress)
        self.ui = Ui_SRT2KMLConverter()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.config = SettingsClass(
            os.path.join(os.path.dirname(__file__), "config.ini")
        )
        
        
        self.ui.btnChooseSource.clicked.connect(self.chooseSource)
        self.ui.btnChooseOutput.clicked.connect(self.chooseOutput)
        self.buttons_extensions_dict = {
            self.ui.btnKML: DRONE_FORMAT_KML,
            self.ui.btnKMZ: DRONE_FORMAT_KMZ,
            self.ui.btnGPX: DRONE_FORMAT_GPX,
            self.ui.btnJSON: DRONE_FORMAT_JSON,
        }
        
        self.all_types = list(self.buttons_extensions_dict.values())
        
        self.loadSettings()
        
        for button in self.buttons_extensions_dict:
            button.clicked.connect(self.changeOutputFileExtension)

        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnClose.clicked.connect(self.close)
        
    def closeEvent(self, event):
        self.config.config_output_path = self.ui.txtOutputFile.text()
        self.config.config_input_path = self.ui.txtSource.text()
        self.config.config_filetype = self.getOutputFormat()
        self.config.write_config()
        
    def progress(self, value):
        self.ui.progressBar.setValue(value)
        
    def loadSettings(self):
        if self.config.config_filetype not in self.all_types:
            self.config.config_filetype = DRONE_FORMAT_KML
        for ch in self.buttons_extensions_dict.keys():
            ch.setChecked(self.config.config_filetype == self.buttons_extensions_dict[ch])
            
        self.ui.txtSource.setText(self.config.config_input_path)
        self.ui.txtOutputFile.setText(self.config.config_output_path)

    def changeOutputFileExtension(self):
        for btn in self.buttons_extensions_dict:
            if btn == self.sender():
                output_format = self.buttons_extensions_dict[btn]
            else:
                btn.setChecked(False)
        self.config.config_filetype = output_format
        if len(self.ui.txtOutputFile.text())>0:
            output_file = self.ui.txtOutputFile.text()
            if output_file:          
                filename, _ = os.path.splitext(output_file)
                new_output_file = filename + "." + output_format
                self.ui.txtOutputFile.setText(new_output_file)


    def chooseSource(self):
        last_open_dir = os.path.dirname(self.ui.txtSource.text())
        if not os.path.exists(last_open_dir):
            last_open_dir = os.path.dirname(self.config.config_input_path)
        input_file, _ = QFileDialog.getOpenFileName(
            self, "Open SRT file", last_open_dir, "SRT Files (*.srt)"
        )
        if input_file:
            self.ui.txtSource.setText(input_file)
            self.config.config_input_path = input_file
            
    def getOutputFormat(self):
        output = DRONE_FORMAT_KML
        for chk in self.buttons_extensions_dict.keys():
            if (chk.checkState()):
                output = self.buttons_extensions_dict[chk]
        return output
    
    def generateAllTypesForDialog(self, current):
        _all = []
        for chk in self.buttons_extensions_dict.keys():
            _file = self.buttons_extensions_dict[chk]
            _all.append(_file)
            to_move = False
            if (_file == current):
                to_move = True
                
            if (_file == 'json'):
                _file = 'GeoJSON'
            else:
                _file = _file.upper()
        
            _all[-1] = '{0} file (*.{1})'.format(_file, _all[-1])
            if to_move:
                _temp = _all[-1]
                _all[-1] = _all[0]
                _all[0] = _temp  
                
        return ';;'.join(_all)          
    
    def updateType(self, output_file):
        _, ext = os.path.splitext(output_file)
        ext = ext.replace(".","")
        if ext.lower() in self.all_types:
            for chk in self.buttons_extensions_dict.keys():
                chk.setChecked(ext.upper() == self.buttons_extensions_dict[chk].upper())
                    
    def chooseOutput(self):
        last_open_dir = os.path.dirname(self.ui.txtOutputFile.text())
        if not os.path.exists(last_open_dir):
            last_open_dir = os.path.dirname(self.config.config_output_path)
        output_file, _ = QFileDialog.getSaveFileName(self,"Chose saving file",
                    last_open_dir, self.generateAllTypesForDialog(self.getOutputFormat()))
        if output_file:
            self.ui.txtOutputFile.setText(output_file)
            self.updateType(output_file)


            
 
    def convertFile(self, _input, _output, _format):
        self.returnStatus = CONVERT_NO_ERRORS
        if not self.converter.loadFile(_input):   
            self.returnStatus = CONVERT_ERROR_LOADING
            return
        if not self.converter.convertFile(_output, _format):
            self.returnStatus = CONVERT_ERROR_CONVERTING

    def start(self):
        self.errors = None
    
        source_path = self.ui.txtSource.text()
        output_path = self.ui.txtOutputFile.text()
        output_format = self.getOutputFormat()
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setValue(0)
        
        if source_path.strip() == '':
            QMessageBox.critical(None, 'Error',"Please select source file")
            return

        if output_path.strip() == '':
            QMessageBox.critical(None, 'Error',"Please select output file")
            return
            
        self.thr = threading.Thread(target=self.convertFile, args=(source_path, output_path, output_format))
        self.thr.start()

       
        

        self.ui.btnStart.setStyleSheet(
            "QPushButton#btnStart {"
            "   border-color: orange;"
            "   color: orange;"
            "   background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #202020, stop:0.5 #1D1D1D, stop:1 #242424);"
            "}"
        )
        self.ui.btnStart.setText("Stop")
        self.ui.btnStart.clicked.disconnect()
        self.ui.btnStart.clicked.connect(self.end)


        while True:
            time.sleep(0.1)
            QApplication.instance().processEvents()
            if not self.thr.is_alive():
                self.end()
                break
        if (self.returnStatus == CONVERT_ERROR_LOADING) and (not self.converter.convAborted):
            QMessageBox.critical(None, 'Error',"Error during loading and parsing Source File.")
            
    
        if (self.returnStatus == CONVERT_ERROR_CONVERTING) and (not self.converter.convAborted):
            QMessageBox.critical(None, 'Error',"Error during converting file.")
            
        if (self.returnStatus == CONVERT_NO_ERRORS) and (not self.converter.convAborted):
            QMessageBox.information(None, 'Information',"File converted.")

             
             
    def end(self):
        self.converter.stop()
        if self.converter.convAborted:
            QMessageBox.information(None, 'Information',"Convert aborted.")
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
        


if __name__ == "__main__":
    app = ConverterApplication(sys.argv)
    w = SRT2KMLConverter()
    w.show()
    sys.exit(app.exec_())
