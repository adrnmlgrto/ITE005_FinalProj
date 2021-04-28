def run():
    def seekTime(h, q):
        # inserts initial head pos. at the beginning of the queue
        q.insert(0, h)
        q = sorted(q)   # sorts the queue from lowest to highest
        fq = []         # will contain proper seek sequence
        st = 0          # total seek time

        if(isLeft):                     # checks if the user chose left or right direction
            for i in range(q.index(h), 0, -1):  # loops from initial head pos to index 0
                # transfers finished element in q to fq
                fq.append(q.pop(i))

            # adds first element of q to the last for operation below
            q.append(q.pop(0))

            for i in range(len(q)-1, -1, -1):   # loops from initial head pos to index 0
                # transfers finished element in q to fq
                fq.append(q.pop(i))

            for i in range(len(fq)-1):          # increments the total seek time with computed
                st += abs(fq[i]-fq[i+1])        # seek time each iteration
        else:
            i = q.index(h)
            while(len(q) > i):      # loops while q length is greater than the index of initial head pos
                # transfers finished element in q to fq
                fq.append(q.pop(i))

            # adds last element of q to the first for operation below
            q.insert(0, q.pop(len(q)-1))
            q = sorted(q)

            while(len(q) > 0):           # loops while q is not empty
                # transfers finished element in q to fq
                fq.append(q.pop(0))

            for i in range(len(fq)-1):      # increments the total seek time with computed
                st += abs(fq[i]-fq[i+1])    # seek time each iteration

        return fq, st           # tuple return value

    isLeft = True   # boolean to check direction, defaults to true

    # initial head pos input
    ihead = int(input("Enter Initial Head Position: "))

    queue = input("Enter request queue (must be seperated by space): ")
    reqs = [int(x) for x in queue.split()]

    d = input("Enter direction [r] or [l]: ")
    if(d == 'r'):                   # sets isLeft false when user chooses r
        isLeft = False

    x = seekTime(ihead, reqs)       # function call

    print("Initial Head Position: "+str(x[0].pop(0)))
    print("Seek Sequence: "+str(x[0]))
    print("Total Seek Time: "+str(x[1]))
