import time
import threading
from gp_alertover import gp_alertover


def func():
    t = time.localtime(time.time())
    min, h, d, mon, wk = t.tm_min, t.tm_hour, t.tm_mday, t.tm_mon, t.tm_wday

    print(min, h, d, mon, wk)

    if h in range(8, 23) and wk in range(0, 6):
        print(min, h, d, mon, wk)
        gp_alertover()

    global timer
    timer = threading.Timer(3600, func, [])
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(5, func, [])
    timer.start()
