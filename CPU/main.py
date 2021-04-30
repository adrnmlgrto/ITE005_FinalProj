from CPU_ALGO import FCFS_CPU
from CPU_ALGO import SJF_CPU
from CPU_ALGO import PRIORITY_CPU
from CPU_ALGO import ROUNDROBIN_CPU

def start():
    print(" ")
    print("------------------------")
    print("CPU SCHEDULING ALGORITHM")
    print("------------------------")
    print(" ")
    print("[1] First Come First Serve (FCFS)")
    print("[2] Shortest Job First (SJF)")
    print("[3] Priority Queue")
    print("[4] Round Robin")
    print("[5] Exit")

    print(" ")
    choice = input("Enter choice: ")
    choices(choice)


def choices(choice):
        if choice == "1":
            print(" ")
            print(" ------------------------")
            print("| FIRST COME FIRST SERVE |")
            print(" ------------------------")
            FCFS_CPU.start()
            start()
        
        elif choice == "2":
            print(" ")
            print(" ---------------------------------")
            print("| SHORTEST JOB FIRST (PRE-EMPTIVE)|")
            print(" ---------------------------------")
            SJF_CPU.start()
            start()
        
        elif choice == "3":
            print(" ")
            print(" --------------------------")
            print("| PRIORITY (NON-PREEMPTIVE)|")
            print(" --------------------------")
            PRIORITY_CPU.start()
            start()

        elif choice == "4":
            print(" ")
            print(" ------------")
            print("| ROUND ROBIN |")
            print(" ------------")
            ROUNDROBIN_CPU.start()
            start()
        
        elif choice == "5":
            import sys
            sys.exit("Program terminated.")

        else:
            print("Invalid input.")

start()