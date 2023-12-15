from threading import Thread,Lock
import time

class Bank:
    money = 100
    mutex = Lock()
    def spend(self):
        self.mutex.acquire()
        for i in range(1000000):
            self.money -= 10
        self.mutex.release()

        print("Spending done !")


    def save(self):
        self.mutex.acquire()
        for i in range(1000000):
            self.money += 10
        self.mutex.release()

        print("saving done ")



s1 = Bank()
Thread(target=s1.spend,args=()).start()
Thread(target=s1.save,args=()).start()
time.sleep(5)
print("Balance : ",s1.money)