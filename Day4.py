content = open("Day4Input.txt").read().strip()

D = content.split('\n')

def partone():
    ans = 0
    col = len(D[0])
    row = len(D)
    for r in range(row):
        for c in range(col):
            if r+3 < row and D[r][c] == 'X' and D[r+1][c] == 'M' and D[r+2][c] == 'A' and D[r+3][c] == 'S': #down
                ans += 1
            if c+3 < col and D[r][c] == 'X' and D[r][c+1] == 'M' and D[r][c+2] == 'A' and D[r][c+3] == 'S': #right
                ans += 1
            if r+3 < row and D[r][c] == 'S' and D[r+1][c] == 'A' and D[r+2][c] == 'M' and D[r+3][c] == 'X': #up
                ans += 1
            if c+3 < col and D[r][c] == 'S' and D[r][c+1] == 'A' and D[r][c+2] == 'M' and D[r][c+3] == 'X': #left
                ans += 1
            if r+3 < row and c+3 < col and D[r][c] == 'X' and D[r+1][c+1] == 'M' and D[r+2][c+2] == 'A' and D[r+3][c+3] == 'S': #down right
                ans += 1
            if r-3 >= 0 and c-3 >= 0 and D[r][c] == 'X' and D[r-1][c-1] == 'M' and D[r-2][c-2] == 'A' and D[r-3][c-3] == 'S': #up left
                ans += 1
            if r-3 >= 0 and c+3 < col and D[r][c] == 'X' and D[r-1][c+1] == 'M' and D[r-2][c+2] == 'A' and D[r-3][c+3] == 'S': #down left
                ans += 1
            if r+3 < row and c-3 >= 0 and D[r][c] == 'X' and D[r+1][c-1] == 'M' and D[r+2][c-2] == 'A' and D[r+3][c-3] == 'S': #up right
                ans += 1
    return ans

def parttwo():
    ans = 0
    col = len(D)
    row = len(D[0])
    for r in range(row):
        for c in range(col):
            if r+2 < row and c+2 < col and D[r][c] == 'M' and D[r+1][c+1] == 'A' and D[r+2][c+2] == 'S' and D[r][c+2] == 'M' and D[r+2][c] == 'S':
                ans += 1
            if r+2 < row and c+2 < col and D[r][c] == 'M' and D[r+1][c+1] == 'A' and D[r+2][c+2] == 'S' and D[r+2][c] == 'M' and D[r][c+2] == 'S':
                ans +=1
            if r+2 < row and c+2 < col and D[r][c] == 'S' and D[r+1][c+1] == 'A' and D[r+2][c+2] == 'M' and D[r][c+2] == 'S' and D[r+2][c] == 'M':
                ans += 1
            if r+2 < row and c+2 < col and D[r][c] == 'S' and D[r+1][c+1] == 'A' and D[r+2][c+2] == 'M' and D[r+2][c] == 'S' and D[r][c+2] == 'M':
                ans +=1
    return (ans)

if __name__ == "__main__":
    print(partone())
    print(parttwo())