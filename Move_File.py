import os, shutil

from_dir = "C:/Users/Ishaan Murugesh/Downloads"

choice = str(input("Do you want to move files(y/n)-"))

def moving():
    if choice == 'y':
        location = str(input('Where do you want to transfer files-'))
        shutil.move(from_dir, location)
        print('Transfer Successful')
    else:
        print('Okay')

    undoChoice = input('Do you want to undo the previous action-(y/n)-')
    if undoChoice == 'y':
        shutil.move(location, from_dir)
        print('Transfer Successful')

    else:
        print('Okay')

moving()