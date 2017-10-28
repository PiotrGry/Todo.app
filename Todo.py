import datetime
import time


class Todo:
    name = ""
    description = ""
    task_day = time.strftime("%-d/%-m")
    is_done = False
    names = None
    task_number = 0
    id_sign = str(task_day)+"/" + str(task_number)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.names = []
        self.names.append(Todo.name)
        Todo.task_number +=1
        self.id_sign = str(self.task_day)+"/" + str(Todo.task_number)


    def mark(self):
            self.is_done = True

    def unmark(self):
            self.is_done = False



    def __str__(self):
        is_done_sign = "o "
        if self.is_done:
            is_done_sign = "✓ "
        return is_done_sign + "Id: " + str(self.id_sign) \
                + " | Title: ~~"+ str(self.name) + "~~ |Description: "+ str(self.description)


# task_1 = Todo("Pepik", "umyj dupe")
# print(task_1)
