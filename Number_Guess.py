##This script is write for Number Guess
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess
  
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The max value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "No guessing higher than the maximum possible value!"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is %d" % first_roll
    sleep(1)
    print "The 2ed roll is %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total roll is %d" % total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
        print "YOU WIN!"
    else:
        print "you lost, try again"
    
roll_dice(56)
