# coding=UTF-8
import time
import threading
from gold_price import gold_price
from gaoxiao_job import gaoxiao_job


def func():
    t = time.localtime(time.time())
    min, hour, wkday = t.tm_min, t.tm_hour, t.tm_wday

    # print(min, hour, wkday)

    # ------------------------------------------------
    # --------add tasks here--------------------------
    if min == 0:
        if hour in range(8, 23):
            if wkday in range(0, 6):    # Monday is 0
                print(min, hour, wkday)

    if min == 0:
        if hour == 8:
            if wkday in range(0, 6):    # Monday is 0
                print(min, hour, wkday)
                gold_price.send_to_ftqq()
                gaoxiao_job.send_to_ftqq()

    # gaoxiao_job.send_to_ftqq()
    # --------end-------------------------------------
    #-------------------------------------------------
    global timer
    timer = threading.Timer(3, func, [])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(3, func, [])
    timer.start()
