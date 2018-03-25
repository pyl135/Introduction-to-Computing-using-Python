#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def get_grade(filename):
    output = open(filename, "r")
    all = 0

    for line in output:
        each = line.split()
        three = int(each[2])
        four = int(each[3])
        five = float(each[4])
        score = (three / four) * five
        all += score
    final = all *100

    return final
    output.close()

#We've supplied sample.cs1301 again to test your function.
#In its original form, it should result in: 
#  92.93372093023255 
print(get_grade("sample.cs1301"))
