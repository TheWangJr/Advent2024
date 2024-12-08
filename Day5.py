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

def is_true(test,rules):

    for rule in rules.split('\n'):
            
            x,y = list(map(int,rule.split('|')))

            if x in test and y in test and test.index(y) < test.index(x):

                test.remove(x)

                test.insert(test.index(y),x)
                
                return False
    return True

def parttwo():
    ans= 0

    for input in inputs.split('\n'):

        test = list(map(int,input.split(',')))
        
        prev_test = None
        
        modified = False

        while not is_true(test, rules):
            if test == prev_test:  # If the test list hasn't changed, break the loop
                print(f"Stuck in an infinite loop! Current test: {test}")
                break
            prev_test = test.copy()
            modified =  True
            
        if modified:
            middle = len(test)//2
            ans += test[middle]
        
    return ans

if __name__ == "__main__":
    print(parttwo())
    