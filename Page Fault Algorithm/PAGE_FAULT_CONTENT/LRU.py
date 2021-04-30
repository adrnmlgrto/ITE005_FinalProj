def run():
    #initializing variables
    frame,pageListString,fault,pageFault = [],[],0,'No'

    #insertion of number of frames in variable capacity as integer
    print("Enter the number of frames: ",end="")
    capacity = int(input())

    #insertion of number of reference string in variable referenceStringArray as integer array
    print("Enter the reference string: ",end="")
    #the type of input is string, this will be later then processed by the following functions to be array of strings:
    #list() a function that returns a list, 
    #map() a function that loops in its parameter and maps the iteration to list
    #strip() removes spaces at the beginning and end of the string to clean the string for user error
    #split() splits array to list elements based on separator (default whitespace)
    referenceStringArray = list(map(int,input().strip().split()))
    #loops in the every element of referenceStringArray
    for i in referenceStringArray:
        #checks if i is not in the frame
        if i not in frame:
            #if condition is met check if the length of current frame is less than capacity to avoid overflowing the limit in number of frames 
            #have page fault
            if len(frame)<capacity:
                #if condition is met append the current value of i to frame and page to the the current page we are in
                frame.append(i)
                #appends the current page to pageListString to keep track on the current page we are in
                pageListString.append(len(frame)-1)
            else:
                #if coditions aren't met it means page overflows the capacity thus pop the first element of page 
                leastRecentlyUsedPage = pageListString.pop(0)
                #replace the leastRecentlyUsedPage to the value of i to frame
                frame[leastRecentlyUsedPage] = i
                #appends the current page to pageListString to keep track on the current page we are in
                pageListString.append(leastRecentlyUsedPage)
            #after all the previous condition has been checked iterate the value of fault by 1
            fault += 1
        else:
            #no page fault
            #appends the current page to pageListString to keep track on the current page we are in
            pageListString.append(pageListString.pop(pageListString.index(frame.index(i))))
            
    
            
    #print number of faults   
    print("\nTotal Page Faults: %d"%(fault))