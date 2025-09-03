BERYL_MAZE = [
 [300, -13, 189, -15, -12, 203, -23, 587, -78, 321, -46],
 [300, -11, -13, -24, 365, 198, -34, -21, 789, -81, -53],
 [300, -12, 112, -46, -76, -11, -23, -59, 321, 204, -32],
 [300, -23, 235, -12, -89, -62, -34, 212, -56, -67, -89],
 [300, 376, -23, -77, 227, -99, 134, 289, -12, 476, -51]
]
 
while (True):
    print("Enter a row and column location for your character in the format x,y:")
    inputTitik = input().split(',')
    x, y = map(int, inputTitik)
    if ((x >= 0 and x < 5) and (y >= 0 and y < 11)):
        print("Enter a character name:")
        name = input()
        break
    else:
        print("Position chosen is invalid. Try again!")
        
for i in range (5):
    for j in range (11):
        if (i == x and j == y):
            print("<" + name[0] + ">", end = "  ")
        else:
            print(BERYL_MAZE[i][j], end = "  ")
    print()