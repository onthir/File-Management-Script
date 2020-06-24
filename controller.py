# folder management script written in python
# author: Bibek Bhandari
# date: 06/05/2020
# description: this script will read from the directory that the user provides and moves the files to specific folder of their category
import os
import shutil

class Flodder:

    # initializer
    def __init__(self):
        super().__init__()

        # store summary
        self.pictures = 0
        self.videos = 0
        self.music = 0
        self.documents = 0
        self.compressed = 0
        self.programming = 0
        self.setup = 0

        self.extensions = {
            "1": [".img", ".jpeg", ".jpg", ".gif", ".png", ".tiff", ".bmp", ".eps", ".jfif"],
            "2": [".mp4", ".avi", ".mpeg4", ".flv", ".mov", ".wmv", ".mkv", ".sfx"],
            "3": [".mp3", ".wav", "m4a", ".ogg"],
            "4": [".exe", ".dmg", ".iso", ".msi", ".msu"],
            "5": [".pdf", ".doc", ".docx", ".ppt", ".csv", ".xlsx", ".odp", ".ppt", ".pps", ".odt", ".txt", ".rtf", ".xlsm", ".xlsb", ".xls", ".CSV", ".srt"],
            "6": [".zip", ".rar", ".tar.gz", ".z", ".7z", ".deb"],
            "7": [],
            "8": [".java", ".py", ".css", ".html", ".pas", ".json", ".php", ".data"]
        }

    # method to move the file
    def move(self, directoryA, directoryB):
        shutil.move(directoryA, directoryB)
    
    # delete the file
    def delete(self, directory):
        os.remove(directory)

    # make directory
    def makeDir(self, path):
        os.mkdir(path)

    # return extensions values
    def extensionVals(self):
        return self.extensions.values()

    # classify the file types
    def classify(self, path):
        altKey = "7"
        # classify the images
        # extract the extension
        filename, file_path = os.path.splitext(path)
        
        # check against our image dictionary
        values = self.extensionVals()
        keys = self.extensions.keys()
        if len(file_path) != 0:
            # loop through values
            result_list= []
            for value in values:
                if file_path in value:
                    result_list = value
                    

            # get the key for corresponding values of the list
            
            for key in self.extensions.keys():
                if(self.extensions[key] == result_list):
                    altKey = str(key)
                    # don't check after that
                    break
        else:
            altKey = "7"
        # return the corresponding key value for further analysis 
        return altKey

    # make default irectories
    def makeDefault(self, path):
        # this will create default directories
        defs = ["Documents", "Music", "Pictures", "Videos", "Setup", "Unknown", "Compressed", "Programming"]
        for directory in defs:
            if not os.path.exists(path + "/" + str(directory)):
                self.makeDir(path+"/"+ str(directory))
                print("Created: " + directory)


    # list all the files from provided path
    def listAll(self, path):
        return os.listdir(path)