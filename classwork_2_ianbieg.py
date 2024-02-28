#ian bieg
age = int(input('Enter your age: '))
if age >12 and age < 20:
    print('You\'re a teen!')
elif age > 70:
    print('You\'re a senior')
elif age <= 0 or age >= 100:
    print('ERROR')
else:
    print('Hello')