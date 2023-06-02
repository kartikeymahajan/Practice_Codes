import threading
import time

def cal_square(num):
    print("The square root function is inisialised")
    for n in range(2, num):
        threading.Event().wait(0.3)
        print("square is:", n*n)

def cal_cube(num):
    print("The cube root function is inisialised")
    for n in range(2,num):
        threading.Event().wait(0.3)
        print("cube is:", n**3)

t = time.time()

th1 = threading.Thread(target=cal_square, args=(10,))
th2 = threading.Thread(target=cal_cube, args=(10,))

th1.start()
th2.start()

th1.join()
th2.join()

print("Total time is taking by thread is ", time.time() - t)
print("Again executing the main thread")  
print("Thread 1 and Thread 2 have finished their execution.")  