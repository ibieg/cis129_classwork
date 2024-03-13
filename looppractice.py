#ianbieg
#declare variables
def main():
    while True:
        number = getInteger('Enter a number: ')
        if number % 2 == 0:
            print('The number is even')
        else:
            print('The number is odd')
        print('Do you want to do it again?')
        again = input('Enter \'y\' to go again ')
        if again.lower() != 'y' :
            break

def getInteger(message):
    while True:
        try:
            userInput = int(input(message))
            return userInput
        except ValueError:
            print('Incorrect data entered, please re-attempt')

main()