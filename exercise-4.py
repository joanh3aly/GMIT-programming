'''
Week 5 - Project Euler Problem 5
Joan Healy
19/2/2018
'''
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# initialise counter variable with a very large number
counter = 999999999
# initialise empty array
checkList = []
  
# create loop from 0  
while counter > 0:
  # make sure our array is empty
  checkList.clear()
  # Loop through numbers 1-20, starting from index 1
  for i in range(1,21):    
    # Use modulo to check to see if number represented by 'counter' has a remainder when divided by i and is therefore an even number
    if counter % i == 0:
      # If no remainder, number is even, so insert 1 into checklist array at index i 
      checkList.insert(i,1)
      # Check to see if the value 1 occurs at every index in the list
      if checkList.count(1) == 20:
        # If all indexes are 1, or 'true', then each number represented by i can be evenly divided into the number represented by counter
        print("answer ", checkList, "counter ", counter) 
    else:    
      # If counter is odd, exit  
      break
  # reduce the counter by 1 before going through the next iteration of the loop
  counter = counter-1 


     

