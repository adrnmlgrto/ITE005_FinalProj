def run():
    print(" ")
    print("LOOK")
    print(" ")

    # distance
    dist = 0

    # current value that is to be subtracted from the headPosition
    current = 0

    # total number of seek
    totalSeek = 0

    # Ask for user inputs (Request Queue and Initial Head Position)
    queue = input('Enter Request Queue (With Spaces In-Between): ')
    requests = [int(x) for x in queue.split()]
    n = len(requests)

    # ask for the head
    headPos = (int(input("Enter initial head position: ")))

    # ask for the direction
    direction = input("Enter direction (left or right): ")

    # for storage of right and left and sequence
    right = []
    left = []
    sequence = []
    sequence.append(headPos)

    # gather the left and right elements
    for i in range(0, n):
        # if the values are HIGHER THAN THE HEADPOS, append to right list
        if requests[i] > headPos:
            right.append(requests[i])

        # if the values are LOWER THAN THE HEADPOS, append to left list
        elif requests[i] < headPos:
            left.append(requests[i])

    # for sorting the elements in the lists
    right.sort()
    left.sort()

    # can only be repeated twice, as there are only two directions(left and right)
    repeat = 2
    while(repeat):
        if direction == "left":

            # range(start, stop, step) going to the LEFT
            for i in range(len(left) - 1, -1, -1):
                # value of i from left will be the current
                current = left[i]

                # append it to the sequence list
                sequence.append(current)

                # get the distance by subtracting the current value from the headPosition with absolite value
                dist = abs(headPos - current)
                # add it to totalSeek
                totalSeek = totalSeek + dist

                # assign the current value to the headpos, so it can be used later again in getting the distance
                headPos = current

            # change the direction to right so the right side can be computed
            direction = "right"

        elif direction == "right":

            # range(start, stop, step) going to the RIGHT
            for i in range(len(right)):
                # value of i from right will be the current
                current = right[i]

                # append it to the sequence list
                sequence.append(current)

                # get the distance by subtracting the current value from the headPosition with absolute value
                dist = abs(headPos - current)
                # add it to totalSeek
                totalSeek = totalSeek + dist

                # assign the current value to the headpos, so it can be used later again in getting the distance
                headPos = current

            # change the direction to left
            direction = "left"

        # minus 1 to the repeat, to repeat the process
        repeat = repeat - 1

    print(" ")
    print(" ")
    print("SEEK TIME: ")
    print(totalSeek, " cylinders")
    print(" ")
    print("SEQUENCE: ")
    print(*sequence, sep=' --> ')
    print(" ")
