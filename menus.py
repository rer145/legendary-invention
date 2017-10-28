import madlibs
import stats

def show_title():
    """ (none) -> NoneType

    Preconditions: none

    Displays an ASCII art title of the program.
    """

    print('___  ___  ___  ______   _      _____ ______  _____ ')
    print('|  \/  | / _ \ |  _  \ | |    |_   _|| ___ \/  ___|')
    print('| .  . |/ /_\ \| | | | | |      | |  | |_/ /\ `--. ')
    print('| |\\/| ||  _  || | | | | |      | |  | ___ \\ `--. \\')
    print('| |  | || | | || |/ /  | |____ _| |_ | |_/ //\__/ /')
    print('\\_|  |_/\\_| |_/|___/   \\_____/ \\___/ \\____/ \\____/ ')


def main_menu(is_first_time):
    """ (bool) -> NoneType

    Preconditions: none

    Displays a welcome screen the first time program is run,
    and then displays a menu to direct the user.
    """

    if (is_first_time):
        show_title()
        print('\n\nWelcome to MAD Libs! Review the menu below to start playing!')

    choice = ''
    while (choice == ''):
        print('\n\nPlease enter the number of the option you want.')
        print(' 1) Pick your own MAD Lib')
        print(' 2) Let the program pick a MAD Lib')
        print(' 3) Auto-generate a MAD Lib')
        print(' 4) View MAD Lib usage statistics')
        print(' 5) About this program')
        print(' 6) Quit')

        choice = input('Enter your choice: ')
        if (choice == '1'):
            theme_menu()
        elif (choice == '2'):
            pick = madlibs.pick_random_madlib()
            print('Hooray! The program picked:', pick)
            choice = ''
        elif (choice == '3'):
            print('auto-gen')
        elif (choice == '4'):
            stats.display_stats()
            choice = ''
        elif (choice == '5'):
            about_menu()
        elif (choice == '6'):
            break
        else:
            choice == ''


def theme_menu():
    """ (none) -> NoneType

    Preconditions: none

    Displays a list of themes for the user to choose from.
    """

    print('Please enter the number of the theme you want.')
    themes = madlibs.get_madlibs_folders('libs')
    counter = 1

    for theme in themes:
        #
        print( '{0}) {1}'.format(counter, theme[theme.rfind('\\')+1:]))
        counter += 1

    choice = input('Enter your choice: ')
    if (choice in map(str, range(counter))):
        madlib_menu(themes[int(choice)-1])
    else:
        print('You entered an invalid number. Please try again.')
        theme_menu()

def madlib_menu(theme):
    """ (string) -> NoneType

    Precondition: theme must be the name of a folder that exists

    Displays a list of mad libs of a certain theme for the user to choose from.
    """

    print('Excellent choice! You picked', theme[theme.rfind('\\')+1:], 'located at:', theme);
    files = madlibs.get_madlibs_from_folder(theme)
    counter = 1

    if (len(files) > 0):
        for file in files:
            print( '{0}) {1}'.format(counter, file[file.rfind('\\')+1:]))
            counter += 1
    
        choice = input('Enter your choice: ')
        if (choice in map(str, range(counter))):
            print('excellent choice', files[int(choice)-1])
            main_menu(False)
        else:
            print('You entered an invalid number. Please try again.')
            madlib_menu(theme)
    else:
        print('There are no MAD Libs available for that theme!')
        theme_menu()

def about_menu():
    """ (none) -> NoneType

    Preconditions: none

    Displays program information and returns back to the main menu.
    """

    show_title()
    print('\n\nThis program was created by Ron Richardson, during the Fall 2017 semester at Mercyhurst University.')

    main_menu(False)
