from PAGE_FAULT_CONTENT import FIFO
from PAGE_FAULT_CONTENT import LFU
from PAGE_FAULT_CONTENT import MFU
from PAGE_FAULT_CONTENT import OPT
from PAGE_FAULT_CONTENT import LRU
from PAGE_FAULT_CONTENT import MRU

# Input =  7 0 1 2 0 3 0 4 2 3 0 3 0 3 2 1 2 0 1 7 0 1 
# Input = 2 3 3 3 0 1 5 5 2 3 0 1 7 7 0 0 1 2 2 3 5 7 

def execute(x):
    if x == 1:
        FIFO.run()
        return
    elif x == 2:
        OPT.run()
        return
    elif x == 3:
        LRU.run()
        return
    elif x == 4:
        MRU.run()
        return
    elif x == 5:
        LFU.run()
        return
    elif x == 6:
        MFU.run()
        return
    else:
        return -1


print('PAGE FAULT ALGORITHM (BY: JAEL, KIWAG, MANALASTAS, MELEGRITO, POWELL)')
print('[1] FIRST IN FIRST OUT PAGE FAULT ALGORITHM')
print('[2] OPTIMAL PAGE FAULT ALGORITHM')
print('[3] LEAST RECENTLY USED PAGE FAULT ALGORITHM')
print('[4] MOST RECENTLY USED PAGE FAULT ALGORITH')
print('[5] LEAST FREQUENTLY USED PAGE FAULT ALGORITHM')
print('[6] MOST FREQUENTLY USED PAGE FAULT ALGORITH')

u_input = int(input('\nPick an option: '))
execute(u_input)
