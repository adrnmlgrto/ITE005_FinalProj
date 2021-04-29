def run():
    def seekTime(h, q):
        # inserts initial head pos. at the beginning of the queue
        q.insert(0, h)
        q = sorted(q)   # sorts the queue from lowest to highest
        s_seq = []         # will contain proper seek sequence
        s_time = 0      # total seek time

        if(isLeft):                     # checks if the user chose left or right direction
            for i in range(q.index(h), 0, -1):  # loops from initial head pos to index 0
                # transfers finished element in q to s_seq
                s_seq.append(q.pop(i))

            # adds first element of q to the last for operation below
            q.append(q.pop(0))

            for i in range(len(q)-1, -1, -1):   # loops from initial head pos to index 0
                # transfers finished element in q to s_seq
                s_seq.append(q.pop(i))

            # increments the total seek time with computed
            for i in range(len(s_seq)-1):
                # seek time each iteration
                s_time += abs(s_seq[i]-s_seq[i+1])
        else:
            i = q.index(h)
            while(len(q) > i):      # loops while q length is greater than the index of initial head pos
                # transfers finished element in q to s_seq
                s_seq.append(q.pop(i))

            # adds last element of q to the first for operation below
            q.insert(0, q.pop(len(q)-1))
            q = sorted(q)

            while(len(q) > 0):           # loops while q is not empty
                # transfers finished element in q to s_seq
                s_seq.append(q.pop(0))

            for i in range(len(s_seq)-1):      # increments the total seek time with computed
                # seek time each iteration
                s_time += abs(s_seq[i]-s_seq[i+1])

        return s_seq, s_time           # tuple return value

    isLeft = True   # boolean to check direction, defaults to true

    # user generated request queue input
    queue_str = input("Enter request queue (must be seperated by space): ")
    req_queue = [int(x) for x in queue_str.split()]

    # initial head pos input
    i_pos = int(input("Enter Initial Head Position: "))

    d = input("Enter direction [r] or [l]: ")
    if(d == 'r'):                   # sets isLeft false when user chooses r
        isLeft = False

    x = seekTime(i_pos, req_queue)       # function call

    print("\nInitial Head Position: "+str(x[0].pop(0)))
    print("Seek Sequence: "+str(x[0]))
    print("Total Seek Time: "+str(x[1]))
