import os
import shutil

path=input("enter the name of the directory to be sorted: ")
# D:/whitehatclasses/AI and ML/class99/san

listoffiles=os.listdir(path)

for files in listoffiles:
    name, ext=os.path.splitext(files)

    print(name)
    print(ext)

    print(files)

    ext=ext[1:]

    if ext=='':
        continue

    if os.path.exists(path+'/'+ext):
        d=shutil.move(path+'/'+files, path+'/'+ext+'/'+files)
        print(d)
    else:
        os.makedirs(path+'/'+ext)
        d=shutil.move(path+'/'+files,path+'/'+ext+'/'+files )
        print(d)




