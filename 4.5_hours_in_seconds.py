def seconds_since_midnight(seconds = int(input('How many seconds have passed: '))):
    hour_in_seconds = (int(input('How many hours have passed: ')) * 60 ** 2)
    minute_in_seconds = (int(input('How many minutes have passed: ')) * 60)
    return print('It\'s been',hour_in_seconds + minute_in_seconds + seconds,'Seconds since midnight')
seconds_since_midnight()