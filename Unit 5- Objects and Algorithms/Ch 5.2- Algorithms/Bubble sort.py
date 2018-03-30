def bubbleSort(lst):
    #Set swapOccurred to True to guarantee the loop runs once
    swapOccurred = True
    
    #Run the loop as long as a swap occurred the previous time
    while swapOccurred:
        
        #Start off assuming a swap did not occur
        swapOccurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swapOccurred = True            

    return lst

# print(bubbleSort([5, 3, 1, 2, 4]))
