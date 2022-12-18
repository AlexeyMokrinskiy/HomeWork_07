import chek
from export_in_file import export_txt


def start():
    greetings = 'Привет!'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '1. Создать новую книгу или очистить существующую'
    new_contact = '2. Добавить новый контакт'
    view_all_contact = '3. Показать все контакты'
    export_to_file = '4. Экспорт'
    to_exit = '0. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{view_all_contact}\n{export_to_file}\n{to_exit}')
    return chek.digit_check()