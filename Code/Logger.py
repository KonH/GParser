import sys
import time


class Log:
    @staticmethod
    def log(msg):
        print(time.strftime("%d/%m/%Y %H:%M:%S") + ":   " + str(msg))

    @staticmethod
    def log_ex(context):
        ex_info = sys.exc_info()
        ex_type = ""
        ex_msg = ""
        if len(ex_info) > 1:
            ex_type = ex_info[0]
            ex_msg = ex_info[1]
        Log.log("Exception (while " + str(context) + "): " + str(ex_type) + " (" + str(ex_msg) + ")")