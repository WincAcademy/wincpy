import sys
import this
import time
import math
from datetime import datetime as dt
import greet

__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"


def wait(seconds):
    time.sleep(seconds)


def my_sin(x):
    return math.sin(x)


def iso_now():
    return dt.now().strftime("%Y-%m-%dT%H:%M")


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return greet.supergreeting(name)


if __name__ == "__main__":
    print(wait(1))
    print(my_sin(5))
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("Winc"))
