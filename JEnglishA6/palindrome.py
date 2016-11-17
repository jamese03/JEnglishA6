# Program to check if a string
#  is palindrome or not
import re

def function():
# take input from the user
  my_str = input("Enter a string to check if it is a palindrome: ")

# make it suitable for caseless comparison
  my_str = my_str.casefold()

#regular expression to remove special characters like !
  my_str = re.sub(r'\W+', '', my_str)

# reverse the string
  rev_str = reversed(my_str)


# check if the string is equal to its reverse
  if list(my_str) == list(rev_str):
     print("It is palindrome")
  else:
     print("It is not palindrome")                                       
