def run():
    # CSCAN Algo
    # this function, controlls and loops the queu to solve the seektime
    def computeSeekTime(rq, i_pos, dir, size):
        left = list()  # created a constructor for both directions
        right = list()
        for i in rq:  # loops the list created for queue
            if i < i_pos:
                left.append(i)
            elif i > i_pos:
                right.append(i)
        seekSequence = []
        seekTime = 0
        leftLim = 0
        rightLim = size
        if dir == 2:
            print("Direction: Right")
            # sorting both vectors
            left.sort()
            right.sort()
            # First service the requests on the right side of the head
            for curr in right:
                # changes the value of seektime by getting the difference of
                seekTime += abs(i_pos - curr)
                # i_pos and current i_pos, then add
                i_pos = curr  # accessed track is now the new i_pos
                seekSequence.append(curr)
            if len(left) > 0:  # checks if the size of length is not 0; if it still has values
                # if yes, increase the seektime by getting the absolute difference of i_pos and right limit
                seekTime += abs(i_pos - rightLim)
                # increase the seektime by getting the absolute difference of right limit and left limit
                seekTime += abs(rightLim - leftLim)
            i_pos = leftLim     # accessed left limit is now the new head
            for curr in left:
                seekTime += abs(i_pos - curr)
                i_pos = curr
                seekSequence.append(curr)

        elif dir == 1:  # To the left (default)
            print("Direction: Left")
            left.sort(reverse=True)  # reverse direction
            right.sort(reverse=True)
            for curr in left:  # access every track in left vector
                # increase seektime by adding the absolute difference of head and the current track
                seekTime += abs(i_pos - curr)
                i_pos = curr    # accessed current track is now the head
                seekSequence.append(curr)
            if len(right) > 0:
                seekTime += abs(i_pos - leftLim)
                seekTime += abs(leftLim - rightLim)
            # accessed right limit (track) is now the head
            i_pos = rightLim
            for curr in right:  # access every queu in right vector
                # increase the seektime by adding the absolute difference of i_pos and accessed current track
                seekTime += abs(i_pos - curr)
                i_pos = curr  # accessed track is now the new head
                seekSequence.append(curr)
        print("Total Seek Time: ", seekTime)
        print("Seek Sequence is:", end=' ')
        print(*seekSequence, sep=" -> ")

    # get inputs
    print("CSCAN Disk Scheduling Algorithm")

    #Max_size = 0-max_size-1
    max_size = int(input("Please input the max size: "))
    queue = input('Enter Request Queue (With Spaces In-Between): ')
    req_queue = [int(x) for x in queue.split()]

    head = int(input("Enter Position of Disk Head: "))  # position of disk head

    direction = int(input("[1] Left\n[2] Right\nEnter direction: "))
    # pass the parameters for the function compute Seektime to find the seek time
    computeSeekTime(req_queue, head, direction, max_size-1)
