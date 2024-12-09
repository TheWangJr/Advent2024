import copy
import time

start_time = time.time()

content = open("Day7Input.txt").read().strip()

D = content.split('\n')

G = []

ans = 0

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def math_left_to_right(expression):
    parts = expression.split()
    ans = int(parts[0])

    i = 1

    while i < len(parts):
        operation = parts[i]
        next_number = int(parts[i+1])

        if operation == '+':
            ans += next_number
        elif operation == '*':
            ans *= next_number
        elif operation == '||':
            ans = int(str(ans) + str(next_number))
        else:
            print(f"error {operation}")
        
        i+=2
    return ans

for line in D:
    test,cause = line.split(':')
    
    G.append((int(test.strip()), list(map(int, cause.strip().split()))))


for line in G:
    
    x,y = line

    operation_space = len(y)-1

    binary_test = '0'.zfill(operation_space)
    
    while operation_space >= len(binary_test):
        count = 1
        testing = copy.deepcopy(y)
        for op in range(len(binary_test)):
            if binary_test[op] == '0':
                testing.insert(op+count,'+')
                count+=1
            elif binary_test[op] == '1':
                testing.insert(op+count,'*')
                count+=1
            elif binary_test[op] == '2':
                testing.insert(op+count,'||')
                count+=1
            else:
                print('There is an error')
    
        if math_left_to_right(' '.join(map(str,testing))) == x:
        
            ans += math_left_to_right(' '.join(map(str,testing)))
            break
        
        binary_test = ternary(int(binary_test, 3) + 1).zfill(operation_space)


end_time = time.time()
ex_time = end_time - start_time

print(f"Code executed in {ex_time:.4f} seconds")  

print(ans)

