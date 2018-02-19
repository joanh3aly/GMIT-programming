'''
Week 5 - Project Euler Problem 5
Joan Healy
19/2/2018
'''

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

counter = 999999999 
checkList = []
  
while counter > 0:
  checkList.clear()
  for i in range(1,21):    
    if counter % i == 0:
      checkList.insert(i,1)
      if checkList.count(1) == 20:
        print("answer ", checkList, "counter ", counter) 
    else:      
      break
  counter = counter-1 

