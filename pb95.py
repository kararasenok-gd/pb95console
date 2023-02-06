import random
from os import system as sys

score = 0
errors = 0
segments = ['red','blue','blue','orange','orange','pink','gray']

system = input('Select OS:\n1. Windows\n2. Linux/Termux')

if system == '1':
    sys('cls')
elif system == '2':
    sys('clear')

while True:
    print('Welcome to ProgressBar95 in console!\nVersion: 0.1b')
    print('Menu:\n1. Start\n2. Quit')
    menu = input('>>>')
    if system == '1':
        sys('cls')
    elif system == '2':
        sys('clear')
    if menu == '1':
        score = 0
        errors = 0
        while score <= 99:
            segment = random.choice(segments)
            
            if system == '1':
                sys('cls')
            elif system == '2':
                sys('clear')
            
            if segment == 'red':
                print('Segment: Red')
                print(f'scores: {score}')
                answer = input("Skip [s] | Take [t]")
                
                if answer == "t":
                    if system == '1':
                        sys('cls')
                    elif system == '2':
                        sys('clear')
                    print("You lose!")
                    break
                elif answer == 's':
                    print("you skipped!")
            if segment == 'blue':
                print('Segment: Blue')
                print(f'scores: {score}')
                answer = input("Skip [s] | Take [t]")
                
                if answer == "t":
                    print("+5%")
                    score += 5
                elif answer == 's':
                    print("you skipped!")
            if segment == 'orange':
                print('Segment: Orange')
                print(f'scores: {score}')
                answer = input("Skip [s] | Take [t]")
                
                if answer == "t":
                    print("+5% (error)")
                    score += 5
                    errors += 5
                elif answer == 's':
                    print("you skipped!")
            if segment == 'pink':
                print('Segment: Pink')
                print(f'scores: {score}')
                answer = input("Skip [s] | Take [t]")
                
                if answer == "t":
                    print("Minus!")
                    score -= 5
                elif answer == 's':
                    print("you skipped!")
            if segment == 'gray':
                print('Segment: Gray')
                print(f'scores: {score}')
                answer = input("Skip [s] | Take [t]")
                
                if answer == "t":
                    print("+0%")
                elif answer == 's':
                    print("you skipped!")
        
        if system == '1':
            sys('cls')
        elif system == '2':
            sys('clear')
        
        print('You win!')
        print(f'Loaded: {score-errors}% | Errors: {errors}%')
        if errors <= 0:
            print('Nice!')
    elif menu == '2':
        input('Press ENTER to quit')
        quit()
