num=int(input('enter a num:- '))
out=0
for i in range(1,num):
    if num%i==0:
       out=out+i
    if out==num:
        print('perfect number')
else:
     print('not perfect number')
