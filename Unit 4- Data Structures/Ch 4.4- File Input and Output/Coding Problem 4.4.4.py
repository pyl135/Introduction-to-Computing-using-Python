#Write a function called write_1301 which will write a file
#in the format described in Coding Problem 4.4.2. The
#sample.cs1301 file has been included to refresh your 
#memory. Your function should accept two arguments:
#A string of a filename to write to, and a list of tuples. 
#You can assume that each tuple will have the following 
#format:
#
#(int, str, int, int, float)
#
#Each tuple will represent a line in the file, and each
#item in the tuple should correspond to the 
#assignment number, the assignment name, the student's 
#grade, the total possible number of points, and the 
#assignment weight respectively. 


#Write your function here!
def write_1301(filename,tupleList):
    output= open(filename,"w")
    result=[]
    for each in tupleList:
        oneline =str(each[0]) +" "+ each[1] +" "+ str(each[2])+ " "+ str(each[3])+ " "+ str(each[4])
        result.append(oneline + "\n")

    output.writelines(result)

    output.close()
#The code below will test your function. It's not used
#for grading, so feel free to modify it!
tuple1 = (1, "exam_1", 90, 100, 0.6)
tuple2 = (2, "exam_2", 95, 100, 0.4)
tupleList = [tuple1, tuple2]
write_1301("test.cs1301", tupleList)


########################################################
#    with open(filename, 'w') as output:
#        output.write('\n'.join('%s %s %s %s %s' % x for x in tupleList))
