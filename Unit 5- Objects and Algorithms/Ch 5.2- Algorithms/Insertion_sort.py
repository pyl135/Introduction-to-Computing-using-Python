def insertion(aList):
    for i in range(1,len(aList)):
        tmp = aList[i]
        j=i - 1
        while j >= 0: 
            if tmp < aList[j]:                        
                aList[j+1] = aList[j]
                aList[j] = tmp
                j -= 1
            else:
                break

    return aList
