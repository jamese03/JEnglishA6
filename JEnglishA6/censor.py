import os
import sys

def function(func):
  file = input("Enter the file you would like to censor ")
  if not os.path.isfile(file):
     print("File does not exist, exiting")
     sys.exit()
  report = open(file, 'r')
  censor = open('censor.txt', 'w')
  for line in report:
    censor.write(line.replace(func, '#%$'))
  report.close()
  censor.close()

