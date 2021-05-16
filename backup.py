import os
import shutil

source=input("enter the source folder name: ") #folderA
dest=input("enter the destination folder name: ") #folderB
# D:/whitehatclasses/AI and ML/class99/san

source=source+'/'
dest=dest+'/'

listoffiles=os.listdir(source)

for files in listoffiles:
    shutil.copy(source+files, dest)

