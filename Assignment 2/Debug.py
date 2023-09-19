#instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix them. (Run them yourself and see what the output is!)
#also, we have some input practice!

def main():
    
    #this is a nice solid working one!
    name = input("your name is? ")
    print("Hello, ", name)

    #this isn't printing anything :( so sad. what's wrong with her? Why she not printing out?
    #dan-notes, requires a print statement to output to or sum like that
    color = input("what's your favorite color? ")
    print("My favorite color is: ", color)
    
    #I thought i did this right :( can you fix it for me?
    #dan-notes, seems to work already, but to be safe do the str(age) check to make sure you're working with a string
    age = input("how old are you? ")
    print("You are " + str(age) + " years old")
	
    #Start with this one! We have a compilation error :(
    #Side note: you can put these statements in parentheses or not. it's up to you.
    #dan-notes, requires colon : at end of if statement
    if (5 > 3):
        print("5 is greater than 3")
    
    #There are multiple correct answers and adjustments to this one
    #dan-notes, seems to work fine, but to be proper should cover condition for elif 5 equal to 5
    isFive = 5
    if isFive > 5:
        print("isFive is greater than 5")
    elif isFive == 5:
        print("isFive is equal to 5")
    else:
        print("isFive is less than 5")

    #more multiple correct answers. Similar to the first. Adjust as perceived
    '''dan-notes, clarify some of the prints, make first two ifs check for equality as well, specific condition for 4,
    everything else should be covered then make else: be an error check or something'''
    toCheck = 4
    if toCheck >= 5:
        print(toCheck, "is greater than or equal to 5.")
    elif toCheck <= 3:
	    print(toCheck, "is less than or equal to 3")
    elif toCheck == 4:
        print(toCheck, "is equal to 4")
    else:
        print("not a number, try again")

    #Is it really printing the BEST option though? Rearrange these as you see fit
    #dan-notes, have prints output actual variables, check equal to 5 first
    toCheck = 5
    if toCheck == 5:
        print(toCheck, "is 5")
    elif toCheck > 7:
        print(toCheck,"is greater than 7")
    elif toCheck < 6:
        print(toCheck, "is less than 6")
    else:
        print("toCheck is invalid")
    
    
    
    
main()
