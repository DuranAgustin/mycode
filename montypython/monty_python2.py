#!/usr/bin/env python3

round = 0
answer = " "
while round < 3 and (answer!= "brian" and answer!="shrubbery"):
    
    round +=1
    
    print(''' Finsh the movie title, "Monty Python's the life of _____"''')
    
    answer = input("your guess -->: " )
    
    answer = answer.lower()
    
    if answer == 'brian':
        print("Correct!")
    elif answer == 'shrubbery':
        print("You gave the super secret answer!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry, try again.\nChances left ",(3-round))
    
