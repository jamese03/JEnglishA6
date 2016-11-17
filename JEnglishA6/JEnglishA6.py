#James English
#Assignment 6


import sys
import os
import palindrome
import censor
import atm
import anagram

def quit():
  print("Script exiting, goodbye")
  sys.exit


options = {1 : palindrome,
	   2 : censor, 
           3 : atm,
           4 : anagram,
           5 : quit
}


for x in options: 
	print(x, options[x].__name__)
choice = input("Enter a choice between 1 - 5 ")
choice = int(choice)


if choice == 1:
  palindrome.function()

elif choice ==2:
  word = input("Enter the word you would like to censor ")
  censor.function(word)
  print("Check censor.txt to see that your word has been censord")

elif choice == 3:
    b=atm.calc()
    print("Your balance is currently " + repr(b))

    bm = {}
    bm['1']="Check Your Balance"
    bm['2']="Deposit Money "
    bm['3']="Withdraw Money"
    bm['4']="Quit"

    while True:
      o=bm.keys()
      for e in o:
        print(e, bm[e])
      cho=input("Select Bank Function:")
      if cho == '1':
        print("")
        b=atm.calc()
        print("Your Current balance is " + repr(b))
        print("")
      if cho =='2':
        print("")
        b=atm.add(b)
        print("Your new balance is " + repr(b))
        print("")
      if cho == '3':
        print("")
        b=atm.sub(b)
        print("your new balance is " + repr(b))
        print("")
      if cho == '4':
        print("Exit")
        sys.exit()

elif choice == 4:
  def anagrams(word):
      """ Generate all of the anagrams of a word. """ 
      if len(word) < 2:
          yield word
      else:
          for i, letter in enumerate(word):
              if not letter in word[:i]: #avoid duplicating earlier words
                  for j in anagrams(word[:i]+word[i+1:]):
                      yield j+letter 

  if __name__ == "__main__":
    word = input("Enter the word you would like to see the anagram of ")
    for i in anagrams(word):
        print(i)

elif choice == 5:
  quit()
