from queue import Queue

def start():
    class Processor:
        # Private members assigned with "__"
        # identification_number
        __id = 0
        # arrival time
        __at = 0
        # burst time
        __bt = 0
        # total burst time
        __tbt = 0
        # starting time
        __st = 0
        # completion time
        __ct = 0
        # flag
        __setFlag = False

        def __init__(self, id, burst_time=0):
            self.__id = id

            self.__bt = burst_time
            self.__tbt = burst_time

        def decrement_burst_time(self):
            self.__bt = int(self.__bt) - 1
            return

        def setFlagstart(self, flagA):
            self.__setFlag = flagA

        def create_start_time(self, start_time):
            self.__st = start_time
            return

        def create_completion_time(self, completion_time):
            self.__ct = completion_time
            return

        def create_arrival_time(self, arrival_time):
            self.__at = arrival_time
            return

        def compute_turnaround_time(self):
            return int(self.__ct) - int(self.__at)

        def compute_waiting_time(self):
            return int(self.compute_turnaround_time()) - int(self.__tbt)

        def compute_partial_waiting_time(self):
            return int(self.__st) - int(self.__at)

        def compute_waiting_time_spent_in_queue(self):
            return int(self.compute_waiting_time()) - int(
                self.compute_partial_waiting_time()
            )

        def return_arrival_time(self):
            return int(self.__at)

        def return_burst_time(self):
            return int(self.__bt)

        def return_total_burst_time(self):
            return int(self.__tbt)

        def return_start_time(self):
            return int(self.__st)

        def return_completion_time(self):
            return int(self.__ct)

        def return_id(self):
            return int(self.__id)

        def return_flag(self):
            return self.__setFlag

        def display(self):
            print("P{}  {:^5}   {:^5}   {:^5}   {:^5}   {:^5}   {:^5}   {:^5}   {:^5}".format(self.__id, self.__at, self.__tbt, self.__st, 
            self.compute_waiting_time_spent_in_queue(), self.__ct, self.compute_waiting_time(), self.compute_partial_waiting_time(), 
            self.compute_turnaround_time()))
            



    # Returns the burst time in order to compare it in the function
    def sort_processor_precedence(sort_array):
        return sort_array.return_burst_time()


    # Creates a ready queue on the existing sorted queue
    def create_ready_queue(prepare_queue, size):

        queue_ready = []

        for prepare_queue in processor_array:
            if prepare_queue.return_arrival_time() == 0:
                queue_ready.append(prepare_queue)

        return queue_ready


    # Top border dashes for the Gantt Chart
    def top_bottom_borders(size, post_border):
        new_border = post_border
        for i in range(1, (size * 2) + 1):
            new_border = new_border + "-"
        new_border = new_border + " "
        return new_border


    # Content provider in the middle of the Gantt Chart
    def content_of_Gantt_Chart(size, post_content, processor_id):
        new_content = post_content

        for i in range(1, (size * 2)):
            if i == size:
                new_content = new_content + "p" + str(processor_id)
            else:
                new_content = new_content + " "
        new_content = new_content + "|"
        return new_content


    # This adds the timer below the gantt chart
    def timer_label_func(size, ptimer_label, ptimer):
        new_label = ptimer_label

        for i in range(1, (size * 2) + 1):
            new_label = new_label + " "
        if ptimer > 9:
            new_label = new_label[: len(new_label) - 1] + str(ptimer)
        else:
            new_label = new_label + str(ptimer)
        return new_label


    # Checks if the ready queue is empty
    def isEmpty(queue):
        for elements in queue:
            if elements is not None:
                return False
        return True


    # Performs a simulation of the Gantt Function
    def simulate_Gantt_Chart(ready_queue, orig_queue, with_arrival):
        # check ensures it will be performed only once
        check = 0
        # index is where it calucated the time burst during the execution per second
        index = 0
        # Timer in miliseconds
        timer = 0

        # Timer_label, border, content for the gantt chart
        timer_label = "0"
        border = " "
        content = "|"

        # Makes the condition of the start time true
        ready_queue[0].setFlagstart(True)

        # Continues the loop until the queue is empty
        while isEmpty(ready_queue) is False:

            # If 0, checks if the burst time is finish
            if ready_queue[0].return_burst_time() == 0:
                getId = ready_queue[0].return_id()
                ready_queue[0].create_completion_time(timer)

                # Adds the contents base on index and time and id
                border = top_bottom_borders(index, border)
                content = content_of_Gantt_Chart(index, content, getId)
                timer_label = timer_label_func(index, timer_label, timer)

                # Removes the queue
                ready_queue.pop(0)

                # Sorts the queue for the first one to finish
                ready_queue = sorted(ready_queue, key=sort_processor_precedence)

                # Checks if the queue is not empty
                if isEmpty(ready_queue) is False:
                    # Checks if the start time is 0
                    if ready_queue[0].return_start_time() == 0:
                        # Checks if the start time has not been created yet
                        if ready_queue[0].return_flag() is False:
                            ready_queue[0].create_start_time(timer)
                            ready_queue[0].setFlagstart(True)
                # Resets the burst counter
                index = 0
                continue

            # This is to make sure everythign is pre-emptive when using this
            if with_arrival == "Y" or with_arrival == "y":
                for elements in orig_queue:
                    # Checks if the arrival time of the not 0
                    if elements.return_arrival_time() != 0:
                        # Checks if the element is equivalent to the timer to be placed on the queue
                        if elements.return_arrival_time() == timer:
                            # Checks the new process if it's less than current process in execution
                            if (
                                elements.return_burst_time()
                                < ready_queue[0].return_burst_time()
                            ):
                                # Check ensures that when switched, the gantt chart will execute once during that time
                                if check == 0:
                                    getId = ready_queue[0].return_id()
                                    border = top_bottom_borders(index, border)
                                    content = content_of_Gantt_Chart(index, content, getId)
                                    timer_label = timer_label_func(
                                        index, timer_label, timer
                                    )
                                    check = 1
                                    index = 0
                                    # Places the new process into the queue
                                    ready_queue.append(elements)

                                    # Checks if it has no start_time
                                    if elements.return_flag() is False:
                                        elements.create_start_time(timer)
                                        elements.setFlagstart(True)
                                    # THis is sorting the Queue in order for the new one to appear again
                                for i in range(1, len(ready_queue)):
                                    temp = ready_queue[0]
                                    ready_queue.pop(0)
                                    ready_queue.append(temp)
                                    del temp
                            else:
                                # If false then place it on the elements
                                ready_queue.append(elements)

            timer = timer + 1
            index = index + 1
            # Decreases the burst time per timer miliseconds
            ready_queue[0].decrement_burst_time()
            check = 0

        # Displays the Gantt chart
        print(border)
        print(content)
        print(border)
        print(timer_label)


    # Main Function
    number_of_processors = int(input("Enter number of processes: "))

    # Creates a certain number of arrays for the processors
    processor_array = [None] * number_of_processors


    # Inputs burst time
    i = 0
    print("Burst time:")
    while i < number_of_processors:
        burst_time = input(f"P{i + 1}: ")
        processor_array[i] = Processor(i + 1, burst_time)
        i = i + 1

    # Waits for user input. Any other
    decision_arrival = input(
        "Set Arrival? type 'y' or 'Y'. Another other input sets arrival time to 0: "
    )

    # Inputs Arrival Time if User wants it
    if decision_arrival == "y" or decision_arrival == "Y":
        print("Arrival Time: ")
        i = 0
        for elements in processor_array:
            arrival_time = input(f"P{i + 1}: ")
            elements.create_arrival_time(arrival_time)
            i = i + 1

    # Sorting the array in order based on burst time
    processor_array = sorted(processor_array, key=sort_processor_precedence)


    # Calls the ready queue function to be placed on the ready queue
    ready_queue = create_ready_queue(processor_array, number_of_processors)

    # Calls the simulation of the Gantt chart and passes the ready queue and the original queue
    simulate_Gantt_Chart(ready_queue, processor_array, decision_arrival)

    # Displays the details of the Processors
    Average_waiting_time = 0
    Average_turnaround_time = 0


    print("TABLE\n{}  {:^6}  {:^6}  {:^6}  {:^6}  {:^6}  {:^6}   {:^6}   {:^6}".format(
        'P', 'AT', 'BT', 'ST', 'WQT', 'CT', 'WT', 'PWT', 'TAT'))
    for elements in processor_array:
        Average_waiting_time = Average_waiting_time + elements.compute_waiting_time()
        Average_turnaround_time = (
            Average_turnaround_time + elements.compute_turnaround_time()
        )
 
        elements.display()

    print("")
    print("Average Waiting Time: ", end=str(Average_waiting_time / len(processor_array)))
    print("")
    print("Average Turnaround Time ", end=str(Average_turnaround_time / len(processor_array)))
    print(" ")
