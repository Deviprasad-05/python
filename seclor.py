a=[1,9,11,23,65,78,43]
out=a[0]
out2=a[0]
for i in a:
    if out<i:
        out2=out
        out=i
    elif out2<i:
        out2=i
print(out,out2)