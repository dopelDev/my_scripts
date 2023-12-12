#!/home/dopel/venv/scripts/bin/python3.9

from os import listdir, getcwd, remove, stat
from os.path import exists
from datetime import datetime
from time import ctime

# agregar fechas despues (aun falta)


# declare GLOBAL variables

current_path = getcwd()
list_files = listdir(current_path)

# declare methods

def get_objFile():

    if exists(current_path + '/currentFile.txt'):
        objFile = open(current_path + '/currentFile.txt', mode='+a')
        objFile.writelines('\n')
    else:
        objFile = open(current_path + '/currentFile.txt', mode='+w')
    return objFile 

def add_files(objFile):
    # add files a lista 
    # st_mtime_ns time de modificacion en nanosecs
    for item in list_files:
        lines = []
        if item == 'currentFile.txt':
            continue
        else:
            tmpFile = open(current_path + '/' + item)
            #lines.append(str(stat(current_path + '/' + item).st_mtime_ns))
            #lines.append('\n')
            lines.append(tmpFile.readline()) 
            tmpFile.close()

    # writing lines n' borrando lines en blank  
    # quzias necesite nueva lista split por '\n'
    lines_spliter = []
    for line in lines:
        if line in '\n':
            chunks = line.split('\n')
            for chunk in chunks:
               lines_spliter.append(chunk) 
        else:
            lines_spliter.append(line)
    for line in lines_spliter:
        if line.isspace() or line == '' or line in 'Ultima modificacion :':
            continue
        else:
            objFile.writelines(line)
            objFile.writelines('\n')
    objFile.writelines('Ultima modificacion : {}'.format(ctime()))
    objFile.close()
 
def remove_files():
    if stat(current_path + '/currentFile.txt').st_size != 0:
        for item in list_files:
            if item == 'currentFile.txt':
                continue
            else:
                remove(current_path + '/' + item)

if __name__== '__main__':
   add_files(get_objFile()) 
   remove_files()
