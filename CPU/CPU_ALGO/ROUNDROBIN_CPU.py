class RoundRobin:
    def processData(self, no_of_processor):
        process_list = []
        for i in range(no_of_processor):
            temporary = []
            print("--------------------------------")
            process_id = int(input(" Process ID: "))
            time_of_arrival = int(input(f" P{process_id} Arrival Time: "))
            time_of_burst = int(input(f" P{process_id} Burst Time: "))
            # [0] means not executed and [1] means execution complete: current state of the process
            temporary.extend([process_id, time_of_arrival, time_of_burst, 0, time_of_burst]) 
            process_list.append(temporary)
        print("--------------------------------")
        quantum = int(input(" Quantum Time: "))
        print("--------------------------------\n")
        RoundRobin.schedulingProcess(self, process_list, quantum)

    def schedulingProcess(self, process_list, quantum):
        time_of_start = []         # Start time of Processes.
        time_of_exit = []          # Exit time of Processes.
        proc_executed = []   # Executed Processes, can be used for Gantt Chart.
        process_arrived = []        # processes that already arrived
        s_time = 0              # current Start time
        process_list.sort(key=lambda x: x[1]) # Sort processes according to the Arrival Time

        while 1:
            process_normal = []   # processes that doesnt arrive yet.
            temp = []

            for i in range(len(process_list)):
                if process_list[i][1] <= s_time and process_list[i][3] == 0:
                    present = 0
                    # Checks if the next process is not part of the Ready Queue
                    if len(process_arrived) != 0:
                        for k in range(len(process_arrived)):
                            if process_list[i][0] == process_arrived[k][0]:
                                present = 1
                    #  Adds process in the Ready Queue only if it is not already present in it
                    if present == 0:
                        temp.extend([process_list[i][0], process_list[i][1], process_list[i][2], process_list[i][4]])
                        process_arrived.append(temp)
                        temp = []
                    # Appends the recently executed process at the end of Ready Queue
                    if len(process_arrived) != 0 and len(proc_executed) != 0:
                        for k in range(len(process_arrived)):
                            if process_arrived[k][0] == proc_executed[len(proc_executed) - 1]:
                                process_arrived.insert((len(process_arrived) - 1), process_arrived.pop(k))
                elif process_list[i][3] == 0:
                    temp.extend([process_list[i][0], process_list[i][1], process_list[i][2], process_list[i][4]])
                    process_normal.append(temp)
                    temp = []

            if len(process_arrived) == 0 and len(process_normal) == 0:
                break

            if len(process_arrived) != 0:
                # If process's Remaining Burst Time is > that the Quantum Time, 
                # it executes until the end of quantum time then switch
                if process_arrived[0][2] > quantum:
                    time_of_start.append(s_time)
                    s_time = s_time + quantum
                    e_time = s_time
                    time_of_exit.append(e_time)
                    proc_executed.append(process_arrived[0][0])
                    for j in range(len(process_list)):
                        if process_list[j][0] == process_arrived[0][0]:
                            break
                    process_list[j][2] = process_list[j][2] - quantum
                    process_arrived.pop(0)
                # If process's Remaining Burst Time is <= the Quantum Time, the execution will be completed
                elif process_arrived[0][2] <= quantum:
                    time_of_start.append(s_time)
                    s_time = s_time + process_arrived[0][2]
                    e_time = s_time
                    time_of_exit.append(e_time)
                    proc_executed.append(process_arrived[0][0])
                    for j in range(len(process_list)):
                        if process_list[j][0] == process_arrived[0][0]:
                            break
                    process_list[j][2] = 0
                    process_list[j][3] = 1
                    process_list[j].append(e_time)
                    process_arrived.pop(0)

            elif len(process_arrived) == 0:
                if s_time < process_normal[0][1]:
                    s_time = process_normal[0][1]
                # If process's Remaining Burst Time is > that the Quantum Time, 
                # it executes until the end of quantum time then switch 
                if process_normal[0][2] > quantum:
                    time_of_start.append(s_time)
                    s_time = s_time + quantum
                    e_time = s_time
                    time_of_exit.append(e_time)
                    proc_executed.append(process_normal[0][0])
                    for j in range(len(process_list)):
                        if process_list[j][0] == process_normal[0][0]:
                            break
                    process_list[j][2] = process_list[j][2] - quantum
                # If process's Remaining Burst Time is <= the Quantum Time, the execution will be completed
                elif process_normal[0][2] <= quantum:
                    time_of_start.append(s_time)
                    s_time = s_time + process_normal[0][2]
                    e_time = s_time
                    time_of_exit.append(e_time)
                    proc_executed.append(process_normal[0][0])
                    for j in range(len(process_list)):
                        if process_list[j][0] == process_normal[0][0]:
                            break
                    process_list[j][2] = 0
                    process_list[j][3] = 1
                    process_list[j].append(e_time)

        t_time = RoundRobin.calculateTurnaroundTime(self, process_list)
        w_time = RoundRobin.calculateWaitingTime(self, process_list)
        RoundRobin.printData(self, process_list, t_time, w_time, proc_executed, time_of_exit)

    # Calculate Turn Around Time
    def calculateTurnaroundTime(self, process_list):
        total_TAT = 0
        for i in range(len(process_list)):
            # turnaround_time = completion_time - time_of_arrival
            turnaround_time = process_list[i][5] - process_list[i][1]       
            total_TAT = total_TAT + turnaround_time
            process_list[i].append(turnaround_time)
        # ave_TAT = total_TAT / no_of_processor    
        ave_TAT = total_TAT / len(process_list) 
        return ave_TAT

    # Calculate Waiting Time
    def calculateWaitingTime(self, process_list):
        total_WT = 0
        for i in range(len(process_list)):
            # waiting_time = turnaround_time - time_of_burst
            waiting_time = process_list[i][6] - process_list[i][4]      
            total_WT = total_WT + waiting_time
            process_list[i].append(waiting_time)
        # ave_WT = total_WT / no_of_processor   
        ave_WT = total_WT / len(process_list)   
        return ave_WT

    # Display Round Robin Proccesses Data
    def printData(self, process_list, ave_TAT, ave_WT, proc_executed, time_of_exit):
        process_list.sort(key=lambda x: x[0]) # Process Sorted according to the ID
        print(" ------- --------------- --------------- ----------------- ----------------- --------------")
        print("| P.ID  |  Arrival Time |   Burst Time  | Completion Time | Turnaround Time | Waiting Time |")
        print(" ------- --------------- --------------- ----------------- ----------------- --------------")
        for i in range(len(process_list)):
            print("| P", process_list[i][0], "\t|",                 # P.ID
                    "    ", process_list[i][1], " \t| ",            # Arrival Time
                    "   ", process_list[i][4], " \t|",              # Burst Time
                    "     ", process_list[i][5], " \t  |",          # Completion Time
                    "      ", process_list[i][6], " \t    |",       # Turnaround Time
                    "   ", process_list[i][7], " \t   | ", end="")  # Waiting Time 
            print()
        print("-------------------------------------------------------------------------------------------")
        
        print("\n ------------------------------------- GANTT CHART -----------------------------------------")
        # Process
        for i in range(len(proc_executed)*8):
            print("-", end="")
        print("\n|"  , end="")
        for i in range(len(proc_executed)):
            print("  P", proc_executed[i], "\t|", end="")
        print()
        for i in range(len(proc_executed)*8):
            print("-", end="")
        # Time
        print()
        print(process_list[0][1], "\t", end="")
        for i in range(len(time_of_exit)):
            print(time_of_exit[i],"\t", end="")
        print(" ")
        print(f'\n Average Waiting Time:  {ave_WT}')
        print(f' Average Turnaround Time:  {ave_TAT}')

# Execute Program
def start():
    no_of_processor = int(input("Enter number of processes: "))
    rr = RoundRobin()
    rr.processData(no_of_processor)
