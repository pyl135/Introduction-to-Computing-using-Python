#Write a function called wordLengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, and exclamation points.
#
#For example:
#  wordLengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
#Hint: Use the split() method to split by spaces, and don't
#forget to remove punctuation marks.  Remember also: strings
#are immutable, so operations like myString.lower() don't
#change the value of myString like list methods: to save
#those results, you'd write myString = myString.lower().


#Write your function here!
def wordLengths(input):
    input = input.lower()
    input = input.replace("!","")
    input = input.replace("?","")
    input = input.replace(".","")
    input = input.replace(",","")
    in_split = input.split(" ")
    dict = {}
    for item in in_split:
        dict[item] = len(item)

    return dict

#The line of code below will test your code. It's not used
#for grading, so feel free to modify it for testing.
print(wordLengths("I ate a bowl of cereal out of a dog bowl today."))
