import configparser
from constants import *

class SettingsClass:
   
    def __init__(self, fileName):
        self.__settingsList = []
        self.__configClass = configparser.ConfigParser()
        self.__configFile = fileName
        self.__section = "settings"

        #settings list, name must start with config_
        self.config_input_path =''
        self.config_output_path =''
        self.config_filetype = DRONE_FORMAT_KML


        #get config list from class atributes
        for z in self.__dir__():
            if z.startswith("config_"):
                self.__settingsList.append(z)
        self.__read_file()
       
        
    def __read_file(self):
        self.__configClass.read(self.__configFile)
        for s in self.__settingsList:
            if self.__section in self.__configClass:
                if s in self.__configClass[self.__section]:
                    self.__setattr__(s, self.__configClass[self.__section][s])
        

    def write_file(self):
        if self.__section not in self.__configClass:
            self.__configClass[self.__section] = {}
        for sf in self.__settingsList:
            self.__configClass[self.__section][sf] = self.__getattribute__(sf)
        with open(self.__configFile, 'w') as configfile:
            self.__configClass.write(configfile)

        


   
   