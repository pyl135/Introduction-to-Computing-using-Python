#Write a function called "write_file" that accepts two 
#parameters: a filename and some data that will either 
#be an integer or a string to write. The function 
#should open the file and write the data to the file.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - If the data isn't a string already, you may need
#   to convert it.
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right! You could add print statements if
#   you want a confirmation the code is done running.
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def write_file(name,data):
    output= open(name,"w")
    
    output.write(str(data))
                 
    output.close()



#To test your code, call your function with the
#filename WriteFileOutput.txt. You'll find this file
#available in the drop-down box in the top left of
#this programming widget, so you can check what your
#code outputs by looking at that file!
#
#Uncomment this line to try that out:
write_file("WriteFileOutput.txt", 123)
