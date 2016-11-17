def calc():
#  print("Welcome to the atm!")
  f=open("balance",'r')
  for line in f:
    bal=line
  bal=bal.strip()
  y=int(bal)
  f.close()
  return(y)
  
  #Now we have the balance as y

def add(b):
  a=input("How much would you like to deposit to the balance? ")
  ba = repr(int(b)) + repr(int(a))
  nums=[int(b),int(a)]
  ba = sum(nums)
  w=open("balance",'w')
  w.write(repr(ba))
  w.close()
  return(int(ba))

def sub(b):
  a=input("How much would you like to withdraw from the balance? ")
  nums=[int(b),-int(a)]
  ba=sum(nums)
  w=open("balance",'w')
  w.write(repr(ba))
  w.close()
  return(int(ba))

def bcheck():
  f=open("balance", 'r')
  for l in f:
    nb=l
