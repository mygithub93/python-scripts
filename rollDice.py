import random
choice = raw_input("Do you want to roll dice (Y/N)? ")
while ( choice == "Y"):
  print(random.randint(1,6))
  choice = raw_input("Do you want to roll a dice again (Y/N)? ")