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

print(len(Left))
print(len(Right))

for n in range(len(Left)):
    sum += abs(Right[n]-Left[n])

print(sum)