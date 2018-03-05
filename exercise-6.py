'''
Exercise 6 
Joan Healy
5/3/2018
'''

def factorial(x):
  counter = 1
  if x > 0:
    for each in range(1,x+1):
      counter = each * counter
  return counter
    
print(factorial(5))
print(factorial(7))
print(factorial(10))

