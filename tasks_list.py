class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


    def sort_items(self):
        """ Sorts a todo_items list decreasing by deadline attribute """
        self.tasks.sort(key=lambda task: tasks.task_day)

    def add_item(self, title, description):
        """ Append TodoItem object to todo_items sorted decrasing by deadline
        Raises TypeError if an argument deadline is not an instance of Datetime class."""

        task = TodoItem(name, description)
        self.tasks.append(task)
        self.sort_items()

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
        for id_sign in tasks:
            if id_sign:
                self.name = input("What should be a new name of task: ")
        return self.name



    def modify_description(self, id_sign):
        for id_sign in tasks:
            if id_sign:
                self.description = input("What should be a new description of a task: ")
        return self.description

    def display_ids(self):
        id_sign_index = 2
        for quest in tasks:
            return quest[id_sign_index]

    def display_task_name(self):
        task_neme_index = 4
        for quest in tasks:
            return quest[task_neme_index]
