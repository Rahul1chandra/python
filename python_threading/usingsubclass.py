import threading
class MyThread(threading.Thread):
    def run(self):
        print (threading.current_thread().getName())
        i = 0
        while i <10:
            print (i)
            i+=1

print ("The main programme ::",threading.current_thread().getName())

t = MyThread()
t.start()
