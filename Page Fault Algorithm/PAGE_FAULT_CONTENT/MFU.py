def run():
    # GET USER INPUTS (REFERENCE STRING & NUMBER OF FRAMES)
    print("MFU Enter the reference string: ", end="")
    ref_str = list(map(int, input().strip().split()))

    print("Enter the number of frames: ", end="")
    frm_sz = int(input())

    # LIST THAT WILL HOLD THE CURRENT PAGES IN THE FRAME
    frm_list = []

    # DECLARATION OF NUMBER OF PAGE FAULTS OCCURED
    pg_fault = 0

    # DECLARATION OF A DICTIONARY THAT HOLDS THE TALLIES
    # TALLYING EVERY TIME A PAGE IS USED (VARIABLE 'i' IN THE LOOP)
    tally = dict.fromkeys(ref_str, 0)

    # TRAVERSING THE REFERENCE STRING AND GETTING EACH ELEMENT
    for i in ref_str:
        # CONDITION IF THE ELEMENT IS NOT YET IN THE FRAME
        if i not in frm_list:
            # CONDITION TO NOT EXCEED THE INTENDED FRAME SIZE OF THE LIST
            if len(frm_list) < frm_sz:
                frm_list.append(i)
                tally[i] += 1
            # CONDITION IF FRAME LIST IS FULL
            else:
                # DECLARATION OF ANOTHER DICTIONARY THAT WILL HOLD THE TALLIES
                # OF THE CURRENT ELEMENTS IN THE FRAME TO DETERMINE WHAT WILL BE REPLACED
                flist_check = {}
                # TRAVERSAL OF KEY-VALUE PAIRS
                for k, v in tally.items():
                    # CHECK IF THE PAGE IS IN THE CURRENT FRAME AND PUT IT
                    # IN THE DICTIONARY WITH ITS TALLY
                    if k in frm_list:
                        flist_check[k] = v

                # DETERMINING THE MOST RECENTLY USED PAGE INSIDE THE FRAME
                # IF EQUAL TALLIES, FIFO IS UTILIZED
                most_recently_used = max(flist_check, key=flist_check.get)

                # REPLACEMENT OF THE PAGE THAT IS MOST RECENTLY USED
                for j in range(len(frm_list)):
                    if frm_list[j] == most_recently_used:
                        frm_list[j] = i
                        tally[i] += 1
                        
                        value = tally.pop(most_recently_used)
                        newDict = {most_recently_used: value}
                        tally.update(newDict)
            pg_fault += 1
        # CONDITION IF PAGE IS IN THE FRAME AND NO PAGE FAULT WILL OCCUR
        else:
            tally[i] += 1

    print(f'\nTotal Number of Page Faults: {pg_fault}')
