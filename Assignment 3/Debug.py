def main():

    #Can you print out "Hello" 8 times? I gave you a tiny hint to start...
    #dan-notes, for x in range(8)
    for x in range(8):
        print("Daniel")



    #What about as a while loop?
    name = "Daniel"
    loops = 0
    while (loops < 9):
        print(name)
        loops = loops + 1

    
    #The loop iterations are one behind in a non-programming counting way... how can we fix this?
    #dan-notes, if we want to count in a real world way change count start to 1 I assume?
    count = 1
    while (count < 3):   
        print("While loop iteration", count)
        count = count + 1
        
    #Same deal here!

    for x in range(3):

        print("For loop iteration:", x+1)

     
    #Uh oh I messed up and made an infinite loop... so silly of me!   
    endless = 4    
    while (endless < 5):
        print("I'm stuck in this loop!!!!")
        endless = endless + 1
    
    #print out your last name one letter at a time
    lastName = "Narewski"
    for x in lastName:
        print(x)

     #aw i suck i made another infinite loop.. use that thing I taught you about to get out once it prints once... starts with a b... br....
    found = False
    while found == False:
        print("i only printed once")
        break


    #can you fill this out so that it prints found when it hits the letter r?
    letter = "r"
    for x in "Marist":
        if x == letter:
            print(x,"found")
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    #you could print out the list using print(numbers) OR you could go the long way and use a for loop to print out the value of each index :)
    for x in numbers:
        print(numbers[0])
    
    #what if I wanted you to print out only the even numbers in this range I made?
    for x in range (20, 501):
        #i feeeeel like modulooooooo is neededddd
        if x % 2 == 0:
            print(x)

main()
