def run():
    # CAN BE USED WHEN USING SCAN/CSCAN ALGORITHM
    # min_track = 0
    # max_track = 199

    # USER INPUT OF THE REQUEST QUEUE SIZE AND ELEMENTS IN THE REQUEST QUEUE
    queue = input('Enter Request Queue (With Spaces In-Between): ')
    request_queue = [int(x) for x in queue.split()]

    # USER INPUT OF THE CURRENT POSITION OF THE HEAD
    curr_track = int(input('Current Track Position: '))

    # LIST WHERE THE ABS(DESTINATION-ORIGIN) IS PLACED
    seek_time = []

    # LIST FOR HOW THE HEAD MOVES IN THE REQUEST QUEUE
    movement = [curr_track]

    # THE PROCESS WHILE REQUEST QUEUE IS NOT EMPTY
    while len(request_queue):
        hold = 0
        minimum = abs(curr_track - request_queue[0])
        destination = 0

        # ITERATION OF EACH REQUESTS TO DETERMINE THE SMALLEST SEEK TIME NEAREST TO THE CURRENT TRACK POSITION
        for i in range(len(request_queue)):
            # pos_diff (POSITION DIFFERENCE)
            pos_diff = abs(curr_track - request_queue[i])

            # IF THE POS_DIFF IS SMALLER THAN THE CURRENT MINIMUM VALUE
            # SET THE CURRENT MINIMUM VALUE TO THE POS_DIFF AND
            # HOLD THE CURRENT INDEX OF THE MINIMUM VALUE
            if minimum > pos_diff:
                minimum = pos_diff
                hold = i

        # AFTER FINDING THE ELEMENT IN THE LIST THAT HAS THE SMALLEST SEEK TIME, SET IT AS THE DESTINATION
        # AND APPEND THE SEEK TIME TO ANOTHER LIST FROM THE ABS(DESTINATION-CURRENT TRACK POSITION)
        # THEN SET THE CURRENT TRACK POSITION FROM THE PREVIOUS DESTINATION
        destination = request_queue.pop(hold)
        seek_time.append(abs(destination-curr_track))
        curr_track = destination
        # RETRIEVING THE VALUE OF HEAD POSITION AND PLACING IN LIST FOR SEQUENCE PRINTING
        movement.append(curr_track)

    print()
    print(f'Total Head Movement (Total Seek Time): {sum(seek_time)} cylinders')
    print('SEQUENCE:', end=' ')
    print(*movement, sep=' -> ')
