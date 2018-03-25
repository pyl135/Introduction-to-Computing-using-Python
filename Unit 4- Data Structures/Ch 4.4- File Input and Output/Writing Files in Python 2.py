#Write a function called "append_to_file" that accepts
#two parameters: a filename and some data that will
#be an integer or a string to write. The function 
#should open the file and add the data to the end of
#the file. Before adding anything to the file, your
#function should also add two linebreaks to the file.
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
# - Your output should not add any lines besides the
#   ones described above -- be careful if you're
#   using print() instead of write()! If you want to
#   use print(), how do you avoid having it add that
#   extra line?


#Write your function here!
def append_to_file(name,data):
    output= open(name, "a")
    print("\n\n" + str(data), end='' ,file=output)
  #  output.write("\n\n"+ str(data))
    
    
    output.close()

#To test your code, call your function with the
#filename AppendToFileOutput.txt. You'll find this
#file available in the drop-down box in the top left
#of this programming widget, so you can check what
#your code outputs by looking at that file! You can
#also change this file manually if you want to reset.
#
#Uncomment this line to try that out:
append_to_file("AppendToFileOutput.txt", 123)
