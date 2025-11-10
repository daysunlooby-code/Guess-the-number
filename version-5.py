mport random as rd
numbers=[]
magic_number= rd. randint(1,100)
# print(magic_number)
guesseint input("what is your guess?:"") counter=6
while guess 1= magic_number and counter > 0 :
counter -=1
numbers append (guess)
print("your already guessed
%S " % (numbers))
if magic_number guess:
print("try a lower number")
if magic_number>guess:
print("try a higher nukber")
print("you have %d guesses left" % (counter))
if counter=0:
print ("gameover")
else:
guess=int (input ("try again:"))
if
guess= magic number:
print("you win!")
