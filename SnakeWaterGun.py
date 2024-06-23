import random

print("\n")
print("                          Let's get started")
print("\n")
print("======================= Snake🐍 Water🌊 Gun🔫 ===========================")
print("\n")
                        
print("\n \n \t \t \t      Snake🐍 \n \n \t \t \t ↙ \n \n \t \t Water🌊              ↖ \n \n \t \t \t    ↘ \n \n \t \t \t \t     Gun🔫")

print("\n\n")
print("Enter : \n \t \t \t 0 for Snake🐍 \n \t \t \t 1 for Water🌊 \n \t \t \t 2 for Gun🔫")

you = int(input("\n \n \t \t ➡   You : "))

computer = random.randint(0,2)

print("\n \n \t \t ➡   Computer : " , computer)


if computer == 0 and you == 1 :
    print("\n \n \t \t    Ohhh You lost ❌")
    print("\n \n \t \t    Computer Won")
elif computer == 0 and you == 2 :
    print("\n \n \t \t Congrates!! 🥳 🎊")
    print("\n \n \t \t    You Won")
elif computer == 1 and you == 0 :
    print("\n \n \t \t Congrates!! 🥳 🎊")
    print("\n \n \t \t    You Won")
elif computer == 1 and you == 2 :
    print("\n \n \t \t    Ohhh You lost ❌")
    print("\n \n \t \t    Computer Won")
elif computer == 2 and you == 0 :
    print("\n \n \t \t    Ohhh You lost ❌")
    print("\n \n \t \t    Computer Won")
elif computer == 2 and you == 1 :
    print("\n \n \t \t Congrates!! 🥳 🎊")
    print("\n \n \t \t    You Won")
else :
    print("\n \n \t \t     Ohhh Nooo 🙀")
    print("\n \n \t \t    Tie the GAME")

print("\n\n")
