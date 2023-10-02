def main():
  
  #set this to any double
  doubleValue = 7.273182
  
  #set this to any int
  intValue = 4
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  
  
  #populate this list
  myFriends = ["me", "myself", "I", "Jonathan", "Danny"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [7, 8, 4, 3, 2]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0]+fiveNumbers[3])
  print(fiveNumbers[1]-fiveNumbers[2])
  print(fiveNumbers[3]/fiveNumbers[4])
  print(fiveNumbers[4]*fiveNumbers[1])
  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[0] = 10
  fiveNumbers[2] = 9
  #print out the list
  print(fiveNumbers)
  
main()
