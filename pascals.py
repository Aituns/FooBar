height = int(input("height: "))

oldrow = [1]
newrow = []

for i in range(height):
    newrow.clear
    if (i == 0 or i == len(oldrow)):
        newrow.append(i+1)
    else:
        newrow.append(oldrow[i] + oldrow[i+1])
    print(newrow)