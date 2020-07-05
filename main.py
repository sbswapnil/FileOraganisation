import os
import shutil
from datetime import datetime, date
from log import logFile


class Organiser:
    directory = {
        "txt": "Text Files",
        "doc": "Documents",
        "docx": "Documents",
        "jpg": "Images",
        "jpeg": "Images",
        "exe": "Executable Files",
        "pptx": "PPT Files",
        "ppt": "PPT Files",
        "zip": "Zip Files",
        "xlsx": "Excel Files",
        "xls": "Excel Files",
        "avi": "Movies",
        "mpg": "Movies",
        "mp4": "Movies",
        "mp3": "Movies",
        "mov": "Movies",
        "m4v": "Movies",
        "mp4v": "Movies",
        "3gp": "Movies",
        "mkv": "Movies",
    }

    def __init__(self, dir="C:\\Users\\" + os.getlogin() + "\\Downloads\\"):
        # print("old dir " + os.getcwd())
        os.chdir(dir)
        self.path = os.getcwd()
        self.filename = ""
        print("new dir " + os.getcwd())
        logFile(log='\n'+str(date.today()))
        logFile(log=f"following changes are applied on {self.path} Directory")
        # print("os path ",os.path)
        self.run()

    def run(self):
        print(f"\nFiles under {self.path} Directery\n")
        with os.scandir(self.path) as dirs:
            for dir in dirs:
                if os.path.isfile(os.path.join(self.path, dir)):
                    self.filename = dir.name
                    if self.filename == "log.txt":
                        continue
                    print(self.filename)
                    file, extension = self.find_extension(filename=self.filename)
                    print(f"{file} is in  {extension} format")

                    if extension not in self.directory.keys():
                        self.directory[extension] = extension.capitalize() + " Files"

                    folderName = self.directory[extension]

                    # check folder is there or not
                    if os.path.exists(os.path.join(self.path, folderName)):

                        # if file with same name is already in the folder then rename our file
                        if os.path.exists(os.path.join(self.path, folderName+"\\"+self.filename)):
                            t = self.currentTime()
                            os.rename(self.filename, file+t+"."+extension)
                            logFile(log=f"{self.filename} rename to {file+t+'.'+extension}")
                            self.filename = file+t+"."+extension

                        # moveing file to folder
                        logFile(log=f"{self.filename} moved to {folderName} ")
                        shutil.move(os.path.join(self.path, self.filename), os.path.join(self.path, folderName))

                    else:
                        os.mkdir(os.path.join(self.path, folderName))
                        print(folderName, f"folder created for {extension} files")
                        logFile(log=f"{folderName} folder created for {extension} files")
                        shutil.move(os.path.join(self.path, self.filename), os.path.join(self.path, folderName))
                        logFile(log=f"{self.filename} moved to {folderName} ")

    def find_extension(self, filename):
        file, extension = filename.rsplit('.', 1)
        return file, extension

    def currentTime(self):
        now = datetime.now()
        return str(now.strftime("%H_%M_%S"))