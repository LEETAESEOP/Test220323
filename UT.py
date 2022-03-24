import os



def func1():
    pass

def func2():
    pass



queue = [52, 15, 30]
queue.append(func1)

print(queue)

while True :
    que_len = len(queue)
    if que_len > 0 :
        task = queue.pop(0)
        task()
