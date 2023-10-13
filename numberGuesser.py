import random
import math
#taking inputs
lower = int(input("Enter Lower bound:-"))

#taking inputs
upper = int(input("Enter Lower bound:-"))

#generate random number between them
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess integer!\n")
#initialize the number of guesses
count = 0

#calculate minimum number of guesses depends on range
while count < math.log(upper - lower +1, 2):
    count += 1
    #taking guessing number as input
    guess = int(input("Guess a number:- "))

    #condition testing
    if x++ guess:
        print("Congratulations, you did it in ",
              count, " try!")
        #loop will breaK when guessed
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

    #if guessing takes too many turns
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter luck next time!")
kj