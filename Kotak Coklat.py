jCoklat = [2,5,3,6,8,11,5]
lCoklat = [3,3,6,5]
i = 0
n = 3
tCoklat = 0
w = 0
m = 0
j = 0
k = 0
while i <= n:
    k = lCoklat[i] - 1
    p = (k + m) % len(jCoklat)
    if w == p:
        j = 0
    else:
        w = p
        j = jCoklat[p]
    tCoklat = tCoklat + j
    m = m + lCoklat[i]
    i = i + 1
print(tCoklat)

kotakCoklat = [2, 5, 3, 6, 8, 11, 5]
langkah = [3, 3, 6, 5] 
tCoklat = 0
m = 0
j = 0
i = 0
while i < len(langkah):
    k = langkah[i] - 1
    p = (k + m) % len(kotakCoklat)
    if j != 0:
        tCoklat = tCoklat + j
    if kotakCoklat[p] != 0:
        j = kotakCoklat[p]
        kotakCoklat[p] = 0
    else:
        j = 0
    m = m + langkah[i]
    i = i + 1
if j != 0:
    tCoklat = tCoklat + j
print(tCoklat)