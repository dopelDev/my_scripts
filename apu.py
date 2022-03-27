#!/home/dopel/venv/scripts/bin/python3.9

from sys import argv
from os import getcwd, mkdir, chdir, makedirs
from time import ctime

current_path = getcwd()
dirs = ['assetsNscripts', 'code', 'scrappyData', 'cleanData']
sub_dirs_assetsNscripts = [dirs[0] + '/assets', dirs[0] + '/scripts']
files = ['log.md', 'readme.md']
project_name = argv[1]

if __name__ == '__main__':
    mkdir(current_path + '/' + project_name)
    chdir(current_path + '/' + project_name)
    current_path = getcwd()
    for item in dirs:
        mkdir(current_path + '/' + item)
    for item in sub_dirs_assetsNscripts:
        makedirs(current_path + '/' + item)
    for item in files:
        objFile = open(current_path + '/' + item, mode='w')
        objFile.writelines('Name Project : ' + project_name + '\n')
        objFile.writelines('Date : ' + ctime())
        objFile.close()
