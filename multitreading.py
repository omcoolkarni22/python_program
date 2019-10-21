from threading import * #for threading 
from time import sleep #for sleep of cores
class hello(Thread):
    def run(self):
        for i in range (5):
            print("helloo")
            sleep(1) #1==sec



class hi(Thread):
    def run(self):
        for i in range (5):
            print("hii")
            sleep(1)




t1=hello()
t2=hi()

t1.start() #use start instead of run() function
t2.start()

