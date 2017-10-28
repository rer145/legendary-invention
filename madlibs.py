import os
import random
import re

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

def get_madlib_text(lib):
    """ (string) -> string

    Preconditions:
        lib is the full path to a text file in the correct madlib format

    Returns the complete text of the madlib file.
    """

    text = ""
    with open(lib, 'r') as f:
        text = f.read()

    return text

def parse_madlib_words(lib):
    """ (string) -> list

    Preconditions:
        lib is the full path to a text file in the correct madlib format

    Parses the madlib and returns a list of the word types needed to
    complete the madlib.
    """

    words = []
    index = 0

    text = get_madlib_text(lib)
    if (len(text) > 0):
        words = re.findall(r'\{{(.+?)\}}', text)

    return words

def generate_story(lib, inputs):
    """ (string, list) -> string

    Preconditions:
        lib is the full path to a text file in the correct madlib format
        inputs is a list with the words to replace in the text

    Returns a string containing the entire text of the madlib with the
    user inputted words instead of placeholders.
    """

    items = iter(str(el) for el in inputs)
    story = ""
    text = get_madlib_text(lib)
    
    if (len(text) > 0):
        #code adapted from: https://stackoverflow.com/questions/13870996/easy-way-to-replace-placeholders-in-string-with-the-list-of-values
        story = re.sub(r'\{{(.+?)\}}', lambda L: next(items), text)
    
    return story
    
