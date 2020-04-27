from os.path import exists, isdir, normpath
from Persistence.filesystem import get_files, get_dirs, update_file, get_file_size, backup
# ========================================================================================================== #
# Exercise1 : Requirement1                                  
# Write recursive code to get all user documents ========================================================================================================== #


def get_user_docs_recurs(directory): 
    result = []
    #dir_list = []
    
    files  = get_files(directory)
    for filename in files :
        result.append(filename)
    sub_dir  = get_dirs(directory)
    for dirs in sub_dir:
        print(dirs)
        result+=get_user_docs_recurs(dirs)
    
    return result

def get_user_docs(directory):   
    '''  Returns the list of files under UserDocs and its sub- directories'''
    
    result = []
    dir_list = []
    dir_list.append(directory)

    while len(dir_list) >0 :
        current_dir = dir_list.pop()
        
        file_list = get_files(current_dir)
        for filename in file_list :
            result.append(filename)
            
        sub_directory = get_dirs(current_dir)
        dir_list += sub_directory
    
    return result

# ========================================================================================================== #
# Exercise1 : Requirement2  
#Write recursive code to backup the log files                                        
# ========================================================================================================== #
def backup_logs(directory, size_in_MB):
    ''' Take backup using backup(file_path) and return the list of files that were backed up'''
    print("Hello backup_logs")
    print("directory")
    print(directory)
    
    str_num = str(directory)
    
    get_file_size()
    if size_in_MB > 20 :
        print("Greater than size")



# ========================================================================================================== #
# Exercise1 : Requirement3  
#Write recursive code to update footer of all templates                                       
# ========================================================================================================== #
def update_footer(directory, replacement):
    ''' Update footer recursively using update_file(file_path, footer_content) and return the list of files that were updated'''
    pass
