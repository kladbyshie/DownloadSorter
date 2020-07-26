import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

class OnMyWatch:
    def __init__(self):
        os.chdir(directory)
        self.observer = Observer()
    
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, directory) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def multikey(item):
        for keys, value in itemsort.items():
            if item in keys:
                return(value)
        return(None) 

    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None
        
        #this checks files created in the directory and then moves/deletes them to the appropriate folder
        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)
            filename = event.src_path[event.src_path.find('\\')+1::]
            ending = filename[filename.find('.')::].lower()
            folder = Handler.multikey(ending)
            if folder is not None:
                folderlocation = f"{directory}/{folder}"
                while True:
                    if os.path.exists(event.src_path):
                        shutil.copy2(event.src_path, folderlocation)
                        print(f"{filename} sorted!")
                        os.remove(event.src_path)
                        break
                    else:
                        #in case the file "does not exist" it sleeps and tries to sort it out again
                        time.sleep(1)
                        continue
                    
                
if __name__ == '__main__': 
    watch = OnMyWatch()
    folder = foldersetup()
    folder
    watch.run()