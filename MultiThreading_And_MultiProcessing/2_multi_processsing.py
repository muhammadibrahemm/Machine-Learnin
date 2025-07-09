import multiprocessing
import multiprocessing.process
import time

def square():
    for i in range(5):
        time.sleep(2)
        print(f"square of a number is:{i*i}")

def cube():
    for i in range(5):
        time.sleep(2)
        print(f"cube of a number is:{i*i*i}")

p1=multiprocessing.Process(target=cube)
p2=multiprocessing.Process(target=square)

p1.start()
p2.start()

p1.join()
p2.join()
