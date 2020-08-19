import threading 
import time
class BookTicket:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.l = threading.Lock()
        #self.l = threading.Seamphore()

    def processbooking(self, requestedSeats):
        print (threading.current_thread().getName())
        time.sleep(1)
        self.l.acquire()
        if self.total_seats+1 > requestedSeats:
            print ("booking ticket")
            print ("confirming the seats")
            print ("print the ticket")
            self.total_seats-= requestedSeats
        else:
            print ("Sorry ! requested seats are not avaialble")
            
        
        print (self.total_seats)
        self.l.release()

bt=  BookTicket(total_seats= 10)
t1 = threading.Thread(target=bt.processbooking, args=(3,))
t2 = threading.Thread(target=bt.processbooking, args=(5,))
t3 = threading.Thread(target=bt.processbooking, args=(2,))
t4 = threading.Thread(target=bt.processbooking, args=(2,))

t1.start()
t2.start()
t3.start()
t4.start()




