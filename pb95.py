import random
from os import system as sys

score = 0
errors = 0
segments = ['red','blue','blue','orange','orange','pink','gray']
noclip = False
scores = 0
scores_boost = 1
BSoD_fix = False
errors_fix = False

system = input('Select OS:\n1. Windows\n2. Linux/Termux')

def clear_screen():
    if system == '1':
        sys('cls')
    elif system == '2':
        sys('clear')

if system == '1':
    sys('cls')
elif system == '2':
    sys('clear')

while True:
    print(f'Welcome to ProgressBar95 in console!\nVersion: 0.2b\n\nScores: {scores}')
    print('Menu:\n1. Start\n2. Quit\n3. Settings\n4. Clear screen\n5. Shop')
    menu = input('>>>')
    clear_screen()
    if menu == '1':
        score = 0
        errors = 0
        while score <= 99:
            segment = random.choice(segments)
            
            clear_screen()
            if noclip is False:
                if segment == 'red':
                    print('Segment: Red')
                    print(f'scores: {score}')
                    answer = input("Skip [s] | Take [t]")
                    
                    if answer == "t":
                        if BSoD_fix is False:
                            if system == '1':
                                sys('cls')
                            elif system == '2':
                                sys('clear')
                            print("You lose!")
                            break
                        else:
                            BSoD_fix = False
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
                    if errors_fix is False:
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
                    
        if score >= 100:
        
            clear_screen()
            errors_fix = False
            print('You win!')
            print(f'Loaded: {score-errors}% | Errors: {errors}%')
            scores += 500*scores_boost
            if errors <= 0:
                scores += 250*scores_boost
                print('Nice!')
                
    elif menu == '2':
        input('Press ENTER to quit')
        quit()
    elif menu == '3':
        clear_screen()
        
        setting = input("Select setting:\n1. Change OS\n2. Cheats\n>>>")
        if setting == '1':
            if system == '1':
                system = '2'
                print('Changed to Linux')
            elif system == '2':
                system = '1'
                print('Changed to Windows')
        elif setting == '2':
            if noclip is True:
                ncstatus = 'on'
            else: 
                ncstatus = 'off'
            cheat = input(f"Select cheat:\n1. No-clip {ncstatus}\n2. Infinity scores\n3. Custom scores")
            if cheat == '1':
                if noclip is False:
                    noclip = True
                else:
                    noclip = False
            elif cheat == '2':
                scores = 1298489398280
            elif cheat == "3":
                scores = int(input("Amount of Scores: "))
        clear_screen()
                
    elif menu == '4':
        pass
    elif menu == '5':
        clear_screen()
        shop_select = input('Select item:\n1. Score boost - 2500\n2. Fix BSoD - 5000\n3. Fix Errors - 3750')
        if shop_select == "1":
            if scores >= 2500:
                scores_boost += 1
                scores -= 2500
        elif shop_select == "2":
            if scores >= 5000:
                BSoD_fix = True
                scores -= 5000
        elif shop_select == "3":
            if scores >= 3750:
                errors_fix = True
                scores -= 3750
        clear_screen()
