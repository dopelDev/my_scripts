#!/usr/bin/python3

from os import chdir, system, getcwd
from datetime import date
from time import sleep

path = '/home/dopel/projects/vizcarraVirus'
chdir(path + '/static/data/COVID-19')

system('git pull origin master')

env = '/env/bin'
chdir(path)
print(getcwd())
system('{}{}{} frozen.py'.format(path, env, '/python3'))

# chdir(path)
# system('python frozen.py')

today = date.today()
today = str(today)

system('git checkout master')
system('git add . ')

system('git commit -m "{}"'.format(today))

system('git push origin master')
