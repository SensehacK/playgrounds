from os import listdir, remove
from os.path import isdir, isfile, join, getsize, join, normpath
import re


def update_file(file_path, replacement):
    ''' Opens a file and updates the footer content given with the replacement provided'''
    pattern = r'<footer>.*</footer>' 
    with open(file_path, 'r+') as f:
        html = f.read()
        html = re.sub(pattern, replacement, html)
        f.seek(0)
        f.write(html)
        f.truncate()
    
def get_files(directory):
    ''' Returns a list of all the file contained in the given directory path'''
    file_list = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f))]
    return file_list

def get_dirs(directory):
    ''' Returns a list of all the sub-directories present in the given directory path'''
    dir_list = [join(directory, f) for f in listdir(directory) if isdir(join(directory, f))]
    return dir_list

def get_file_size(file_path):
    ''' Returns the size of the given file in MB''' 
    return getsize(file_path) / 10 ** 6

def backup(file_path):
    ''' Moves the file to the ./EasyCommProject/Logs/BackupLogs folder and deletes'''
    
    data = ''
    
    ''' Update the path below'''
    backup_path = r'C:\Users\kautilya.save\Desktop\EasyCommProject\BackupLogs'
    backup_path = normpath(backup_path)
    
    with open(file_path, 'r+') as f:
        data = f.read()
    
    file_name = file_path.split('\\')[-1]
    
    file_name = join(backup_path, file_name)
    
    with open(file_name, 'w') as f:
        f.write(data)
        
    remove(file_path)
        
