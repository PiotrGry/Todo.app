import csv
from Todo import Todo


class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


    def add_item(self, name, description):
        quest = Todo(name, description)
        self.tasks.append(quest)

    def remove_item(self, index):
        index -= 1
        self.tasks.pop(index)

    def modify_name(self, id_sign):
        for quest in self.tasks:
            if id_sign == quest.id_sign:
                quest.name = input("What should be a new name of quest: ")
                return quest.name
        else:
            print("error")

    def modify_description(self, id_sign):
        for quest in self.tasks:
            if id_sign == quest.id_sign:
                quest.description = input("What should be a new description of a quest: ")
                return quest.description

    def display_ids(self):
        ids = []
        for quest in self.tasks:
            ids.append(quest.id_sign)
        return ids

    def display_task_names(self):
        names = []
        for quest in self.tasks:
            names.append(quest.name)
        return names

    def save_data_to_file(self, file_name):
        with open(file_name, "w", newline="") as import_file:
            file_writer = csv.writer(import_file, delimiter=" ")
            for quest in self.tasks:
            # file_writer.writerow(self.tasks)

                file_writer.writerow(str(quest))




    def add_items_from_file(self, file_name):
            with open(file_name) as import_file:
                file_reader = csv.reader(import_file, delimiter="|")
                tasks = []
                for item in file_reader:
                    tasks.append(item)

            
    def __str__(self):
        formatted_list = []
        index = 1
        for quest in self.tasks:
            formatted_list.append(str(index) + ". " + str(quest)+"\n")
            index += 1
        return "".join(formatted_list)
