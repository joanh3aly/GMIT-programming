'''
Exercise 6 - get factorial of number
Joan Healy
5/3/2018
'''

# Create factorial function
def factorial(x):
  # Initialise counter to 1
  counter = 1
  # Condition whereby if the function's argument is greater than 1 run code
  if x > 0:
    # Loop from 1 to 1 plus the function's argument 'x', (as we want to start from 1 not the default 0)
    for each in range(1,x+1):
      # multiply each iteration of the loop (all of the positive numbers less than x) by the counter and update counter to the result
      counter = each * counter
  # return the result of counter
  return counter

# Print the factorial function of 5, 7 and 10 by calling the factorial function with each of these numbers as arguments   
print(factorial(5))
print(factorial(7))
print(factorial(10))
