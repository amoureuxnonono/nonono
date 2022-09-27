from ws.utils.jacobian import(  
    produce_wallet
)

from ws.caller import(
    QQCaller
)

import argparse

def execute_hack(args):
    ori_file = r'keys\some.txt'
    with open(ori_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            input = line.rstrip('\n')
            wallet_key = input
            caller = QQCaller(wallet_key, 1)
            #caller.transfer('receiver address')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    args = parser.parse_args()
    execute_hack(args)