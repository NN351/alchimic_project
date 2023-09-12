from database.manager import StudentGroupManager
from db import get_session
from os import system

session = get_session()

def clear_terminal():
    system('cls')


def add_new_group():
    name = input('Please enter new name of group: ')
    group_manager = StudentGroupManager(session=session)
    group_manager.insert_group({'name':name})
    clear_terminal()
    print('New group added successfully')


def get_groups():
    manager = StudentGroupManager(session)
    result=manager.get_all_groups()
    print("All groups: ")
    for group in result:
        print(f"{group.id}- {group.name}")

    
def search_group():
    manager = StudentGroupManager(session)
    search_name = input('Enter name to search: ')
    group_list=manager.search_by_group_name(search_name)
    if group_list:
        for group in group_list:
            print(f'{group.id} - {group.name}')
    else:
        print('No group found with this name')
    