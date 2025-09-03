n = 7
m = n-1
if n % 2 == 0:
    total = n*-1
else:
    total = n
while m>0:
    if m%2==0:
        m=m*-1
        total = total + m
        m = (m*-1)-1
    else:
        total = total + m
        m = m-1
print(total)