def start():
    class Process:
        def __init__(self, pID, a_time, b_time):
            self.__pID = pID
            self.__a_time = a_time
            self.__b_time = b_time
            self.__s_time = None
            self.__c_time = None
            self.__w_time = None
            self.__tA_time = None

        # GETTERS AND SETTERS
        def getProcessID(self):
            return self.__pID

        def getArrivalTime(self):
            return self.__a_time

        def getBurstTime(self):
            return self.__b_time

        def getStartingTime(self):
            return self.__s_time

        def getCompletionTime(self):
            return self.__c_time

        def getWaitingTime(self):
            return self.__w_time

        def getTurnaroundTime(self):
            return self.__tA_time

        def setProcessID(self, iD):
            self.__pID = iD
            return

        def setArrivalTime(self, x):
            self.__a_time = x
            return

        def setBurstTime(self, y):
            self.__b_time = y
            return

        def setStartingTime(self, a):
            self.__s_time = a
            return

        def setCompletionTime(self, b):
            self.__c_time = b
            return

        def computeWaitingTime(self):
            self.__w_time = self.__tA_time - self.__b_time
            return

        def computeTurnaroundTime(self):
            self.__tA_time = self.__c_time - self.__a_time
            return


    numOfProcesses = int(input("Enter number of processes: "))
    process_list = [None]*numOfProcesses

    # CREATE OBJECTS WITHIN THE PROCESS LIST
    for i in range(numOfProcesses):
        in_aTime = int(input(f'Process {i+1} arrival time: '))
        in_bTime = int(input(f'Process {i+1} burst time: '))

        process_list[i] = Process(i+1, in_aTime, in_bTime)

    # SORT LIST FOR EASIER TABULATION (BASED ON ARRIVAL TIME)
    for i in range(numOfProcesses-1):
        for j in range(0, numOfProcesses-i-1):
            if process_list[j].getArrivalTime() > process_list[j+1].getArrivalTime():
                process_list[j], process_list[j+1] = process_list[j+1], process_list[j]

    # PROCESSING OF STARTING TIMES AND COMPLETION TIMES FOR EACH PROCESSES
    # SINCE LIST IS SORTED (ARRIVAL TIME), FIRST PROCESS WILL ALWAYS START WITH TIME ZERO (0)
    process_list[0].setStartingTime(0)
    process_list[0].setCompletionTime(
        process_list[0].getStartingTime() + process_list[0].getBurstTime())

    for i in range(1, len(process_list)):
        # CONDITION HANDLE IF THERE WILL BE A CASE OF CPU IDLING
        if process_list[i-1].getCompletionTime() > process_list[i].getArrivalTime():
            process_list[i].setStartingTime(process_list[i-1].getCompletionTime())
        else:
            process_list[i].setStartingTime(process_list[i].getArrivalTime())
            
        process_list[i].setCompletionTime(process_list[i].getStartingTime() + process_list[i].getBurstTime())

    # INVOKE METHODS computeTurnaroundTime() AND computeWaitingTime()
    # SINCE ALL VARIABLES NEEDED ARE PRESENT FOR COMPUTATION
    for i in range(len(process_list)):
        process_list[i].computeTurnaroundTime()
        process_list[i].computeWaitingTime()

    # COMPUTE FOR AVERAGE WAITING TIME (AVE_WT) AND AVERAGE TURNAROUND TIME (AVE_TAT)
    raw_TAT = 0
    raw_WT = 0
    for i in range(len(process_list)):
        raw_TAT += process_list[i].getTurnaroundTime()
        raw_WT += process_list[i].getWaitingTime()

    ave_tat = raw_TAT / len(process_list)
    ave_wt = raw_WT / len(process_list)


    # PRINTING OF EACH PROCESSES
    print("{}  {:^6}  {:^6}  {:^6}  {:^6}  {:^6}  {:^6}".format(
        'P', 'AT', 'BT', 'ST', 'CT', 'WT', 'TAT'))
    for i in range(numOfProcesses):
        print("P{}  {:^5}   {:^5}   {:^5}   {:^5}   {:^5}   {:^5}".format(process_list[i].getProcessID(), process_list[i].getArrivalTime(), process_list[i].getBurstTime(), process_list[i].getStartingTime(), process_list[i].getCompletionTime(), process_list[i].getWaitingTime(), process_list[i].getTurnaroundTime(),
                                                                        ))
    print("===================GANTT CHART======================")

    for k in range(0, len(process_list)):
        print(f"| P{process_list[k].getProcessID()}  \t", end="\t")

    print(" ")

    flag = False
    for i in range(0, len(process_list) + 1):
        if flag == False:
            print(process_list[i].getArrivalTime(), end="\t")
            flag = True

        else:
            print("\t", process_list[i-1].getCompletionTime(), end="\t")

    print("")
        
        
    # PRINTING OF AVERAGES
    print(f"\nAverage Waiting Time: {ave_wt}ms")
    print(f"Average Turnaround Time: {ave_tat}ms")