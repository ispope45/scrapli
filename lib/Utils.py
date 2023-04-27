# cording = utf-8
import sys
import os
from datetime import *

CURTIME = str(date.today()).replace("-", "")


class Logtools:
    def __init__(self):
        self.start_date = date.today()
        self.base_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    def write_log(self, string, log_name=''):
        dat = str(self.start_date).replace("-", "")

        if log_name == '':
            filename = f'{dat}.log'
        else:
            filename = f'{dat}_{log_name}.log'

        f = open(self.base_path + f'\\{filename}', "a+")

        cur_time = datetime.now().strftime('!%H:%M:%S') + datetime.now().strftime('.%f;')[:4]
        f.write(f'{cur_time};{string}\n')
        f.close()


def print_progress(iteration, total, prefix='', suffix='', decimals=1, barLength=100):
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def chk_dir(filename):
    if os.path.isdir(filename):
        pass
    else:
        os.mkdir(filename)


def export_txt(savePath, filename, contents):
    try:
        chk_dir(savePath)
        with open(f"{savePath}//{CURTIME}_{filename}.txt", "w", encoding="utf8") as f:
            f.write(contents)
    except Exception as e:
        print(e)