n=5
i=1
total=0
while i<=n:
    if i%2==1:
        total=total+4/((2*i)-1)
    else:
        total=total-4/((2*i)-1)
    i=i+1
print(total)