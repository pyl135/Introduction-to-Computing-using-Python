#Here's a long one -- you can do it!
#
#Rewrite the following class so that it uses getters and
#setters for all three variables (title, description,
#completed). The getters should be called: getTitle,
#getDescription,  getCompleted. The setters should be
#called: setTitle, setDescription, setCompleted.
#
#Whenever a getter is called, the method should print
#"<attribute name> accessed". For example, when calling
#getTitle(), the program should print "title accessed".
#
#Whenever a setter is called, the method should print
#"<attribute name> changed". For example, when calling
#the method setCompleted(True), the program should print
#"completed changed".
#
#In addition, the setter should check to make sure that
#the new value is the correct type: title and description
#should always be of type str, and completed should always
#be of type bool. If the value is not the right type,
#print "invalid value" in addition to "<attribute name>
#changed", and set the value of the corresponding
#attribute to None (the keyword, not the string "None").
#
#Note that when assigning variables their initial values
#inside the constructor, you should use the getters and
#setters, not modify the variables directly.
#
#To summarize (and give a to-do list):
# - Create getters and setters for each variable.
# - Print a log statement when the getters and setters
#   are called.
# - Check the type of the new value inside the setters,
#   and print an error if it's the wrong type.
# - Modify the constructor body to use the getters and/or
#   setters instead of assigning values directly.
#
#See the bottom of the code for hints!

class TodoItem:
    def __init__(self, title, description, completed=False):
        self.setTitle(title)
        self.setDescription(description)
        self.setCompleted(completed)

    def getTitle(self):
        print("title accessed")

    def getDescription(self):
        print("description accessed")

    def getCompleted(self):
        print("completed accessed")

    def setTitle(self, title):
        if type(title) == str:
            self.title = title
        else:
            print("invalid value")
            self.title = None
        print("title changed")

    def setDescription(self, description):
        if type(description) == str:
            self.description = description
        else:
            print("invalid value")
            self.description = None
        print("description changed")

    def setCompleted(self, completed):
        if type(completed) == bool:
            self.completed = completed
        else:
            print("invalid value")
            self.completed = None
        print("completed changed")
                 
#Feel free to write code below to test the class you've
#written above!
myTest = TodoItem("Super", "trying")
myTest.setTitle("How are you")


#Hint: You will need to change the body of the constructor
#and add six new methods to this class, but you should not
#need to change the header of the class or the constructor.
#
#Hint 2: You can check to see if a variable is a string by
#checking the logical expression type(var) == str, where
#var is the variable you're checking. For integers, use
#int instead of str. For floats, use float. For booleans,
#use bool.
#
#Hint 3: Remember to put self before any instance variables
#or methods you're trying to access. For example, to access
#the method setTitle from within the constructor, you would
#need to write self.setTitle().
