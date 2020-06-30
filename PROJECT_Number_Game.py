#Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. 
#Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced. 

import random

def guess_num_game ():
  
  x = random.randint(0,21)
  life = 5

  print "Let's get ready to play! \n"
  print "I've chosen a secrete whole number between 0 and 20."
  print "You will have 5 lives equivalent to 5 chances to guess. If you get it wrong, one life is deducted and you will unfortunately lose the game if you have no life left. I will give you hint each time, however! \n"

  guess_number = int(raw_input ("Give me a number between 0 and 20: "))


  while guess_number not in range (0,21):
    guess_number = int(raw_input ("Please only give me a number between 0 and 20: "))


  while guess_number != x:
      if life <= 0:
        break
      
      elif guess_number - x > 0:
        print "Uhm, my number is SMALLER than your guess."
        life -= 1
        print "Number of lives left: ", life, "\n"
        guess_number = int(raw_input ("Why don't you guess a new number? Type here: "))
        while guess_number not in range (0,21):
          guess_number = int(raw_input ("Please only give me a number between 0 and 20: "))
      
      elif guess_number - x < 0:
        print "My number is BIGGER than your guess."
        life -= 1
        print "The number of lives you have left is: ", life, "\n"
        guess_number = int(raw_input ("Why don't you guess a new number? Type here: "))
        while guess_number not in range (0,21):
          guess_number = int(raw_input ("Please only give me a number between 0 and 20: "))

  else:
    print "That's crazy! Great minds think alike! You won - Congrats!"


  if guess_number != x:
    print "\nThere's no more life left :("
    print "The number I have in mind was:", x,"!"

guess_num_game ()



















#======
#Attempt that didn't work because there wasn't a break in the while loop to stop when the number of lives is negative
#======
# while guess_number != x:
#   if life >= 0:
#     if guess_number - x > 0:
#       print "Uhm, my number is SMALLER than your guess."
#       life -= 1
#       print "Number of lives left: ", life
#       print
#       guess_number = int(raw_input ("Why don't you guess a new number? Type here: "))
#     if guess_number - x < 0:
#       print "Uhm, my number is BIGGER than your guess."
#       life -= 1
#       print "The number of lives you have left is: ", life
#       print
#       guess_number = int(raw_input ("Why don't you guess a new number? Type here: "))
#   else:
#     print ":( Game over" 
#   #This else statement is INSIDE the WHILE loop, which will run for as long as guess_number is NOT equal to x.
#   #Hence if the user guesses incorrectly at the 5th time, the WHILE loop will keeps running and printing out endless lines of ":( Game over"
# else:
#   print "That's crazy! Great minds think alike! You won - Congrats!"

#======
#Attempt that didn't work because there wasn't any loop/repetition to tell the program to keep going until the right answer is right or until there's no life left.
#======
# if guess_number = x:
#   print "Amazing, you are right!"
# else:
#   if guess_number - x > 0:
#     print "Good start! My number is SMALLER than your guess."
#     life -= 1
#     print "The number of lives you have left is: ", life
#   else:
#     print "Good start! My number is BIGGER than your number."
#     life -=1
#     print "The number of lives you have left is: ", life
#   guess_number = raw_input ("Why don't you guess a new number: ")