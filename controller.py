
import add_contact as ac
import user_interface as ui
import view_all_contacts as vac
import export_in_file as eif


def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 5:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 1:
        ac.create_json()
    elif choice_num == 2:
        ac.add_to_json()
    elif choice_num == 3:
        vac.view_all_contacts()
    elif choice_num == 4:
        eif.export_txt()
    elif choice_num == 0:
        print('\nВыход')
        exit()