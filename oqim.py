
import httpx
import time
from threading import Thread

#
url = httpx.get('https://jsonplaceholder.typicode.com/photos')
photo = url.json()


#

def task1():
    url = httpx.get('https://jsonplaceholder.typicode.com/photos')
    print('birinchi oqim ishladi')


def task2():
    start2 = time.time()
    url = httpx.get(
        'https://xitmuzon.net/')

    end1 = time.time()
    print('ikkinchi oqim ishladi')
    return int(end1 - start2)


def task3():

    url = httpx.get('https://uznews.uz/')


    print('uchinchi oqim ishladi')


def task4():
    url = httpx.get('https://uzhits.net/')
    print('turtinchi oqim ishladi')

def task5():
    url = httpx.get('https://music.yandex.com/home')
    print('beshinchi oqim ishladi')


task1 = Thread(target=task1)
task2 = Thread(target=task2)
task3 = Thread(target=task3)
task4 = Thread(target=task4)
task5 = Thread(target=task5)
task1.start()
task2.start()
task3.start()
task4.start()
task5.start()

task1.join()
task2.join()
task3.join()
task4.join()
task5.join()
