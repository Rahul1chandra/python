import threading

class MyThreadClass:
    
    def display(self):
        i = 0
        while i <11:
            print (i)
            i+=1

class_obj = MyThreadClass()
th_obj =  threading.Thread(target= class_obj.display())













