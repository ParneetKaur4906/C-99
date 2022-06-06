import os
import shutil
path = input("Enter a name of a directory to be sorted")
list_of_files = os.listdir(path)
for file in list_of_files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exist(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    
