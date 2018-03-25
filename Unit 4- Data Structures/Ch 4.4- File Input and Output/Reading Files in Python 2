#Write a function called "load_file" that accepts one 
#parameters: a filename. The function should open the
#file and return the contents. If the contents of the
#file is an integer, it should be returns as an
#integer; otherwise, it should be returned as a string.
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right!
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def load_file(name):
    output= open(name,"r")
    content = output.read()
    #print(content)
    #print(content.isdigit())

    if content.isdigit()==True:       
        return int(content)
    else:
        return content
    
    output.close()

#To test your code, call your function with the
#filename LoadFromFileInput.txt. You'll find this file
#available in the drop-down box in the top left of
#this programming widget, so you can check what your
#code outputs by looking at that file!
#
#Uncomment this line to try that out:
print(load_file("LoadFromFileInput.txt"))
