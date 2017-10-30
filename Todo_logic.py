import csv
from Todo import Todo


class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


    def add_task(self, name, description):
        quest = Todo(name, description)
        self.tasks.append(quest)

    def remove_task(self, id_sign):
        for quest in self.tasks:
            if id_sign == quest.id_sign:
                self.tasks.remove(quest)

    def modify_name(self, id_sign):
        for quest in self.tasks:
            if id_sign == quest.id_sign:
                quest.name = input("What should be a new name of quest: ")
                return quest.name
        else:
            raise ValueError("Wrong id sign")

    def modify_description(self, id_sign):
        for quest in self.tasks:
            if id_sign == quest.id_sign:
                quest.description = input("What should be a new description of a quest: ")
                return quest.description

    def display_ids(self):
        ids = []
        for quest in self.tasks:
            ids.append(quest.id_sign)
            ids.append("\n")
        return ids

    def display_names(self):
        names = []
        for quest in self.tasks:
            names.append(str(quest.name))
            names.append("\n")
        return names

    def save_data_to_file(self, file_name ="data/task_data.txt"):
        with open(file_name, "w") as import_file:
            for quest in self.tasks:
                import_file.write(str(quest) + "\n")

    def add_task_from_file(self, file_name = "data/task_data.txt"):
        with open(file_name) as import_file:
            file_reader = csv.reader(import_file, delimiter=" ")
            new_tasks_from_file = []
            for item in file_reader:
                new_tasks_from_file.append(item)


            print(new_tasks_from_file)

        name_index = 5
        description_index = 7

        for quest in new_tasks_from_file:
            name = quest[name_index]
            description = quest[description_index]
            self.add_task(name, description)

    def __str__(self):
        formatted_list = []
        for quest in self.tasks:
            formatted_list.append(str(quest)+"\n")
        return "".join(formatted_list)
