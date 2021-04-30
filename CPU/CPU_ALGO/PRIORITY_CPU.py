# for waiting time calculation
def waitingTime(processes, n, wt):
    wt[0] = 0
 
    for i in range(1, n):
        wt[i] = processes[i - 1][1] + wt[i - 1]
 
# for turn around time
def turnAroundTime(processes, n, wt, tat):
     
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
 
# for calculating waiting and turn around times, and displaying details 
def calcTime(processes, n):

    # list for wt and tat
    wt = [0] * n
    tat = [0] * n
 
    # for waiting time
    waitingTime(processes, n, wt)
 
    # for turnaround time
    turnAroundTime(processes, n, wt, tat)
 
    # display the details
    print("\nProcesses    Burst Time    Priority    Waiting",
          "Time    Turn-Around Time")
    wait_total = 0
    turnAround_total = 0
    for i in range(n):
 
        wait_total = wait_total + wt[i]
        turnAround_total = turnAround_total + tat[i]
        print(" ", processes[i][0], "\t\t",
                   processes[i][1], "\t\t",
                   processes[i][2], "\t\t",
                   wt[i], "\t\t", tat[i])

    # for the gantt chart
    bt = []
    bt.insert(0,0)
    for j in range(1, n+1):
        bt.insert(j, processes[j-1][1] + bt[j-1])
 
    print("------------------------------GANTT CHART-------------------------------")

    #for displaying the processes
    print(" ")
    for k in range(0, len(processes)):
        print(f"| P{processes[k][0]}  \t", end="\t")

    # for displaying waiting time and gantt chart
    print("")
    for i in range(len(processes) + 1):
            print(bt[i], end="\t \t")

    print(" ")
    print("\nAverage waiting time = ",(wait_total /n))
    print("Average turn around time = ", turnAround_total / n)
 
def prioScheduling(proc, n):
     
    # sort processes according to priority
    proc = sorted(proc, key = lambda proc:proc[2],)
                                   #reverse = True);
 
    # call calcTime to calculate the waiting and turn around time
    calcTime(proc, n)
     

def start():
    # get the input for num of processes
    n_proc = int(input("Enter number of processes: "))
    print(" ")

    #get inputs for process IDs, burst times and priorities and put it in a list
    proc_list = []
    for i in range (n_proc):
        temp = []
        proc_ID = int(input("Enter process ID: "))
        burst_time = int(input(f"Enter burst time for P{i+1}: "))
        priority = int(input(f"Enter priority for P{i+1}: "))
        print("------------------------------------------------------------------------")

        temp.extend([proc_ID, burst_time, priority])
        proc_list.append(temp)
    
    #call prioScheduling function
    prioScheduling(proc_list, n_proc)
