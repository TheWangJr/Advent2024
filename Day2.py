file = open("Day2Input.txt","r")
content = file.readlines()


def increment_or_decrement_in_range(array):
    for n in range(len(array)-1):
        if abs(int(array[n])-int(array[n+1])) < 1 or abs(int(array[n])-int(array[n+1])) > 3:
            return False
    return True    

def is_safe(line: list[str]):
    parts = [int(num) for num in line]
    test = sorted(parts, reverse=False)
    revtest = sorted(parts , reverse=True)
    return (parts == test or parts == revtest) and increment_or_decrement_in_range(parts)

def solve_part_one():
    counter = 0
    for line in content:
        line = line.strip().split()
        counter += is_safe(line)
    return counter

print(solve_part_one())

def solve_part_two():
    counter = 0
    for i,line in enumerate(content):
        line = line.split()
        counter += is_safe(line)
        if not is_safe(line):
            for n,x in enumerate(line):
                if is_safe(line[:n]+line[n+1:]):
                    counter += 1
                    break
                
    return counter

print(solve_part_two())