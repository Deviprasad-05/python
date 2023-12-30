num=int(input('entyer a num:- '))
i=1
temp=False
while i<=num:
    if num % i==0 and i!=0 and i!=num:
        temp=True
    i+=1
if not temp:
        print('is a prime number')
else:
    print('not a prime number')