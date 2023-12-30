result=[]
for i in range(1,11):
    out=1
    for i in range(1,i+1):
        out*=i
    result=[out]
    print(result)
