#No. a
nilai = [5,5,6,8,1,1,1,10,10,7]
frek = [0,0,0,0,0,0,0,0,0,0]
i=0
n=9
while i<=n:
    if nilai[i] == 1:
        frek[0] = frek[0]+1
    elif nilai[i] == 2:
        frek[1] = frek[1]+1
    elif nilai[i] == 3:
        frek[2] = frek[2]+1
    elif nilai[i] == 4:
        frek[3] = frek[3]+1
    elif nilai[i] == 5:
        frek[4] = frek[4]+1
    elif nilai[i] == 6:
        frek[5] = frek[5]+1
    elif nilai[i] == 7:
        frek[6] = frek[6]+1
    elif nilai[i] == 8:
        frek[7] = frek[7]+1
    elif nilai[i] == 9:
        frek[8] = frek[8]+1
    else:
        frek[9] = frek[9]+1
    i = i+1
print(frek)

#No. b   
i = 0
n = 9
frek_kum = [0,0,0,0,0,0,0,0,0,0]
while i<=n:
    frek_kum[i]=frek_kum[i-1]+frek[i]
    i=i+1
print(frek_kum)

#No. c
x = 4
i = 0
n = 9
res = 0
while i<=n:
    if nilai[i]<=x and frek_kum[nilai[i]-1]!=0:
        res=res+1
    i=i+1
print(res)
