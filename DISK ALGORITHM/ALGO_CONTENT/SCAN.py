def run():

    # This is the function to operate and compute the total seeking time and display the current simulation
    def scan_disc(list, head, start, direction, upper_size):
        run = 2
        seek_time = 0
        current = head
        sequence_array = []
        while(run != 0):
            # Seek_time defaults to 0

            # index is the place of the headstart
            # Current is the headstart value itself

            if(direction == 1):
                index = start
            else:
                index = start + 1
            # Loops while index is greater than or equal to 0

            if(direction == 1):
                while(index >= 0):
                    # Computes the distance between the current value and the queue itself, also the seek time itself
                    distance = current - list[index]
                    # Computes the total seek_time
                    seek_time = seek_time + distance
                    # Displays the simulation in progress

                    # Sets the seeked sequence as the current one
                    current = list[index]
                    # Appends to the seeking sequence
                    sequence_array.append(current)
                    # Gets the next request to the left
                    index = index - 1
                # Changes the direction to the right
                direction = 2
            else:
                # Scans the seeking time to the right
                while(index < len(list)):
                    # Absolute distance to get the positive distance
                    distance = abs(current - list[index])
                    # Adds the total number of seek time
                    seek_time = seek_time + distance

                    # Sets the seeked request as the current one
                    current = list[index]
                    # Appends to the seeking sequence
                    sequence_array.append(current)
                    # Gets the next sequence to the right
                    index = index + 1
                # Changes teh Direction to the left
                direction = 1

            # if the index now reaches to the last part of the queue to the left, it continues to the 0 part as per the scan algorithm.
            if run == 2:
                if index < 0:
                    # Computes total seek time.
                    seek_time = seek_time + current
                    # It reaches the end of the disk on the left
                    current = 0
                else:
                    current = abs(upper_size-current)
                    # It reaches the end of the disk on the right
                    seek_time = seek_time + current

                    current = upper_size
            # Reduces the cycle
            run = run - 1

        # Returns the seeking time and array
        return seek_time, sequence_array

    # The queue

    #Max_size = 0-max_size-1
    max_size = int(input("Please input the max size: "))
    # Input the queue sequence and split it by space
    queue = input("Enter sequence (must be seperated by space): ")
    # Puts the sequence in the array
    queue = [int(x) for x in queue.split()]

    # The size of the queue list
    size = len(queue)
    # The headstart value
    head = int(input("Enter Headstart value: "))
    # Initializing the start position of the head
    start = 0
    # Sorts the queue in increasing order
    queue.sort()

    direction = int(input("[1] Left\n[2] Right\nEnter direction: "))
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
    x = scan_disc(queue, head, start, direction, max_size - 1)
    print("Cylinder Movement: ", x[0])
    print("Sequence Array: ", x[1])
