# -*- coding: UTF-8 -*-
from threading import Timer
import time
import order
def run():
    order123()
    Timer(600, run).start()
run()