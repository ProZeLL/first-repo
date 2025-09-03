n = 7
if n==1:
    res = 0
elif n==2:
    res=1
else:
    res_1 = 0
    res_2 = 1
    x = 3
    while x<=n:
        res = res_1+res_2
        res_1 = res_2
        res_2 = res
        x = x+1
print(res)

ARR = [0,1]
i = 1
while len(ARR) < n:
    ARR.append((ARR[i]+ARR[i-1]))
    i = i + 1
print(ARR)

