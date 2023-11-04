#if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
#this script is going to require some googling: I want you to practice using your resources with this one. But of course if you get stuck, reach out :)
'''instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an 11 as one of the values, return the sum - 10. '''
import random

def rng():
    return random.randrange(1, 11, 1)

def bust(x,y,z):
   return x + y + z


def main():
    num1 = rng()
    #num1 = 11, tested to see if first if statment works
    num2 = rng()
    num3 = rng()

    result = bust(num1,num2,num3)

    if num1 == 11 or num2 == 11 or num3 == 11:
        print("There was an ace",result - 10)
    elif result <= 21:
        print("Your number is:",result)
    elif result > 21:
        print("Too high:",0)
    else:
        print("GG")



main()
