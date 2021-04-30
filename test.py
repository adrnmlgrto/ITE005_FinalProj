class Priority:

    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []

            arrival_time = int(
                input(f"Enter Arrival Time for Process {i+1}: "))

            burst_time = int(input(f"Enter Burst Time for Process {i+1}: "))

            priority = int(input(f"Enter Priority for Process {i+1}: "))

            # '0' is the state of the process. 0 means not executed and 1 means execution complete
            temporary.extend(
                [i+1, arrival_time, burst_time, priority, 0, burst_time])

            process_data.append(temporary)
        Priority.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        # Sort processes according to the Arrival Time
        process_data.sort(key=lambda x: x[1])

        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                 process_data[i][5]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][4] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                 process_data[i][5]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[3], reverse=True)
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                # if burst time is zero, it means process is completed
                if process_data[k][2] == 0:
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                normal_queue.sort(key=lambda x: x[1])
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                # if burst time is zero, it means process is completed
                if process_data[k][2] == 0:
                    process_data[k][4] = 1
                    process_data[k].append(e_time)
        t_time = Priority.calculateTurnaroundTime(self, process_data)
        w_time = Priority.calculateWaitingTime(self, process_data)
        Priority.printData(self, process_data, t_time,
                           w_time, sequence_of_process, exit_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            # turnaround_time = completion_time - arrival_time
            turnaround_time = process_data[i][6] - process_data[i][5]

            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        # average_turnaround_time = total_turnaround_time / no_of_processes
        average_turnaround_time = total_turnaround_time / len(process_data)

        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            # waiting_time = turnaround_time - burst_time
            waiting_time = process_data[i][6] - process_data[i][2]

            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        # average_waiting_time = total_waiting_time / no_of_processes
        average_waiting_time = total_waiting_time / len(process_data)

        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, sequence_of_process, exit_time):
        # Sort processes according to the Process ID
        process_data.sort(key=lambda x: x[0])

        print("------------------------------------------------------------------------------------------------------")
        print("Process   ARRIVAL_TIME   BURST_TIME      PRIORITY     COMPLETION_TIME   TURNAROUND_TIME   WAITING_TIME")

        for i in range(len(process_data)):
            print("", process_data[i][0], "\t",                  # P.ID
                  "    ", process_data[i][1], " \t ",          # Arrival Time
                  "   ", process_data[i][5], " \t",            # Burst Time
                  "   ", process_data[i][3], " \t",            # Priority
                  # Completion Time
                  "   ", process_data[i][6], " \t",
                  # Turnaround Time
                  "   ", process_data[i][7], " \t",
                  "   ", process_data[i][8], " \t ", end="               ")  # Waiting Time

        print()
        print()
        print(f'Average Turnaround Time: {average_turnaround_time}')
        print(f'Average Waiting Time: {average_waiting_time}')
        print()

        print("GANTT CHART :")
        for i in range(len(sequence_of_process)*8):
            print("-", end="")
        print("\n|", end="")
        for i in range(len(sequence_of_process)):
            print("  P", sequence_of_process[i], "\t|", end="")
        print()
        for i in range(len(sequence_of_process)*8):
            print("-", end="")
        # Time
        print()
        print(process_data[0][1], "\t", end="")
        for i in range(len(exit_time)):
            print(exit_time[i], "\t", end="")


if __name__ == "__main__":
    no_of_processes = int(input("Enter number of processes: "))
    priority = Priority()
    priority.processData(no_of_processes)
