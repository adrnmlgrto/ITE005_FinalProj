def run():
    #for the input of process sequence
    queue = input("Enter reference string (must be seperated by space): ")

    #for splitting the process sequence and putting them in pages list
    pages = [int(x) for x in queue.split()]

    #ask for number of frames
    frames = int(input("Enter number of frames: "))

    #current pages list
    current_pages = []
    page_fault = 0

    #traverse through the pages list
    for x in pages:

        #if the value of x is not in current_pages
        if x not in current_pages:

            #check if current_pages reach the number of frames
            if len(current_pages) == frames:
                current_pages.remove(current_pages[0])
                current_pages.append(x)

            #if not, append the values
            else: 
                current_pages.append(x)
            
            page_fault = page_fault + 1

    print("Number of page faults: ", page_fault)


