# import modules
import random
import time
import asyncio
import tkinter as tk



# set random number and print intro
print("Let's play a game. I'm thinking of a number between 1 and 1 million. i will give you clues on how what the answer is (answer is not a decimal!)\n")
ranum = random.randint(1,1000000)
tries = 0
print(ranum)

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
sees = input("Would you like to see your previous scores? yes or no\n")
if sees == "yes":        
    f = open("scores.txt", "r")
    print(f.read())

else:
    print("ok")

time.sleep(120)
print("poo")
    
# loops program
loop = asyncio.get_event_loop()
try:
    loop.run_forever()
finally:
    loop.close()
