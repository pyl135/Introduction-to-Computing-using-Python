def selectionSort(aList):
    
    #For each index in the list...
    for i in range(len(aList)):
        
        #Assume first that current item is already correct...
        minIndex = i

        #For each index from i to the end...
        for j in range(i + 1, len(aList)):
            
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if aList[minIndex] > aList[j]:
                minIndex = j

        #Save the current minimum value since we're about
        #to delete it
        minValue = aList[minIndex]
        
        #Delete the minimum value from its current index
        del aList[minIndex]
        
        #Insert the minimum value at its new index
        aList.insert(i, minValue)
    
    #Return the resultant list
    return aList
	
# print(selectionSort([5, 3, 1, 2, 4]))
