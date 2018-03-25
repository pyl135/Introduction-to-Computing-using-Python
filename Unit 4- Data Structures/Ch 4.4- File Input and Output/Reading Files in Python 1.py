#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: the file.read() method will return the entire
#contents of the file as one big string. You can use that
#to make this simpler instead of using readline().


#Write your function here!
def find_coffee(name):
    output = open(name, "r")
    word = output.read()
    if not word.find("coffee")== -1:
        return True
    else:
        return False


#You can test your function with the provided files named 
#"coffee.txt" and "nocoffee.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffee.txt"))
print(find_coffee("nocoffee.txt"))
