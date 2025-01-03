name = "jeel"
question = "Will i be succesfull in the field i admired ?"
answer = ""

import random

random_number = random.randint(1, 9)


## used if else statment for the required answers

if (random_number == 1):
    answer = "YES - definetly"
elif(random_number == 2):
    answer = "It is decidedly so"
elif(random_number == 3):
    answer = "without a doubt"
elif(random_number == 4):
    answer = "Reply hazy, try again"
elif(random_number == 5):
    answer = "Ask again later"
elif(random_number == 6):
    answer = "Better not tell you now"
elif(random_number == 7):
    answer = "My sources say no"
elif(random_number == 8):
    answer = "Outlook not so good"
elif(random_number == 9):
    answer = "Very doubtful"
else:
    print("The number is not applicable")

print(name , "asks : ")
print(question)
print("magic ball 8's answer : " , answer)

