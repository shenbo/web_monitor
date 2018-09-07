# coding=UTF-8

import time
import threading


def func():
    t = time.localtime(time.time())
    min, hour, wkday = t.tm_min, t.tm_hour, t.tm_wday
    # print(min, hour, wkday)

    # --------add tasks here--------------------------
    mm, hh, dd = [33], [13], range(0, 6)            # time
    if min in mm and hour in hh and wkday in dd:
        print(min, hour, wkday)
        # do something
    # --------tasks end----------------------------

    global timer
    timer = threading.Timer(5, func, [])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(1, func, [])
    timer.start()
