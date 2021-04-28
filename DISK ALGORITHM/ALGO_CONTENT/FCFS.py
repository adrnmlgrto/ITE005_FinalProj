def run():
    # FCFS Algorithm
    # USER INPUT OF THE REQUEST QUEUE SIZE AND ELEMENTS IN THE REQUEST QUEUE
    queue = input('Enter Request Queue (With Spaces In-Between): ')
    reqs = [int(x) for x in queue.split()]

    # USER INPUT OF THE CURRENT HEAD POSITION
    curr_track = int(input('Current Track Position: '))

    # LIST THAT STORES THE MOVEMENT OF THE HEAD
    head_movement = [curr_track]

    # TOTAL SEEK TIME
    seek_time = 0

    # NEXT POSITION OF THE HEAD
    for i in range(len(reqs)):
        temp_value = curr_track
        curr_track = reqs[i]
        seek_time += abs(curr_track - temp_value)
        head_movement.append(curr_track)

    print()
    print(f'Total Head Movement (Total Seek Time): {seek_time} cylinders')
    print('SEQUENCE:', end=' ')
    print(*head_movement, sep=' -> ')
