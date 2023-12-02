import os
import sys
sys.path.append(os.path.abspath('../'))
from constants import *

import re
import xml.etree.ElementTree as ET
import json

class SRT2KMLConverterEngine:
    
    def __init__(self):
        self.loadedData = []
        self.fileName = ""
        self.baseName = ""
    def parseSRTRecord(self, rec):
        SRTRecord = {}
        if len(rec) < 3:
            return False
        lat_long_pattern = r'\[latitude: ([\-\d\.]+)\] \[longitude: ([\-\d\.]+)\]'
        SRTRecord['id'] = rec[0]
        _period = 'm'.join(rec[1].split('-->')[-1].split(':')[1:3]).replace(',','.')
        SRTRecord['name'] = self.baseName + '_' + _period
        
        match = re.search(lat_long_pattern, ''.join(rec))
        lat = 0.0
        long = 0.0
        if match:
            lat, long = match.groups() 
        else:
            return False
        SRTRecord['lat'] = float(lat)
        SRTRecord['long'] = float(long)
        self.loadedData.append(SRTRecord)
        return True
    
    def loadFile(self, filename): 
        try:
            _file = open(filename, "r")
            self.fileName = os.path.basename(filename)
            self.baseName, _ = os.path.splitext(self.fileName)
        except IOError as e:
            return False
       
        _st  = _file.read().replace("\r", "")
        _file.close()
        _lines = _st.split("\n")
        self.loadedData.clear()
        _temp = []
        for _ln in _lines:
            if _ln.strip() != "":
                _temp.append(_ln)
            else:
                if (len(_temp)>0):
                    if self.parseSRTRecord(_temp) == False:
                        return False
                    _temp.clear()
                
        if len(_temp)>0:
            if self.parseSRTRecord(_temp) == False:
                return False
            
        
        
                
        
        
        
        
if __name__ == '__main__':
    _convert = SRT2KMLConverterEngine()
    _convert.loadFile('C:\Projects\SRT_Converter\SRT_Sample\DJI_20230919231119_0001_S.SRT')
    
