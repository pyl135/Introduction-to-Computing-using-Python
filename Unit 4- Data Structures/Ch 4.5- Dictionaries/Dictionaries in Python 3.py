#Write a function called mostOscars, which takes in one
#parameter, a dictionary. This dictionary maps actor/actress
#names to the number of Academy Awards they have won. This
#function should return a tuple containing the name and
#number of awards of the actor/actress who has won the most.
#You may assume there will not be a tie for the actor with
#the most (although there may be other ties in the list).


#Write your function here!
def mostOscars(file):
    dict = file
    current_time = 0
    actor = ""
    for (name, time) in dict.items():
        if time > current_time:
            current_time = time
            actor = name
    return (actor,current_time)

#The code below will test your function. It isn't needed for
#grading, so feel free to modify it. As written, it should
#print out: ('Jennifer Lawrence', 1)
winners = {'Bette Davis': 2, 'Katharine Hepburn': 4, 'Jane Fonda': 2, 'Cate Blanchett': 2, 'Ingrid Bergman': 3, 'Meryl Streep': 3}
print(mostOscars(winners))
