from Business.logic import get_user_docs, backup_logs, update_footer, get_user_docs_recurs
from os.path import exists, normpath

def display_menu(heading, options):
    try:
        print('-------------------------')
        print(heading.center(25))
        print('-------------------------')
        op_num = 1
        for option in options:
            print(str(option))
            op_num +=1
        
        print()    
        choice = int(input("Enter your choice: "))
        if choice > len(options):
            raise
        print()
        
        return options[choice - 1]
    
    except:
        print('Invalid Input!')
        input('Press Enter to continue..')
        return
    
def main():
    options = {'1. Get submitted documents': menu_get_user_docs, '2. Backup log files': menu_backup_logs, '3. Update template': menu_update_footer}
    options_list = list(options.keys())
    options_list.sort()
    
    heading = 'Main Menu'
    while True:
        choice = display_menu(heading, options_list)
        
        if choice == None:
            continue
        
        options[choice]()
        print()
        
        input('Press Enter to continue..')
        
def menu_get_user_docs():
    try:
        ''' Update the path below'''
        directory = r'C:\Users\kautilya.save\Desktop\EasyCommProject\UserDocs'
        
        
        ''' Handle inconsistencies in path'''
        directory = normpath(directory)
        if not exists(directory):
            print('Invalid Directory Path!')
            return
        
        print()
        file_list = get_user_docs_recurs(directory)
        #file_list = get_user_docs(directory)
        print("Hello3")
        if len(file_list) == 0:
            print('No files found!')
            return
        
        print('The list of submitted user documents: ')
        
        for file_path in file_list:
            print(file_path)    
    except:
        print('Something went wrong!')
    
def menu_backup_logs():
    try:
        ''' Update the path below'''
        directory = r'C:\Users\kautilya.save\Desktop\EasyCommProject\Logs'
        
        ''' Handle inconsistencies in path'''
        directory = normpath(directory)
        
        if not exists(directory):
            print('Invalid Directory Path!')
            return
        size = input('Please enter the min log size in MB: ')
        
        
        size = int(size)
        print()
        
        file_list = backup_logs(directory, size)
        
        if len(file_list) == 0:
            print('No logs found >', size,' MB!')
            return
        
        print('The following logs have been backed up and cleared.')
    
        print('')
        
        for filename in file_list:
            print(filename)
            
    except Exception as e:
        print('Something went wrong!')

def menu_update_footer():
    
    try:
        ''' Update the path below'''
        directory = r'C:\Users\kautilya.save\Desktop\EasyCommProject\ApplicationTemplates'
        
        ''' Handle inconsistencies in path'''
        directory = normpath(directory)
        
        if not exists(directory):
            print('Invalid Directory Path!')
            return
        
        replacement = input('Please enter the updated footer content(eg. Copyright &copy; 2016 ): ')
        replacement = '<footer>' + replacement + '</footer>'
            
        print()
        print('The following templates have been updated:')
        print()
        
        result = update_footer(directory, replacement)
        print()
        
        if result == False:
            raise
        
        for file in result:
            print(file)
        
    except:
        print('Something went wrong!')
        
main()