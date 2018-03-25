#Recall last exercise that you wrote a function, wordLengths,
#which took in a string and returned a dictionary where each
#word of the string was mapped to an integer value of how
#long it was.
#
#This time, write a new function called lengthWords so that
#the returned dictionary maps an integer, the length of a
#word, to a list of words from the sentence with that length.
#If a word occurs more than once, add it more than once.
#
#For example:
#
#  lengthWords("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
#As before, you should remove any punctuation and make the
#string lowercase.
#
#Hint: To create a new list as the value for a dictionary key,
#use empty brackets: lengths[wordLength] = []. Then, you would
#be able to call lengths[wordLength].append(word). Note that
#if you try to append to the list before creating it for that
#key, you'll receive a KeyError.


#Write your function here!
def lengthWords(input):
    input = input.lower()
    input = input.replace("!","")
    input = input.replace("?","")
    input = input.replace(".","")
    input = input.replace(",","")
    in_split = input.split(" ")
    dict = {}

    for word in in_split:
        word_len=len(word)
        if word_len in dict:
            dict[word_len].append(word)
        else:
            dict[word_len] = [word]

    return dict

#The code below will test your function. It isn't used for
#grading, so feel free to modify it.
print(lengthWords("I ate a bowl of cereal out of a dog bowl today."))
