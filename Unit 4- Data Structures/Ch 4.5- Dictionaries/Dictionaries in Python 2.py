#Create a function called tup2Dict. tup2Dict should take one
#parameter: a list of tuples. You can assume each tuple in
#the list has exactly two values.
#
#The function should return a dictionary where the first item
#in each tuple is the key, and the second item in each tuple
#is the corresponding value.
#
#For example:
# colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
# tup2Dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
#
#Hint: the previous exercise is very similar; this just turns
#it into a function!


#Write your function here!
def tup2Dict(data):
    dict = {}
    for item in data:
        if item[0] not in dict:
            dict[item[0]] = item[1]
    return dict        


#The code below will test your function. It is not used for
#grading, so feel free to modify it. As written, this should
#print: {'turquoise':'#40E0D0', 'red':'#990000'}
#Don't worry if it prints those in the reverse order; that's
#still correct!
print(tup2Dict([("turquoise", "#40E0D0"), ("red", "#990000")]))
