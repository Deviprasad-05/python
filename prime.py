num=int(input('entyer a num:- '))
i=1
count=0
while i<=num:
    if num % i==0:
        count+=1
    i+=1
if count==2:
        print('is a prime number')
else:
    print('not a prime number')