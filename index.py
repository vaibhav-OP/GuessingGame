import math
import random

# runs the code until user types any other key then 0
while True:
    flag = input("press 0 to play and any other key to stop: ")

    if flag == "0":
        # generates two random numbers
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)

        # calculates the answer
        correct_answer = num1 + num2
        # takes answer from user
        user_answer = int(input("What is sum of {} and {}: ".format(num1, num2)))

        # condition to check the answer
        # prints accordingly
        if(user_answer == correct_answer):
            print("{} is correct.".format(user_answer))
        else:
            print("{} is wrong, {} was the correct answer.".format(user_answer, correct_answer))
    else:
        break

# does not close the app immediately.
input("Press Enter to exit.")