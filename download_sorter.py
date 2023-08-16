import os, shutil, sys, logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import exists, splitext, join

# Source path
source = "" # add your download folder path


# Destination paths
doc_dest = source + "/documents/"
img_dest = source + "/images/"
aud_des = source + "/audio/"
vid_dest = source + "/video/"
others_dest = source +"/others/"
files_dest = source + "/files/"

# File extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".psd", ".ai", ".eps"]
video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".mpeg", ".mpg", ".3gp", ".asf", ".vob", ".rm", ".swf", ".ogg", ".ogv", ".qt", ".rmvb", ".ts", ".m2ts", ".mts", ".divx", ".xvid", ".h264", ".h265"]
audio_extensions = [".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma", ".m4a", ".aiff", ".amr", ".mid", ".midi"]
document_extensions = [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".csv", ".txt", ".rtf", ".odt", ".odp", ".ods", ".pages", ".key", ".numbers"]



# Generate unique name
def uniqify(dest, name):
    filename, ext = splitext(name)
    count = 0
    while exists(f"{dest}/{name}"):
        count+=1
        name = f"{filename}_{count}{ext}"
        
    return name
        
    

# Move file to the destionation
def move(file, dest):
    name = file.name
    unique_name = uniqify(dest, name)
    
    if not exists(dest):
        os.mkdir(dest)
          
    shutil.move(file.path, f"{dest}/{unique_name}")
        
        
    
    
# Handle files on any modifications  
class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source) as files:
            for file in files:
                name = file.name
                self.check_file(name, file)
    # Check file type
    def check_file(self, name, file):
        if file.is_file():
            self.handle_files(name, file)
        else:
            self.handle_dir(file)
                
    
    # Moves files to appropriet folders
    def handle_files(self,name, file):
        _, ext = splitext(name)
        if ext.lower() in document_extensions:
            move(file, doc_dest)
        elif ext.lower() in image_extensions:
            move(file, img_dest)
        elif ext.lower() in audio_extensions:
            move(file, aud_des)
        elif ext.lower() in video_extensions:
            move(file, vid_dest)
        else:
            move(file, others_dest)
        
    
    # Handles directory 
    def handle_dir(sef, file):
        if file.path+'/' not in [doc_dest, img_dest, aud_des, vid_dest, others_dest, files_dest]:
            move(file, files_dest)
        
        
      
# Starting point  
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()