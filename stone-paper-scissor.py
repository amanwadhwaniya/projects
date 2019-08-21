import random
list = ['st','p','sc']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Stone , Paper , Scissor")
print("st for stone \np for paper \nsc for scissor")

#making game in the while
while no_of_chance < chance:
    _input = input('Stone,Paper,Scissor: ')
    _random = random.choice(list)

    if _input == _random:
        print("Tie both 0 points \n")

    #if user enters st
    elif _input == "st" and _random == "p":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random} \n ")
        print("Computer wins 1 point \n ")
        print(f"computer point is {computer_point} and human point is {human_point}")

    elif _input == "st" and _random == "sc":
        human_point = human_point + 1
        print(f"your guess is {_input} and computer guess is {_random} \n ")
        print("Human Wins 1 point \n ")
        print(f"Computer point is {computer_point} and human point is {human_point}")

    #if user enters p
    elif _input == "p" and _random == "st":
        human_point = human_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}")
        print("Human Wins 1 point \n ")
        print(f"Computer point is {computer_point} and human point is {human_point}")

    elif _input == "p" and _random == "sc":
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}")
        print("Computer wins 1 point \n ")
        print(f"Computer point is {computer_point} and human point is {human_point}")

    #if user enters sc
    elif _input == "sc" and _random == "p":
        human_point = human_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}")
        print("Human wins 1 point \n ")
        print(f"Computer point is {computer_point} and human point is {human_point}")

    elif _input == "sc" and _random == "st":
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random}")
        print("Computer wins 1 point \n ")
        print(f"Computer point is {computer_point} and human point is {human_point}")

    else:
        print("You have wrong input")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game Over")

if computer_point > human_point:
    print("Computer wins and you loose")

if computer_point < human_point:
    print("you win and computer losse")

print(f"your point is {human_point} and computer point is {computer_point}")
