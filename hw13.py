from datetime import datetime
import time


def dec_time_measure(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Час виконання функції {func}: {end - start} секунд")

    return wrapper


@dec_time_measure
def testFunc1():
    print("Виконується функція testFunc1")
    time.sleep(1)
    print("Функція testFunc1 виконана")


@dec_time_measure
def testFunc2():
    print("Виконується функція testFunc2")
    time.sleep(2)
    print("Функція testFunc2 виконана")

testFunc1()
testFunc2()