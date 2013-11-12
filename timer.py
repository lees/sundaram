import time


class Timer():
    starttime = 0

    @staticmethod
    def start():
        Timer.starttime = time.time()

    @staticmethod
    def end():
        endtime = time.time()

        if Timer.starttime == 0:
            print "You forget to start a timer"
            return

        print "Elapsed time: {0:.4f} sec".format(endtime - Timer.starttime)
        Timer.starttime = 0