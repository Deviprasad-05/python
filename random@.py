import random

num = random.randint(100,200)

while True:
    a= int(input('enter a number:- '))
    if a == num:
        print('congrats you successfully geussed the number',num)
        break
    elif a < num:
        print('enter greater number')
    elif a > num:
        print('enter lesser number')