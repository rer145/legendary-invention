import os
import random

def get_madlibs_folders(root):
    """ (string) -> list

    Preconditions: root is the name of the root folder of all madlibs folders in the cwd

    Returns a list of all folders that contain madlibs.
    """

    folders = []
    path = os.path.join(os.getcwd(), root)

    if (os.path.isdir(path)):
        for name in os.listdir(path):
            if (os.path.isdir(os.path.join(path, name))):
                folders.append(os.path.join(path, name))

    return folders

def get_madlibs_from_folder(folder):
    """ (string) -> list

    Preconditions: folder must be the name of a folder that exists

    Returns a list of all madlibs from a folder.
    """

    files = []
    
    if (os.path.isdir(folder)):
        for name in os.listdir(folder):
            if (os.path.isfile(os.path.join(folder, name))):
                files.append(os.path.join(folder, name))

    return files

def get_all_madlibs():
    """ (NoneType) -> list

    Preconditions: none

    Returns a lit of all madlibs available from the file system.
    """

    folders = get_madlibs_folders('libs')
    libs = []
    for folder in folders:
        libs += get_madlibs_from_folder(folder)

    return libs

def pick_random_madlib():
    """ (None) -> (string)

    Preconditions: none

    Returns the file path for a random madlib from all the available
    ones in a folder
    """

    libs = get_all_madlibs()
    return random.choice(libs)

def parse_madlib(lib):
    return False
