import re

content = open("Day3Input.txt").read().strip()

def partone():
    list = re.findall("mul\(\d+,\d+\)",content)
    ans = 0
    for i in list:
        num1,num2 = re.findall("\d+",i)
        ans += int(num1)*int(num2)
    return ans


def parttwo():
    list = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",content)
    ans = 0
    is_valid = True
    for x in list:
        if x == "do()":
            is_valid = True
        elif x == "don't()":
            is_valid = False
        else:
            if is_valid:
                num1,num2 = re.findall("\d+",x)
                ans += int(num1)*int(num2)
    return ans

if __name__ == "__main__":
    print(partone())
    print(parttwo())