import datetime
import time

task_count = 0



def add_task(name):
    task_count +=1
    today = time.strftime("%-d/%-m")
    id_sign = str(today)+"/"+ str(task_count)+" "
    
    return id_sign + str(name)


print(add_task("zapalić dom"))
print(add_task("Ugasić dom"))
