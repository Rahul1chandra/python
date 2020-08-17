import threading

def display():
    print (threading.current_thread().getName())
    i = 1

    while i < 11:
        print (i)
        i+=1

print (threading.current_thread().getName())

t_obj  = threading.Thread(target=display)
t_obj.start()

