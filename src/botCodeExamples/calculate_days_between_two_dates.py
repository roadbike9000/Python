# prompt: calculate days between two dates

import datetime


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
    return abs((d2 - d1).days)


d1 = '2024-03-12'
d2 = '2024-03-27'

print(days_between(d1, d2))
