from ALGO_CONTENT import FCFS
from ALGO_CONTENT import SSTF
from ALGO_CONTENT import SCAN
from ALGO_CONTENT import CSCAN
from ALGO_CONTENT import LOOK
from ALGO_CONTENT import CLOOK

def display():
    print('DISK SCHEDULING ALGORITHM (BY: JAEL, KIWAG, MANALASTAS, MELEGRITO, POWELL)')
    print('[1] First-Come-First-Serve Disk Scheduling Algorithm (FCFS)')
    print('[2] Shortest Seek-Time First Disk Scheduling Algorithm (SSTF)')
    print('[3] Elevator/SCAN Disk Scheduling Algorithm (SCAN)')
    print('[4] Circular-SCAN Disk Scheduling Algorithm (CSCAN)')
    print('[5] LOOK Disk Scheduling Algorithm (LOOK)')
    print('[6] Circular-LOOK Disk Scheduling Algorithm (CLOOK)')
    print('[7] Exit')

def execute():
    x = 0
    while (x != 7):
        display()
        x = int(input('\nPick an option: '))
        if x == 1:
            FCFS.run()
      
        elif x == 2:
            SSTF.run()
    
        elif x == 3:
            SCAN.run()
     
        elif x == 4:
            CSCAN.run()
      
        elif x == 5:
            LOOK.run()
        
        elif x == 6:
            CLOOK.run()
      
        elif x == 7:
            return
        else:
            print("Invalid input")
    return



execute()
