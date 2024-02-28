import datetime
import traceback
import sys
import os


def divide(x, y):
    try:
        return x / y        
    except Exception as err:
        print('Hata oluştu')
        create_log(err)

def create_log(err):
    cwd = os.getcwd()
    logs_dirs = f'{cwd}/logs/'
    if not os.path.isdir(logs_dirs):
        os.mkdir(f'{cwd}/logs/')
    with open(f'{logs_dirs}log.txt', 'a') as file:
        file.write(f'{traceback.format_exc()} {sys.exc_info()} {datetime.datetime.now()}\n')

divide(3,0)
