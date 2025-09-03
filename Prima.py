n=15
m=n
res=True
if m==1:
    res=False
else:
    while m>=3:
        if n%(m-1)==0:
            res=False
        m=m-1
print(res)
