# Joan Healy - Exercise 3 
# Collatz conjecture program
# 8/2/2018

number = input('Enter a number: ')
number = int(number)

while number > 1:
    if number % 2 == 0:
        number = number / 2
        print(number)
    elif number % 2 == 1:
        number = (3 * number) + 1
        print(number)
