BERYL_MAZE = [
    [300, -13, 189, -15, -12, 203, -23, 587, -78, 321, -46],
    [300, -11, -13, -24, 365, 198, -34, -21, 789, -81, -53],
    [300, -12, 112, -46, -76, -11, -23, -59, 321, 204, -32],
    [300, -23, 235, -12, -89, -62, -34, 212, -56, -67, -89],
    [300, 376, -23, -77, 227, -99, 134, 289, -12, 476, -51]
]

print("Enter a row and column location for your character in the format x,y:")
startPosition = input().split(",")
x, y = map(int, startPosition)
direction = input("Choose a direction:\n")
digitToFind = input("Choose a Dollar Indicator digit to find:\n")
digitToFind = str(digitToFind)

visitedLocations = []  
dollarIndicators = []
if direction == "right":
    dx, dy = 0, 1
elif direction == "up":
    dx, dy = -1, 0
elif direction == "down":
    dx, dy = 1, 0
else:
    print("Invalid direction!")
    exit()

found = False
initialPosition = (x, y)

visitedLocations.append(initialPosition)

while True:
    x += dx
    y += dy
    if x < 0 or x >= len(BERYL_MAZE) or y < 0 or y >= len(BERYL_MAZE[0]):
        print("Entered restricted area!")
        break
    visitedLocations.append((x, y))
    dollarValue = BERYL_MAZE[x][y]
    if dollarValue is not None:
        dollarIndicators.append(dollarValue)
        if digitToFind in str(dollarValue):
            found = True
            break
if found:
    print("Visited " + str(visitedLocations[1:]) + " with corresponding Dollar Indicators " + str(dollarIndicators))
    print("Found digit at location " + str(visitedLocations[-1]))
else:
    print("Returned to location " + str(initialPosition))
