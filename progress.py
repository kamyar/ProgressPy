
##########################################################
######                  ProgressPy                  ######
######  By Kamyar Ghasemlou k.ghasemlou@gmail.com   ######
##########################################################


import time
import sys
import itertools

class Progress:
    def __init__(self, total=100, title='Progress Bar'):
        self._total = total
        self._title = title
        self._spinner = itertools.cycle("|/-\\")
        self._baseTime = None
        return

    def update(self, count=0, suffix=''):
        if not self._baseTime:
            self._baseTime = time.time()
        bar_len = 60
        filled_len = int(round(bar_len * count / float(self._total)))

        percents = round(100.0 * count / float(self._total), 1)
        bar = '=' * (filled_len-1) + ">" + '-' * (bar_len - max(1, filled_len))

        print("\033c")
        sys.stdout.write("%s\n" % self._title)
        sys.stdout.flush()
        sys.stdout.write("({0}) [{1}] {2:}%\t{3}\n".format(self._spinner.next(), bar, percents,  suffix))
        sys.stdout.flush()
        sys.stdout.write("{0} since execution".format( time.strftime("%H:%M:%S", time.localtime(time.time() - self._baseTime + time.timezone))))
        sys.stdout.flush()