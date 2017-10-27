import datetime
import time


class TodoItems:
    name = ""
    description = ""
    task_day = time.strftime("%-d/%-m")
    is_done = True

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def mark(self):
            self.is_done = True

    def unmark(self):
            self.is_done = False



    def __str__(self):
        is_done_sign = "o "
        if self.is_done:
            is_done_sign = "✓ "
        task_number = 0
        id_sign = str(self.task_day)+"/" + str(task_number)
        return  is_done_sign + "Id: " + id_sign + str(self.task_day)+"/" + str(task_number)\
                + " | Title: "+ str(self.name)+" | Description: "+ str(self.description)
