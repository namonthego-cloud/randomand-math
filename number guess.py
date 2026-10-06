import random #importing module
playing = True
number = str(random.randint(0,9)) #random in built in function

print("I will genrate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("THe game ends when you get one hero!")
#itrate loop till the condtion is true
while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game!")
        print("the number was",number)
        break

    else:
        print("c'mon your guess is wrong,try again. \n")