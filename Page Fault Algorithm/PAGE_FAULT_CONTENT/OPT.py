def run():
    def get_page_fault(input_array, size):
        #Display what index of the frame_array has been placed first
        FIFO_array = []
        #This is the frame array where it will be inserted
        page_array = []
        #the number of page fault
        page_fault = 0

        #Predicts the future reference string that will less likely to be usedin the future
        def optimize (input_array, page_array, FIFO_array, index):
            #the index of the page_array
            position = -1
            #computing the farthest distance in the ref_string
            farthest_distance = index
            #If there is no value found in the reference string
            nothing_list = []
            
            #Loops the page_array to find out the distance and get its position/index
            for i in range (0, len(page_array)):
                #This checks if the ref_string in page_array is exist
                flag = False
                #Loops through the input array
                for j in range (index, len(input_array)):
                    #Tries to find the ref_string in the page array in the list of the original ref_string array
                    if input_array[j] == page_array[i]:
                        #Checks if the current farthest_distance is less than the current distance
                        if farthest_distance < j: 
                            #Sets the farthest_distance 
                            farthest_distance = j
                            #Gets the position
                            position = i
                        #Since it is existing inside the array, set flag to true    
                        flag = True
                        #breaks the J loop
                        break
                #If no array, add ref_string to the Nothing_list
                if flag is False:
                    nothing_list.append(page_array[i])

            #If and elif condition checks if there is something in the nothing_list and tries to get that instead
            #else condition is where it returns the position to be replaced
            if len(nothing_list) == 1:
                get = nothing_list[0]
                return page_array.index(get)
            elif len(nothing_list) > 1:
                
                get_index = FIFO_array[0]
                for current_nothing in nothing_list:
                    if page_array[get_index] == current_nothing:
                        return page_array.index(current_nothing)
            else:
                return position


        #Every reference string to be put in the frame
        for i in range (0, len(input_array)):
            #Sets the current ref_string of the input array
            current = input_array[i]
            #Checks if the ref_string exists in the page_array
            if current not in page_array:
                #Checks if the there are available page_array size
                if len(page_array) < size:
                    #Adds the ref string to the frame list and the index (Where it's placed) into the FIFO_arrray
                    page_array.append(current)
                    FIFO_array.append(len(FIFO_array))
                elif i == len(input_array)-1:
                    #At the last ref_string, it gets the position of the Earliest refstring that had been placed and replaced it
                    get_position = FIFO_array.pop(0)
                    page_array[get_position] = current
                    FIFO_array.append(get_position)
                else:
                    #Goes to the optimize function to get the position of the ref_string to be replaced
                    get_position = optimize(input_array, page_array, FIFO_array, i+1)
                    page_array[get_position] = current
                    #Sets the newly placed ref_string as the latest input
                    FIFO_array.append(FIFO_array.pop(get_position))
                #Increases the page fault if the ref_string is not in the array
                page_fault = page_fault + 1
            else:
                #Continues
                continue
        #Returns the total Page fault
        return page_fault

 

    #Inputs the queue and the frame size
    queue = input("Enter sequence (must be seperated by space): ")
    queue = [int(x) for x in queue.strip().split()]
    frame_size = int(input("Enter Frame size: "))

    #Displays the total page fault
    print(get_page_fault(queue, frame_size))
