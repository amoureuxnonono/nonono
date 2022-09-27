from ws import (
    BatchForceScan
)

import argparse

def execute_pow_scan(fscan, args):
     fscan.pow_scan(args.pow, args.max)

def execute_step_scan(fscan, args):
    fscan.step_scan(int(args.start, args.dp), args.step, args.max)

def execute_revolving_scan(fscan, args):
    fscan.revolving_scan(args.start)

def execute_birthday_scan(fscan, args):
    fscan.birthday_scan(args.prefix, args.suffix, args.max)

def execute_xyloop_scan(fscan, args):
    fscan.xyloop_scan(int(args.start, args.dp), args.xy, args.max)

def execute_multiply_scan(fscan, args):
    fscan.multiply_scan(int(args.start, args.dp), args.max)

def execute_double_scan(fscan, args):
    fscan.double_scan(int(args.start, args.dp), args.max)

def execute_file_scan(fscan, args):
    fscan.file_scan(args.filepath)

def execute_rbirthday_scan(fscan, args):
    fscan.rbirthday_scan(args.max)

def execute(args):
    fscan = BatchForceScan(args.net, args.loopmax)

    if(args.scantype == 1):
        execute_pow_scan(fscan, args)

    elif(args.scantype == 2):
        execute_step_scan(fscan, args)

    elif(args.scantype == 3):
        execute_revolving_scan(fscan, args)

    elif(args.scantype == 4):
        execute_birthday_scan(fscan, args)

    elif(args.scantype == 5):
        execute_xyloop_scan(fscan, args)

    elif(args.scantype == 6):
        execute_multiply_scan(fscan, args)

    elif(args.scantype == 7):
        execute_double_scan(fscan, args)

    elif(args.scantype == 8):
        execute_file_scan(fscan, args)

    elif(args.scantype == 9):
        execute_rbirthday_scan(fscan, args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-d', dest='dp', default=16, type=int, help='decimal base')
    parser.add_argument('-xy', dest='xy', default=0, type=int, help='x or y only work on xyloop scan')
    parser.add_argument('-bp', dest='prefix', default='', help='prefix only work on birthday scan')
    parser.add_argument('-bs', dest='suffix', default='', help='suffix only work on birthday scan')
    parser.add_argument('-s', dest='start', help='start')
    parser.add_argument('-f', dest='filepath', help='file path')
    parser.add_argument('-t', dest='step',  default=1, type=int, help='scan step')
    parser.add_argument('-p', dest='pow', type=int, help='pow base, only work on pow scan')
    parser.add_argument('-m', dest='max', default=200, type=int, help='scan count')
    parser.add_argument('-lm', dest='loopmax', default=50, type=int, help='loop max')
    parser.add_argument('-n', dest='net', default=1, type=int, help='network')
    parser.add_argument('-k', dest='scantype', default=1, type=int, help='''scan type, 
  1 = pow(-p,-m) 
  2 = step(-s, -t, -m) 
  3 = revolving(-s) 
  4 = birthday(-bp,-bs,-m) 
  5 = xyloop(-s, -xy, -m)
  6 = multiply(-s, -m)
  7 = double(-s, -m)
  8 = file(-f)
  9 = repeat birthday(-m) ''')
    args = parser.parse_args()
    execute(args)
   
 
 