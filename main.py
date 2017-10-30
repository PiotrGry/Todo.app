import os
import time
import sys
from Todo import Todo
from Todo_logic import Tasks

def print_ui():
    with open("data/UI_main_menu.txt") as user_ui:
        for line in user_ui:
            print (line)
        print()

def print_display_menu():
    with open("data/Display_menu.txt") as user_ui:
        for line in user_ui:
            print (line)
        print()

def check_len_name_and_description(task_name, task_description):
    name_max_len = 20
    description_max_len = 150

    if len(task_name) > name_max_len  or len(task_description) > description_max_len:
        raise ValueError("Name or description has too many characters  ")

def main():
    daily_dutes = Tasks()
    active = True

    while active:
        os.system('clear')
        print_ui()
        user_pick = input("Select an option: ")

        if user_pick == "1":
            print("""\nNOTE : Name and description of the task must be shorter than,
respectively 20 and 150 characters.""")
            task_name = input("\nEnter a name for a task:" )
            task_description = input("\nEnter a description for a task:" )
            check_len_name_and_description(task_name, task_description)
            daily_dutes.add_task(task_name,task_description)
            os.system('clear')

        if user_pick == "2":
            print(daily_dutes)
            action = input("Do you want to mark or unmark [M/U]? : ")
            if action.upper() == "M":
                picked_task_id = input("Choose a task by id sign as done:" )
                for quest in daily_dutes.tasks:
                    if picked_task_id == quest.id_sign:
                        quest.mark()
                print("\nTask with id {} was changed to done".format(quest.id_sign))
                time.sleep(3)
            elif action.upper() == "U":
                picked_task_id = input("Choose a task by id sign as not done:" )
                for quest in daily_dutes.tasks:
                    if picked_task_id == quest.id_sign:
                        quest.unmark()
                print("\nTask with id {} was changed to not done".format(quest.id_sign))
                time.sleep(3)

        if user_pick == "3":
            print(daily_dutes)
            action = input("Do you want to change name or description [N/D]? : ")
            if action.upper() == "N":
                picked_task_id = input("Choose a task by id sign to change a name: ")
                for quest in daily_dutes.tasks:
                    if picked_task_id == quest.id_sign:
                        daily_dutes.modify_name(picked_task_id)
                print("\nDescription of task with id {} was changed to {}"\
                        .format(quest.id_sign, quest.name))
                time.sleep(3)

            elif action.upper() == "D":
                picked_task_id = input("Choose a task by id sign to change a description: ")
                for quest in daily_dutes.tasks:
                    if picked_task_id == quest.id_sign:
                        daily_dutes.modify_description(picked_task_id)
                print("\nName of task with id {} was changed to {}"\
                        .format(quest.id_sign, quest.description))
                time.sleep(3)

        if user_pick == "4":
            while active:
                print_display_menu()
                action = input("What do you want to see? : ")
                if action == "1":
                    print(daily_dutes)
                elif action == "2":
                    print("\nTask's ids: \n", *daily_dutes.display_ids(), sep="")
                elif action == "3":
                    print("\nTask's names: \n", *daily_dutes.display_names(), sep="")
                elif action == "4":
                    break

        if user_pick == "5":
            print(daily_dutes)
            picked_task_id = input("Choose a task by id sign to delete it: ")
            for quest in daily_dutes.tasks:
                if picked_task_id == quest.id_sign:
                    daily_dutes.remove_task(picked_task_id)
                    print("\nTask with id {} was deleted".format(quest.id_sign))
                    time.sleep(3)


        if user_pick == "6":
            action = input("""do you want to load tasks from another file? If no, tasks
will be loaded from dedault file [Y/N]: """)
            if action.upper() == "N":
                daily_dutes.add_task_from_file()
            elif action.upper() == "Y":
                file_name = input("Type a name of the file: " )
                daily_dutes.add_task_from_file(file_name)


        if user_pick == "7":
            action = input("""do you want to save tasks in new file? If no, tasks
will be saved in dedault file [Y/N]: """)
            if action.upper() == "N":
                daily_dutes.save_data_to_file()
            elif action.upper() == "Y":
                file_name = input("Type a name of the file: " )
                daily_dutes.save_data_to_file(file_name)
            sys.exit()

if __name__ == "__main__":
    main()
