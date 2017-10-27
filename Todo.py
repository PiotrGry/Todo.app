import datetime
import time


class TodoItems:
    name = ""
    description = ""
    task_day = time.strftime("%-d/%-m")
    is_done = False

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def mark(self):
            self.is_done = True

    def unmark(self):
            self.is_done = False

    # def exporting_data(self,filename = "task_data.txt"):
    #     with open ("task_data.txt","w") as f_name:
    #         tasks = []
    #         for ele in f_name:
    #             tasks.append(ele)


    def add_Todo(self, name, description):
        pass

    def __str__(self):
        is_done_sign = "o"
        if self.is_done:
            is_done_sign = "✓"
        task_number += 1


        return str(task_day)+"/" + str(task_number) + " Id: "+str(id_sign) +" | Title: "+ str(self.name)+" | Description: "+ str(self.description)


task_1 = TodoItems("pepik", "mam do zorobienia kupe")
task_2 = TodoItems("Pieszczoch", "Znajdź se mózg")
print(task_1)
print(task_2)
