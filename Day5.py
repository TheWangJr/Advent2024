import re

content = open("Day5Input.txt").read().strip()


rules,inputs = content.split('\n\n')




def partone():
    ans = 0
    for input in inputs.split('\n'):
        test = list(map(int,input.split(',')))
        ok = True
        for rule in rules.split('\n'):
            x,y = list(map(int,rule.split('|')))
            if x in test and y in test and test.index(y) < test.index(x):
                ok = False
                break
        if ok:
            x = len(test)//2
            ans += test[x]       


    return ans

def parttwo():
    ans= 0
    for input in inputs.split('\n'):
        test = list(map(int,input.split(',')))
        for rule in rules.split('\n'):
            x,y = list(map(int,rule.split('|')))
            if x in test and y in test and test.index(y) < test.index(x):
                test.insert(test.index(x),y)
                test.remove(y)
                l = len(test)//2
                ans += test[l]
    return ans

if __name__ == "__main__":
    print(partone())
    print(parttwo())
    