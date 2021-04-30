

def run():
    #Inputs the reference string
    print("Enter the reference string: ", end="")
    refList = list(map(int, input().strip().split()))

    #Inputs the capacity or size of the page frame
    print("Enter the number of frames: ", end="")
    capacity = int(input())
                    
    #Initiates the page frame to be given            
    page_frame = [] 
    #Initiates the page fault. set defaults to 0
    pageFaults = 0
    #This one discovers what is recently used during comparison
    most_recently_used = None

    #Loops through the entire reference list to check with the page_frame
    for i in refList:
        #Checks if the element is in the page frame
        if i not in page_frame:
            #If the page frame is empty or less than the capacity
            if len(page_frame) < capacity:
                page_frame.append(i)
            #If it's not empty, then replace the one with the most recently used 
            else:
                #Finds the matching page inside the page_frame and replaces it
                index = page_frame.index(most_recently_used)
                page_frame[index] = i
            #Increase the page fault since the page is not in the page frame
            pageFaults +=1
        #Sets the current checked frame as the one as the most recently used.
        most_recently_used = i
        
    #Prints the page frame
    print("{}".format(pageFaults))