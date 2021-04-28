def run():
    # CSCAN Algo
    # this function, controlls and loops the queu to solve the seektime
    def computeSeekTime(arr, headStart, mode):
        left = list()  # created a constructor for both directions
        right = list()
        for i in arr:  # loops the list created for queue
            if i < headStart:
                left.append(i)
            elif i > headStart:
                right.append(i)
        seekSequence = []
        seekTime = 0
        leftLim = 0
        rightLim = 199
        if mode == 2:
            print("Direction: Right")
            # sorting both vectors
            left.sort()
            right.sort()
            # First service the requests on the right side of the head
            for curr in right:
                # changes the value of seektime by getting the difference of
                seekTime += abs(headStart - curr)
                # headstart and current headstart, then add
                headStart = curr  # accessed track is now the new headStart
                seekSequence.append(curr)
            if len(left) > 0:  # checks if the size of length is not 0; if it still has values
                # if yes, increase the seektime by getting the absolute difference of headStart and right limit
                seekTime += abs(headStart - rightLim)
                # increase the seektime by getting the absolute difference of right limit and left limit
                seekTime += abs(rightLim - leftLim)
            headStart = leftLim     # accessed left limit is now the new head
            for curr in left:
                seekTime += abs(headStart - curr)
                headStart = curr
                seekSequence.append(curr)

        elif mode == 1:  # To the left (default)
            print("Direction: Left")
            left.sort(reverse=True)  # reverse direction
            right.sort(reverse=True)
            for curr in left:  # access every track in left vector
                # increase seektime by adding the absolute difference of head and the current track
                seekTime += abs(headStart - curr)
                headStart = curr    # accessed current track is now the head
                seekSequence.append(curr)
            if len(right) > 0:
                seekTime += abs(headStart - leftLim)
                seekTime += abs(leftLim - rightLim)
            # accessed right limit (track) is now the head
            headStart = rightLim
            for curr in right:  # access every queu in right vector
                # increase the seektime by adding the absolute difference of headstart and accessed current track
                seekTime += abs(headStart - curr)
                headStart = curr  # accessed track is now the new head
                seekSequence.append(curr)
        print("Total Seek Time: ", seekTime)
        print("Seek Sequence is:", end=' ')
        print(*seekSequence, sep=" -> ")

    # get inputs
    print("CSCAN Disk Scheduling Algorithm")

    queue = input('Enter Request Queue (With Spaces In-Between): ')
    array = [int(x) for x in queue.split()]

    head = int(input("Enter Position of Disk Head: "))  # position of disk head

    direction = int(input("[1] Left\n[2] Right\nEnter direction: "))
    # pass the parameters for the function compute Seektime to find the seek time
    computeSeekTime(array, head, direction)
