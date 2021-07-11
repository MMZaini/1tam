# import modules
import random
import time



# set random number and print intro
print("Let's play a game. I'm thinking of a number between 1 and 1 million. i will give you clues on what the answer is or is not! (answer is not a decimal!)\n")
ranum = random.randint(1,1000000)
tries = 0

# print(ranum)

# checks if answers are correct
while True:
    
    ans = int(input())
    tries += 1
    if ans == ranum:
        print("Congratulations! You got the correct answer! The answer was", ranum, "and it took you", tries, "tries!")
        break

    if ans < ranum:
        print("Incorrect. Try again. The correct answer is higher.")

    if ans > ranum:
        print("Incorrect. Try again. The correct answer is lower.")
# writes the scores in a txt
f = open("scores.txt", "a")
f.write(f"It took you {tries} tries and the correct answer was {ranum}\n")
f.close()
# asks to see scores and prints it
vs = input("Would you like to see your previous scores? yes or no\n")
if vs == "yes":        
    f = open("scores.txt", "r")
    print(f.read())
time.sleep(1)
input("Press enter 3x to exit program")
input("Press enter 2x to exit program")
input("Press enter 1x to exit program")
