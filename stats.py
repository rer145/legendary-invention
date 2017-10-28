import os

def display_stats():
    """ () -> NoneType

    Preconditions: none

    Displays statistics of the common words and madlibs used.
    """
    
    root = os.path.join(os.getcwd(), 'stats')

    lib_counts = {}
    with open(os.path.join(root, 'libs.txt'), 'r') as lfile:
        for line in lfile:
            line = line.strip()
            if line in lib_counts:
                lib_counts[line] += 1
            else:
                lib_counts[line] = 1
    
    print('\n\nBelow are the top 3 most used MAD Libs:')
    #sorted_lib_counts = sorted(invert_dictionary(lib_counts))
    sorted_lib_counts = sorted(lib_counts, key=lib_counts.get, reverse=True)
    counter = 1
    for x in sorted_lib_counts:
        if counter < 4:
            path_parts = x.split('\\')
            file = path_parts[len(path_parts)-1]
            theme = path_parts[len(path_parts)-2]
            print(' {0} time(s): {1} -> {2}'.format(lib_counts[x], theme, file))
            counter += 1


    types = set()
    words = {} #string:list
    with open(os.path.join(root, 'words.txt'), 'r') as wfile:
        for line in wfile:
            line = line.strip()
            if len(line) > 0:
                parts = line.split(':')
                types.add(parts[0])
                if parts[0] in words:
                    words[parts[0]].append(parts[1])
                else:
                    words[parts[0]] = []
                    words[parts[0]].append(parts[1])

    print('\n\nBelow are the top 5 most used words of each type:\n')
    for t in types:
        print(t.center(30))
        print('-'*30)

        temp = [words[t].count(w) for w in words[t]]
        freq = dict(list(zip(words[t], temp)))
        sorted_freq = [(freq[key], key) for key in freq]
        sorted_freq.sort()
        sorted_freq.reverse()

        counter = 1
        for x in sorted_freq:
            if counter < 4:
                print(' {0} {1}'.format(x[0], x[1]))
                #print(str(x))
                counter += 1

        print('\n\n')
    
def invert_dictionary(dictionary):
    """ (dictionary) -> dictionary

    Preconditions: none

    Returns a dictionary with the keys and values inverted.
    """

    inverted = {}
    for key, value in dictionary.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = key

    return inverted

def log_stats(lib, types, inputs):
    """ (string, list, list) -> NoneType

    Preconditions:
        lib must be the full path to a madlib text file
        len(types) == len(inputs)

    Logs the word type and input to the stats folder, as well as logging
    the amount of times a madlib has been used.
    """

    root = os.path.join(os.getcwd(), 'stats')

    if len(types) == len(inputs):
        with open(os.path.join(root, 'words.txt'), 'a') as wfile:
            for i in list(range(len(types))):
                wfile.write('{0}:{1}\n'.format(types[i], inputs[i]))

    with open(os.path.join(root, 'libs.txt'), 'a') as lfile:
        lfile.write(lib + '\n')
