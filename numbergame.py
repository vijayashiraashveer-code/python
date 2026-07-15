from random import randint

n = str(randint(0,9))
print("guess a number from 0 to 9")
while input("your guess")!=n:
  print("wrong try again!")

print("you win!")
print("the number was",n)