import os
from constants import *
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
import json
import tempfile
import zipfile

class SRT2KMLConverterEngine:
    
    def __init__(self, progressCallBack = None):
        self.loadedData = []
        self.fileName = ""
        self.baseName = ""
        self.progressCallBack = progressCallBack
        self.lastProgress = 0
        
    def callProgress(self, progress):
        if (int(progress)!=self.lastProgress):
            if self.progressCallBack != None:
                self.progressCallBack(int(progress))
        self.lastProgress = int(progress)
        
    def convertFile(self, src, dst, type):
        if not self.loadedFile(src):
            return False
        if type == DRONE_FORMAT_KML or type == DRONE_FORMAT_KMZ:
            return self.convertToKML(dst, type)
        if type == DRONE_FORMAT_GPX:
            return self.convertToGPX(dst)
        if type == DRONE_FORMAT_JSON:
            return self.convertToJSON(dst)
        
    def convertToGPX(self, dst, prettyXML = True):
            if len(self.loadedData) == 0:
                return False
            gpx = ET.Element("gpx", xmlns="http://www.topografix.com/GPX/1/1", 
                 xmlns_gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3", 
                 creator="USR", version="1.1")
            progress = 50.0
            progressStep = 50/len(self.loadedData)
            for rec in self.loadedData:
                wpt = ET.SubElement(gpx, "wpt", lat=str(rec['lat']), lon=str(rec['long']))
                name = ET.SubElement(wpt, "name")
                name.text = rec['name']
                progress += progressStep
                self.callProgress(progress)
            xml_string = ET.tostring(gpx, encoding='unicode', method='xml')
            if prettyXML:
                reparsed = minidom.parseString(xml_string)
                xml_string = reparsed.toprettyxml(indent="  ")        
            try:      
                with open(dst, "w", encoding="utf-8") as f:            
                    f.write(xml_string)
            except IOError as e:
                return False
            self.callProgress(100)
            return True
                
    def convertToKMLKMZ(self, dst, type, prettyXML = True):
        if len(self.loadedData) == 0:
                return False
        kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2", 
                 xmlns_gx="http://www.google.com/kml/ext/2.2")
        plcId = 3
        pointId = 2
        document = ET.SubElement(kml, "Document", id="1")
        progress = 50.0
        progressStep = 50/len(self.loadedData)
        for rec in self.loadedData:
            placemark = ET.SubElement(document, "Placemark", id=str(plcId))
            plcId += 2
            ET.SubElement(placemark, "name", name=rec['name'])
            point = ET.SubElement(placemark, "Point", id=str(pointId))
            pointId += 2
            coordinates = ET.SubElement(point, "coordinates")
            coordinates.text = str(rec['long'])+","+str(rec['lat'])
            progress += progressStep
            self.callProgress(progress)
            
        xml_string = ET.tostring(kml, encoding='unicode', method='xml')
        if prettyXML:
            reparsed = minidom.parseString(xml_string)
            xml_string = reparsed.toprettyxml(indent="  ")        
        
        if type == DRONE_FORMAT_KML:
            try:      
                with open(dst, "w", encoding="utf-8") as f:            
                    f.write(xml_string)
            except IOError as e:
                return False
            
        if type == DRONE_FORMAT_KMZ:
            
            try:     
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_file_path = os.path.join(temp_dir, "doc.kml")
                    with open(temp_file_path, "w", encoding="utf-8") as f:
                          f.write(xml_string)
                    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zipf:
                         zipf.write(temp_file_path, "doc.kml")
                         
            except IOError as e:
                return False
        self.callProgress(100)
        return True
    
    
    def convertToJSON(self, dst, prettyJSON = True):
        if len(self.loadedData) == 0:
                return False
        features = []
        progress = 50.0
        progressStep = 50/len(self.loadedData)
        for rec in self.loadedData:
            rec = {"id":'id', "type":'Feature', 
                   "geometry": {"coordinates":[rec['long'], rec['lat'], 0, 0], "type":"Point"}, 
                    "properties": {"marker-symbol": "point", 
                                   "marker-color": "#FF0000", 
                                   "title": rec['name'], "class": "Marker", "updated": 0}                      
                                }
            features.append(rec)
            progress += progressStep
            self.callProgress(progress)
            
        idnt = None
        if prettyJSON:
            idnt = 4
        json_st = json.dumps({"features":features, "type":"FeatureCollection"}, indent=idnt)
        try:
            f = open(dst, "w")
            f.write(json_st)
            f.close()
        except IOError as e:
            return False
        
        self.callProgress(100)
        return True
            
    
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
        self.lastProgress = 0
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
        progress = 0.0
        progressStep = 50/len(_lines)
        for _ln in _lines:
            if _ln.strip() != "":
                _temp.append(_ln)
            else:
                if (len(_temp)>0):
                    if not self.parseSRTRecord(_temp):
                        return False
                    _temp.clear()
            progress += progressStep
            self.callProgress(progress)
                
        if len(_temp)>0:
            if self.parseSRTRecord(_temp):
                return False
                
if __name__ == '__main__':
    _convert = SRT2KMLConverterEngine()
    _convert.loadFile('..\SRT_Sample\CDJI_20230919231119_0001_S.SRT')
    _convert.convertToJSON("export.json", False)
    _convert.convertToGPX("export.gpx")
    _convert.convertToKMLKMZ('export.kmz', DRONE_FORMAT_KMZ)
    _convert.convertToKMLKMZ('export.kml', DRONE_FORMAT_KML)
    
