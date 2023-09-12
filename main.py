from sys import argv 

from migrate import create_tables
from utils import (
    add_new_group,
    clear_terminal,
    get_groups,
    search_group  
)


if __name__ == "__main__":
    arguments = argv
    print(arguments)
    if arguments[1] == "migrate":
        create_tables()
    elif arguments[1] == 'add_group':
        clear_terminal()
        add_new_group()
    elif arguments[1] == 'get_groups':
        clear_terminal()
        get_groups()
    elif arguments[1] == 'search_group':
        clear_terminal()
        search_group()