import os
import json
import zipfile
import math
import classes.exreg
from pykml import parser

DRONE_FORMAT_DJI = 'kml'
DRONE_FORMAT_KMZ = 'kmz'
DRONE_FORMAT_GPX = 'gpx'
DRONE_FORMAT_JSON = 'json'
DJI_TEMPLATE = "ui/assets/DJI_Template.kml"

class SARTopoConverter():

    error = None

    def start(self, source_file, output_file, format):
        self.error = None
        if not os.path.exists(source_file):
            self.error = self.tr("Source file does not exist.")
            return
        self.getDataFromSARTopoFile(source_file)
        if not self.data:
            self.error = self.tr("The source file seems to be corrupt or empty.")
            return
        self.output_file = output_file
        self.format = format
        self.saveData()

    def getDataFromSARTopoFile(self, source_file):
        print("anyway here comes")
        self.data = []
        with open(source_file) as f:
            kml_object = parser.parse(f)
        for e in kml_object.xpath('//*[contains(local-name(), "coordinates")]/text()'):
            print(e)
            points = e.split('\n')
            for point in points:
                point = point.split(',')
                try:
                    lon, lat, alt = float(point[0]), float(point[1]), float(point[2])
                    if lat and lon and not math.isnan(lat) and not math.isnan(lon):
                        self.data.append((lon, lat, alt))
                except (ValueError, IndexError):
                    print(f"Wrong data: {point}")
 
    def saveData(self):
        if self.format == DRONE_FORMAT_DJI:
            self.saveKML(zip=False)
        elif self.format == DRONE_FORMAT_KMZ:
            self.saveKML(zip=True)
        elif self.format == DRONE_FORMAT_GPX:
            self.saveGPX()
        elif self.format == DRONE_FORMAT_JSON:
            self.saveGeoJSON()
        print("saved.")

    def saveKML(self, zip=False):
        with open(DJI_TEMPLATE, 'r', encoding='utf-8') as t:
            template = t.read()
        insert_text = ''
        for i, row in enumerate(self.data):
            lon, lat, alt = row[0], row[1], row[2]
            insert_text += f"{lon},{lat},{alt} "
        template = template.replace('*', insert_text)
        if not zip:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(template)
        else:
            with zipfile.ZipFile(self.output_file, 'w') as zf:
                zf.writestr('doc.kml', template)
            #zipfile handling

    def saveGPX(self):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("""<?xml version="1.0"?>""")
            f.write("""<gpx xmlns="http://www.topografix.com/GPX/1/1" 
            xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" 
            creator="USR" version="1.1">""")
            for row in self.data:
                lon, lat, point_name = row[0], row[1], row[2]
                f.write("""
                <wpt lat="{}" lon="{}"><name>{}</name></wpt>
                """.format(lat, lon, point_name))
            f.write("</gpx>")

    def saveGeoJSON(self):
        geojson = {}
        geojson['features'] = []
        for num, row in enumerate(self.data):
            lat, lon = row[0], row[1]
            point = {}
            point['id'] = exreg.getone("[a-e\d]{8}\-[a-e\d]{4}\-[a-e\d]{4}\-[a-e\d]{4}\-[a-e\d]{12}")
            point['type'] = 'Feature'
            point['geometry'] = {'coordinates': [float(lon), float(lat), 0, 0],
                                 'type': 'Point'}
            point['properties'] = {
                'marker-symbol': 'point',
                'marker-color': '#FF0000',
                'title': f'Point {num+1}',
                'class': 'Marker',
                'updated': 0
                }
            geojson['features'].append(point)
        geojson['type'] = "FeatureCollection"
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(geojson, f)

    def tr(self, msg):
        return msg

if __name__=='__main__':
    os.chdir('..')
    source_file = "Caltopo XML File.kml"
    source_file = "SARTopo export.kml"
    extractor = SARTopoExtractor()
    extractor.start(source_file, "dji.kml", DRONE_FORMAT_DJI)
    extractor.start(source_file, "dji.kmz", DRONE_FORMAT_KMZ)
    extractor.start(source_file, "dji.gpx", DRONE_FORMAT_GPX)
    extractor.start(source_file, "dji.json", DRONE_FORMAT_JSON)
    print(extractor.error)