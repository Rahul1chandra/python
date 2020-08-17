 
import threading

class MyThreadClass:
    
    def display(self):
        print (threading.current_thread().getName())
        i = 0
        while i <11:
            print (i)
            i+=1

class_obj = MyThreadClass()
th_obj1 =  threading.Thread(target= class_obj.display)

th_obj2 =  threading.Thread(target= class_obj.display)

th_obj3 =  threading.Thread(target= class_obj.display)



th_obj1.start()
th_obj2.start()
th_obj3.start()
