from ALGO_CONTENT import FCFS
from ALGO_CONTENT import SSTF
from ALGO_CONTENT import SCAN
from ALGO_CONTENT import CSCAN
from ALGO_CONTENT import LOOK
from ALGO_CONTENT import CLOOK


def execute(x):
    if x == 1:
        FCFS.run()
        return
    elif x == 2:
        SSTF.run()
        return
    elif x == 3:
        SCAN.run()
        return
    elif x == 4:
        CSCAN.run()
        return
    elif x == 5:
        LOOK.run()
        return
    elif x == 6:
        CLOOK.run()
        return
    else:
        return -1


print('DISK SCHEDULING ALGORITHM (BY: JAEL, KIWAG, MANALASTAS, MELEGRITO, POWELL)')
print('[1] First-Come-First-Serve Disk Scheduling Algorithm (FCFS)')
print('[2] Shortest Seek-Time First Disk Scheduling Algorithm (SSTF)')
print('[3] Elevator/SCAN Disk Scheduling Algorithm (SCAN)')
print('[4] Circular-SCAN Disk Scheduling Algorithm (CSCAN)')
print('[5] LOOK Disk Scheduling Algorithm (LOOK)')
print('[6] Circular-LOOK Disk Scheduling Algorithm (CLOOK)')

u_input = int(input('\nPick an option: '))
execute(u_input)
