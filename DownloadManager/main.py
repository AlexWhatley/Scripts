import os
import shutil
import paths

mainpath = 'C:\\Users\\alexp\\Downloads'
os.chdir(mainpath)
for root, dirs, files in os.walk(mainpath):
    for file in files:
        try:
            if ".jpg" in file:
                shutil.move(file, paths.jpgpath)
            elif ".png" in file:
                shutil.move(file, paths.pngpath)
            elif ".webp" in file:
                shutil.move(file, paths.otherimagepath)
            elif ".exe" in file:
                shutil.move(file, paths.exepath)
            elif ".pdf" or ".docx" or ".doc" or ".pptx" in file:
                shutil.move(file, paths.pdfdocxpath)
            elif ".txt" in file:
                shutil.move(file, paths.txtpath)
            elif ".zip" in file:
                shutil.move(file, paths.zippath)
            elif ".mp4" in file:
                shutil.move(file, paths.videopath)
            elif ".mp3" in file:
                shutil.move(file, paths.audiopath)             
        except FileNotFoundError as e:
            continue
        except shutil.Error as e:
            continue
