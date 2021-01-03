q = "   O "
w = " --|--" 
e = "   | "
r = " _/ \_"

#states
"""
   O 
 --|--
   | 
 _/ \_

   O 
 --|--
   | 


   O 
 --|--
   | 

   O 
 --|--

   O
"""
hangManFull = (q+"\n"+w+"\n"+e+"\n"+r)
hangManone = (q+"\n"+w+"\n"+e+"\n")
hangMantwo = (q+"\n"+w+"\n"+e)
hangManthree = (q+"\n"+w)
dead = (q)

guessedButWrongChar = ""
failCount = 0
guess = "_ _ _ _ _"
word = "yummy"

while True:
  print(guess)
  print("")
  guessinput = input("Guess: ")
  if guess == "yummy":
    print("You win!")
    break
  elif guess:
    if failCount > 3
    print("try again.")
    failCount += 1
    if failCount == 3:
      print("you lose")
      break
      
  

