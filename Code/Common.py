import time
import random
from Logger import Log

class Common:
    @staticmethod
    def Wait():
        MIN = 1
        MAX = 3
        sec = random.randint(MIN, MAX)
        Log.log("Wait for " + str(sec) + " secs.")
        time.sleep(sec)