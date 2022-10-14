#!/home/dopel/venv/gvenv/bin/python3.9

from os import getcwd, listdir, mkdir, remove
from os.path import exists, isdir 
from shutil import copytree, rmtree
from pathlib import Path 
from filecmp import cmpfiles, dircmp


# declaracion de variables
HOME = str(Path.home())
current_path = getcwd()
dirNameList = current_path.split('/')
dirName = dirNameList[-1]
back_up_old = HOME + '/.old/' + dirName
dir_old = current_path + '/.old'
files_2_delete = listdir(current_path) 

def notExistsOld():
    if exists(HOME + '/.old'):
        return True
    else:
        mkdir(HOME + '/.old')
        return True

def getPathAndListDirs():
    list_files = listdir(getcwd())
    return list_files 

def copyDirs(bool, list_files):
    if bool:
        copytree(current_path,back_up_old)
        copytree(current_path,dir_old)
        print('los siguientes archivos se copiaran')
        for items in list_files:
            print(items)

def dirsDiffs():
    # obj comparisoons
    # obj 1 = home old + cwd + old
    # obj 2 = home old + source
    obj_cmp1 = dircmp(back_up_old, dir_old)
    obj_cmp2 = dircmp(back_up_old, current_path)
    print('report : ' )
    print(obj_cmp1.report())
    print('second report : ' )
    print(obj_cmp2.report())

def deleteFiles():
    print('====== los siguientes archivos seran borrados de la fuente ===========')
    for item in files_2_delete:
        print(item)
    opt = input('Y/N\n')
    if opt.upper() == 'Y':
        print('Comenzara el borrado de archivos')
        for item in files_2_delete:
            if isdir(current_path + '/' + item):
                rmtree(current_path + '/' + item)
            else:
                remove(current_path + '/' + item)
    else:
        print('No se borraran los archivos')
            

if __name__ == '__main__':
    copyDirs(notExistsOld(),getPathAndListDirs())
    dirsDiffs()
    deleteFiles()
