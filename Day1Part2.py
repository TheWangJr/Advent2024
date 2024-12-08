file = open("Day_1_input","r")
content = file.readlines()

sum = 0
Left = []
Right = []

for line in content:
    parts = line.split()
    Left.append(int(parts[0]))
    Right.append(int(parts[1]))

Left.sort()
Right.sort()
counter = [0]*len(Left)

for n in range(len(Left)):
    try:
        counter[Left.index(Right[n])] += 1
    except:
        pass

for n in range(len(Left)):
    sum += counter[n]*Left[n]

print(sum)