import time
import os
import shutil

#Note: directory.txt needs to be created that contains the directory monitored
with open("directory.txt", "r") as direct:
    directory = direct.readlines()
    directory = directory[0].strip()

#dictionary with tuples and string key-value pairs. The tuples are collections of file endings, strings are names of folders the files go into.
#the foldersetup class will automatically set up folders corresponding to the dictionary values
itemsort = {
    ('.jpg','.jpeg','.bmp','.png', '.gif'): "Images",
    ('.mp3','.wav'): "Music files",
    ('.webm','.mp4'): "Videos",
    ('.exe', '.msi', '.jar'): "Executables and Installers",
    ('.zip','.7z', '.rar'): "Archives",
    ('.docx', '.doc', '.pdf'): "Documents",
    ('.torrent'): "Torrents",
}

#if folders are not set up, this class will create them based on the itemsort values
class foldersetup:
    def __init__(self):
        os.chdir(directory)
        folders = list(itemsort.values())
        for item in folders:
            if not os.path.isdir(item):
                os.mkdir(item)

class sorter:
    def __init__(self):
        starttime = time.time()
        while True:
            self.check()
            time.sleep(15.0 - ((time.time() - starttime) % 15.0))
            
    @staticmethod
    def multikey(item):
        for keys, value in itemsort.items():
            if item in keys:
                return(value)
        return(None) 

    @staticmethod
    def check():
        items = os.listdir(directory)
        for item in items:
            ending = item[item.rfind('.')::].lower()
            folder = sorter.multikey(ending)
            if folder is not None:
                folderlocation = f"{directory}/{folder}"
                shutil.copy2(item, folderlocation)
                print(f"{item} sorted!")
                os.remove(item)

if __name__ == '__main__': 
    folder = foldersetup()
    folder
    sorter = sorter()
    sorter