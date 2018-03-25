#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
def reader(filename):
    output = open(filename, "r")
    array= ()
    sum = []
    for line in output:
        each = line.split()
        one = int(each[0])
        two = each[1]
        three = int(each[2])
        four = int(each[3])
        five = float(each[4])

        array = (one,two,three,four,five)
        sum.append(array)

    return sum

    output.close()

#We have supplied the same sample.cs1301 from the previous
#exercise. Feel free to test your code with it to see if it
#works:
print(reader("sample.cs1301"))
