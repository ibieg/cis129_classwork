#classwork Ian Bieg
userAge = int(input('How old are you?\n'))
drinkChoice = input('What do you want to drink?\n')
if userAge >= 21:
    print('Welcome to grown-up drink place')
    if drinkChoice.lower() == 'water':
        print('It\'s important to stay hydrated')
    else:
        print('Enjoy your grown-up beverage')
else:
    print('You\'re not old enough to be here')