import os
import math
import time
import random
operator = ["+", "-", "/", "*"]
min_operand = 2
max_operand = 12
total_problems = 10
score = 0


def generateproblems():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operand = random.choice(operator)
    expression = str(left) + "" + operand + "" + str(right)
    answer = eval(expression)
    return expression, answer


print("----------------------------")
input("Press enter to start : ")
print("----------------------------")
start_time = time.time()
for i in range(total_problems):
    expression, answer = generateproblems()
    print(expression)
    while True:
        guess = input(f"Enter the answer for Question{str(i+1)} : ")
        if guess == str(answer):
            score += 1
            print(f"current score = {score}")
            print("you got that one right, congratulations!!!!")
            break
        else:
            print("Wrong answer , better luck next time")
            break
end_time = time.time()
total_time = end_time - start_time


print(f"Your score was : {score}")
print("----------------------------")
print("Gameover Thankyou for playing")
print("----------------------------")
print(f"Your total time was {round(total_time, 2)} seconds ")
