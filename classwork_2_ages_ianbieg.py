#ian bieg

#aquire user age
age = int(input('Enter your age: '))
if age <= 0 or age >= 100:
    print('ERROR')
elif age > 12 and age < 20:
    print('You\'re a teen!')
elif age > 70:
    print('You\'re a senior')
else:
    print('Hello')