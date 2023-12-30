import random

name = random.randint(bookmyshow)

while True:
    a= int(input('enter a name:- '))
    if a == name:
        print('Hi,{name} successfully booking seets',name)
        break
    elif a < 200:
        print('choose daimend class')
    elif a < 150:
        print('choose gold class')
    elif a < 100:
        print('choose silver class')
    else:
        print('select the number of sets:-')