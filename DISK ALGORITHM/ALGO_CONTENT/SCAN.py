def run():
    # SCAN Algorithm (To The Left)
    # This is the function to operate and compute the total seeking time and display the current simulation
    def scan_disc(list, head, start, direction):
        run = 2
        seek_time = 0
        current = head
        sequence_array = []
        while(run != 0):
            # Seek_time defaults to 0

            # index is the place of the headstart
            # Current is the headstart value itself

            if(direction == "left"):
                index = start
            else:
                index = start + 1
            # Loops while index is greater than or equal to 0

            if(direction == "left"):
                while(index >= 0):
                    # Computes the distance between the current value and the queue itself, also the seek time itself
                    distance = current - list[index]
                    # Computes the total seek_time
                    seek_time = seek_time + distance
                    # Displays the simulation in progress
                    print("Current: ",  str(current))
                    print("Next Seeking Node: ", str(list[index]))
                    print("Seeking Time: ",  str(distance))
                    # Adds a break
                    print()

                    # THe current value now seeks to the next value of Scan to the left.
                    current = list[index]
                    sequence_array.append(current)

                    index = index - 1
                    direction = "right"
            else:
                # Scans the seeking time to the right
                while(index < len(list)):
                    # Absolute distance to get the positive distance
                    distance = abs(current - list[index])
                    seek_time = seek_time + distance
                    print("Current: ",  str(current))
                    print("Next Seeking Node: ",  str(list[index]))
                    print("Seeking Time: ",  str(distance))
                    print()

                    current = list[index]
                    sequence_array.append(current)
                    index = index + 1
                    direction = "left"

            # if the index now reaches to the last part of the queue to the left, it continues to the 0 part as per the scan algorithm.
            if run == 2:
                if index < 0:
                    # Computes total seek time.
                    seek_time = seek_time + current
                    print("No more list, Approaching 0 and Reverse Direction")
                    print("Seeking Time: ",  str(current))
                    print()
                    current = 0
                else:
                    current = abs(199-current)
                    seek_time = seek_time + current
                    print("No more list, Approaching 199 and Reverse Direction")
                    print("Seeking Time: ",  str(current))
                    print()
                    current = 199

            run = run - 1

        # Returns the seeking time
        return seek_time, sequence_array

    # The queue

    # Input the queue sequence and split it by space
    queue = input("Enter sequence (must be seperated by space): ")
    queue = [int(x) for x in queue.split()]

    # The size of the queue list
    size = len(queue)
    # The headstart value
    head = int(input("Enter Headstart value: "))
    # Initializing the start position of the head
    start = 0
    # Sorts the queue in increasing order
    queue.sort()

    direction = input("Enter Direction (All small letters): ")
    # Checks the queue to set up the start. If the headvalue is less than the first one in the queue, then it will scan to 0 to the left then to the right
    if (head < queue[0]):
        start = -1
    # This checks if the head value is greater than last one in the queue
    elif (head >= queue[size-1]):
        start = size-1
    else:
        # checks if the head value position is in between the list and gets the index lower than the head value.
        for i in range(0, size-2):
            if(head >= queue[i] and head <= queue[i+1]):
                if head == queue[i+1]:

                    start = i+1
                    break
                else:
                    start = i
                    break
    # prints the Total seeking time by converting the seeking time integer into string using the parameters of the queue list, head value and the start position of the head
    x = scan_disc(queue, head, start, direction)
    print("Cylinder Movement: ", x[0])
    print("Sequence Array: ", x[1])
