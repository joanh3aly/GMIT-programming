# Joan Healy - Exercise 3 
# Collatz conjecture program
# 8/2/2018

# Input a number and store in 'number' variable
number = input('Enter a number: ')
# Change number from string to integer datatype
number = int(number)

# Loop starting from the number inputted to 1
while number > 1:
    # Check to see if number is even, by using modulus operator to see if there is no remainder
    if number % 2 == 0:
        # If even, divide by 2
        number = number / 2
        print(number)
    # If not even, check to see if number is odd, by using modulus operator to see if the remainder is 1   
    elif number % 2 == 1:
        # If odd, multiply by 3 and add 1
        number = (3 * number) + 1
        print(number)
