# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwjfTacw-t9hWeRB-ffdVwiFc4TaIukV
"""

birth_year=input('birth year; ')
age= 2019-int(birth_year)
print(age)

weight_lbs=input('weight (lbs); ')
weight_kg= int(weight_lbs)*0.45
print(weight_kg)

course="python's course for beginners"
print(course)

course= '''

Hi chandan


Here is our first email for you.
Thank you,
The support team

'''
print(course)

course='Python for beginner'
print(course[0])
print(course[1])
print(course[2])
print(course[3])
print(course[4])
print(course[5])

print(course[-6])
print(course[-1])
print(course[-2])
print(course[-3])
print(course[-4])
print(course[-5])

course='Python for beginner'
print(course[0:5])
print(course[1:10])
print(course[2:6])
print(course[3:6])
print(course[4:10])
print(course[5:9])

'''index no'''


print(course[-6:1])
print(course[-1:2])
print(course[-2:5])
print(course[-3:9])
print(course[-4:7])
print(course[-5:4])

course='Python for beginner'
print(course[0])
print(course[0:])
print(course[1:])
print(course[-1:])
print(course[-10:])
print(course[:])

course='Python for beginner'
chandan =course[:]
print(chandan)

fist='chandan'
last='singh'
message=fist + '[' + last +'] is a coder'
print(message)

fist='chandan'
last='singh'
msg=f'{fist}[{last}] is a coder'
print(msg)

course=' python for beginner'
print(len(course))
course=' python  beginner'
print(len(course))
course=' python for '
print(len(course))

course=' python for beginner'
print(course.upper())

TCS='Ultimatix - Digitally Connected !'
print(TCS.upper())

TCS='Ultimatix - Digitally Connected !'
print(TCS.lower())

TCS='Ultimatix - Digitally Connected !'
print(TCS)

TCS='Ultimatix - Digitally Connected !'
print(TCS)
TCS='Ultimatix - Digitally Connected !'
print(TCS.lower())
TCS='Ultimatix - Digitally Connected !'
print(TCS.upper())

TCS='Ultimatix - Digitally Connected !'
print(TCS.find('D'))
print(TCS.find('c'))
print(TCS.find('n'))
print(TCS.find('connected'))

TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('Connected','chandan'))
TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('Digitally','chandan'))
TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('Ultimatix','chandan'))

TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('C','j'))
TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('Digitally','TCS'))
TCS='Ultimatix - Digitally Connected !'
print(TCS.replace('Ultimatix','KOLKATA'))

x=10
x=x+3
x +=3
print(x)

x=10
x=x+3
x -=3
print(x)

x=10+3*2
print(x)

x=10+3*2**2
print(x)

x=(10+3)*2**2
print(x)

x=(2+3)*10-3
print(x)

x=2.9
print(round(x))

x=-2.9
print(abs(x))

import math
print(math.floor(2.9))

is_hot=True