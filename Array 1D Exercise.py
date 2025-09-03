ARR = [8,8,4,2,3,0]
ARR_N = [8,7,4,2,1,0]

#Mengecek suatu list turun sesuai order
i = 0
n = 5
res=True
while i<=n-1:
    if ARR[i]<ARR[i+1]:
        res=False
    i=i+1
print(res)

#Mencari nilai terkecil dalam suatu array
i=1
n=5
res=ARR[0]
while i<=n:
    if ARR[i]<res:
        res=ARR[i]
    i+=1
print(res)

#Mengecek suatu list turun secara strict
i=0
n=5
res=True
while i<=n-1:
    if ARR[i]==ARR[i+1]:
        res=False
    i=i+1
print(res)

#Mencari total nilai dalam suatu array
i=0
n=5
total=0
while i<=n:
    total = total+ARR[i]
    i=i+1
print(total)

#Mencari nilai terbesar dalam suatu array
i=1
n=5
res=ARR[0]
while i<=n:
    if ARR[i]>res:
        res=ARR[i]
    i=i+1
print(res)

#Mencari frekuensi pada setiap nilai di rentang 1-100
i_ARR=0
i_FREK_ARR = 0
frekuensi_nilai=1
n=6
FREK_ARR = [0]
while (i_FREK_ARR<=frekuensi_nilai) and (frekuensi_nilai!=101):
    while i_ARR<=n:
        if frekuensi_nilai == ARR[i_ARR]:
            FREK_ARR[i_FREK_ARR]+=1
        i_ARR+=1
    if frekuensi_nilai == 100:
        print(FREK_ARR)
    FREK_ARR+=[0]
    i_FREK_ARR+=1
    frekuensi_nilai+=1
    i_ARR=0

#Membuat array untuk rata-rata dari kedua nilai pada kedua array
i=0
n=7                                 #(size of ARR)
ARR_AVG = [0]*n                     # ([0] * size of ARR)
while i<=n-1:
    ARR_AVG[i]=(ARR[i]+ARR_N[i])/2
    i=i+1
print(ARR_AVG)
    