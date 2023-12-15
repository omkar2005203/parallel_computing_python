import time
from threading import Thread



def do_work():
    print("STARTED")
    #time.sleep(5)
    '''
    CPU bound operaation
    '''
    i=0
    for _ in range(20000000):
        i+=1
    
    print("STOPPED")



for _ in range(5):
    t = Thread(target=do_work,args=())
    t.start()