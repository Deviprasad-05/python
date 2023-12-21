char = input('enter a char:- ')

if 'A'<=char <='Z':
    print('it is an uppercase char')

elif 'a'<=char <='z':
    print('it is a lower char')

elif '0'<=char <='9':
    print('it is a digit')

else:
    print('it is a special char')