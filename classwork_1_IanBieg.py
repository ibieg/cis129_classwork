#classwork Ian Bieg
userAge = int(input('How old are you?\n'))
drinkChoice = input('What do you want to drink?\n')
if userAge >= 21:
    print('Welcome to grown-up drink place')
    if drinkChoice.lower() == 'water':
        print('It\'s important to stay hydrated')
    else:
        print('Enjoy your grown-up beverage')
elif userAge < 21 and drinkChoice.lower() == 'water':
    print('Okay fine now here\'s some free water scram!')
else:
    print('You\'re not old enough to be here')
print('Thanks for stopping by')