################################################
#       __                 ______
#  ____/ /___  ____  ___  / / __ \___ _   __
# / __  / __ \/ __ \/ _ \/ / / / / _ \ | / /
#/ /_/ / /_/ / /_/ /  __/ / /_/ /  __/ |/ /
#\__,_/\____/ .___/\___/_/_____/\___/|___/
#          /_/
#
################################################
#Date : Fri 01 Jan 2021 09:03:14 AM -05
#GitHub :  https://github.com/dopelDev
#Facebook : https://www.facebook.com/profile.php?id=100036185774355
#Mail : 322kuroneko2@gmail.com
################################################
from sys import executable
import os

print(executable)

def get_list_scripts(path):
    script_list = []
    if os.path.exists(path):
        script_list = os.listdir(path)

    return script_list

# paths
from_path_python = '/home/dopel/projects/pythonScript'
from_path_bash = '/home/dopel/projects/bashScripts'
destination_path = '/home/dopel/scripts'

# lists
list_python = get_list_scripts(from_path_python)
list_bash = get_list_scripts(from_path_bash)
list_destination  = get_list_scripts(destination_path)
print(list_python)
print(list_bash)
print(list_destination)
