#ian bieg
#creates a table of squares and cubes

#create variables
numberSquared = 0
numberCubed = 0

#create header
print('Number\tSquare\tCube')
#create 5 numbers
for number in range(6):
    #calculations
    numberSquared = number ** 2 
    numberCubed = number ** 3
    #display results
    print(f'{number:>6}\t{numberSquared:>6}\t{numberCubed:>4}')
