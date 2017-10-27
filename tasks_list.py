class Tasks:
    tasks = None

    def __init__(self):
        self.tasks = []


     def sort_items(self):
        """ Sorts a todo_items list decreasing by deadline attribute """
        self.tasks.sort(key=lambda task: task.task_day)

    def add_item(self, title, deadline):
        """ Append TodoItem object to todo_items sorted decrasing by deadline
        Raises TypeError if an argument deadline is not an instance of Datetime class."""
        if not isinstance(deadline, datetime.date):
            raise ValueError('Incorrect deadline')

        task = TodoItem(name, description)
        self.tasks.append(task)
        self.sort_items()

    def remove_item(self, index):
        """Removes TodoItem object from index of list todo_items"""
        self.tasks.pop(index)
