import random as rd

counter = 2
magic_number = rd.randint(1,10)
print(magic_number)

guess = int(input("Guess a number between 1 and 10:"))

while guess != magic_number and counter > 0:
  counter-= 1
  print("You lose !")
  print("You have %s guesses left." % (counter))
  guess = int(input("Guess a number between 1 and 10"))
else:
    print("You win!")
  
