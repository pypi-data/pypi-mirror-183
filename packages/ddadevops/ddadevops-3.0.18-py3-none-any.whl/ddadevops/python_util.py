from subprocess import check_output, Popen, PIPE
import sys

def execute(cmd, shell=False):
    if sys.version_info.major == 3:
        output = check_output(cmd, encoding='UTF-8', shell=shell)
    else:
        output = check_output(cmd, shell=shell)
    return output.rstrip()

def execute_live(cmd):
    p = Popen(cmd, stdout=PIPE)
    for line in iter(p.stdout.readline, b''):
        print(line.decode('utf-8'), end='')
    p.stdout.close()
    p.wait()

def filter_none(list):
    return [x for x in list if x is not None]
