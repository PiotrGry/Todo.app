from Todo import TodoItems

class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


    def add_item(self, name, description):
        quest = TodoItems(name, description)
        self.tasks.append(quest)

    def remove_item(self, id_sign ):

        self.tasks.pop(id_sign)

    def modify_name(self, id_sign):
        for id_sign in self.tasks:
            if id_sign == TodoItems.id_sign:
                self.name = input("What should be a new name of quest: ")
                return self.name
        else:
            print("error")
    def modify_description(self, id_sign):
        for id_sign in self.tasks:
            if id_sign == TodoItems.id_sign:
                TodoItems.description = input("What should be a new description of a quest: ")
                return TodoItems.description

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

    def __str__(self):
        formatted_list = []
        for quest in self.tasks:
            formatted_list.append(str(quest)+"\n")
        return "".join(formatted_list)
