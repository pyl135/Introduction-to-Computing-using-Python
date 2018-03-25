#Write a function called 'string_type' which accepts one
#string argument and determines what type of string it is. 
#
# - If the string is empty, return "empty".
# - If the string is a single character, return "character".
# - If the string represents a single word, return "word".
#   The string is a single word if it has no spaces.
# - If the string is a whole sentence, return "sentence".
#   The string is a sentence if it contains spaces, but
#   at most one period.
# - If the string is a paragraph, return "paragraph". The
#   string is a paragraph if it contains both spaces and
#   multiple periods (we won't worry about other
#   punctuation marks).
# - If the string is multiple paragraphs, return "page".
#   The string is a paragraph if it contains any newline
#   characters ("\n").
#
#Hint: think carefully about what order you should check
#these conditions in.
#
#Hint 2: remember, there exists a count() method that
#counts the number of times a string appears in another
#string. For example, "blah blah blah".count("blah")
#would return 3.


#Write your function here!
def string_type(string):
    dot= string.count(".")
    pun= string.count("!")
    space =string.count(" ")

    if string.count("\n") >=1:
        return "page"
    elif (dot + pun) >=2:
        return "paragraph"
    elif space >=1 and (dot + pun) ==1:
        return "sentence"
    elif len(string) >1 and 1>= (dot + pun) >= 0:
        return "word"
    elif (dot + pun) ==1 or len(string)==1:
        return "character"
    else:
        return "empty"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#empty
#character
#word
#sentence
#paragraph
#page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))
