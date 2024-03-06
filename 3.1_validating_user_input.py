# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures
# process 10 students
for student in range(10):
    # get one exam result
    while student <= 9:
        result = int(input('Enter result (1=pass, 2=fail): '))
        if result == 1:
            passes = passes + 1
            break
        elif result == 2:
            break
        else: print('try again')
#calculate failures based off of passes
failures = (student + 1) - passes
# termination phase
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')
