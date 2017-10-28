import datetime
import time




def add_task(name):
    task_count = 0
    task_count +=1
    today = time.strftime("%-d/%-m")
    id_sign = str(today)+"/"+ str(task_count)+" "

    return id_sign + str(name)

    def task_counter():
        for ele in id_sign:
            return ele


print(add_task("zapalić dom"))
print(add_task("Ugasić dom"))
print(task_counter())
