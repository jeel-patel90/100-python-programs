import random as r

options = ("rock", "paper", "scissors")
player = None
computer = r.choice(options)
while player not in options:
    player = input("Enter your choice (Rock, Paper, Scissor) : ")

print(f"Player : {player}")
print(f"Computer : {computer}")

if(player == computer):
    print("This game is tie, Play it again...")
elif(player == "rock" and computer == "scissors"):
    print("Congrats jeel, You win !!")
elif(player == "paper" and computer == "rock"):
    print("Congrats jeel, You win !!")
elif(player == "scissors" and computer == "paper"):
    print("Congrats jeel, You win !!")
else:
    print("Oh no man!! You loose")   
