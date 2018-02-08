# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

'''
Output of Exercise 1:~
My name is Joan, so the first and last letter of my name (J + N = 10 + 14) give the number 24. The 24th Fibonacci number is 46,368. 

Output of Exercise 2:~
My surname is Healy
The first letter H is number 72
The last letter y is number 121
Fibonacci number 193 is 9663391306290450775010025392525829059713

The ord() method returns an integer representing the Unicode code point of the given Unicode character.
'''

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Healy"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
