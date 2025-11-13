play=True 

while play:
  import random as rd
  numbers=[]
  magic_number= rd. randint(1,100)
  
  guess=int(input("what is your guess?"))
  counter=6
  
  while guess != magic_number and counter > 0 :
    counter-=1
    numbers.append(guess)
    print("your already guessed %s " % (counter))
    if magic_number<guess:
      print("try lower number")
    if magic_number>guess:
      print("try a higher number")
    print("you have %d gueses left" % (counter))
    if counter==0:
      print("gameover")
      print("would you like th play another round")
      response=input("y/n")
      if response == "y":
        attempt=1
        print("okay round"+str(attempt))
    else:
      guess=int(input("try again:"))
      
  if guess==magic_number:
    print("you win!")
    wins+=1
  if guess==magic_number or counter==0:
   attempt+=
    print("SCOREBOARD")
    print("----------")
    print("would you like to play another round?")
    
    Print("would you like to play another round?")
    response=input("y/n")
    
    if response == "y"
    
    os.system("cls")
    round+=1
    print("okay round"str(round))
    else:
      play=false 
      print("bye bye")
   
