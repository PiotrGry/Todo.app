from Todo import TodoItems

class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


    def add_item(self, name, description):
        quest = TodoItems(name, description)
        self.tasks.append(quest)

    def remove_item(self, index):

        self.tasks.pop(index)

    def get_item(self, index):
        """Returns TodoItem object from index of list todo_items.
        Raises IndexError if an argument index is out of range list todo_items."""
        if index <= len(self.todo_items):
            return self.todo_items[index]
        else:
            raise IndexError("Argument index is out of range list todo_items")

    def modify_name(self, id_sign):
        for id_sign in self.tasks:
            if id_sign == self.id_sign:
                self.name = input("What should be a new name of quest: ")
                return self.name

    def modify_description(self, id_sign):
        for id_sign in self.tasks:
            if id_sign :
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
        """Returns a formatted list of todo_items sorted decrasing by deadline."""
        formatted_list = []
        for quest in self.tasks:
            formatted_list.append(str(quest)+"\n")
        return "".join(formatted_list)
