import time
import threading
from gp_alertover import gp_alertover


def func():
    t = time.localtime(time.time())
    min, hour, wkday = t.tm_min, t.tm_hour, t.tm_wday

    # print(min, hour, wkday)

    if min == 0:
        if hour in range(8, 23):
            if wkday in range(0, 6):    # Monday is 0
                print(min, hour, wkday)
                gp_alertover()
    global timer
    timer = threading.Timer(60, func, [])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(1, func, [])
    timer.start()
