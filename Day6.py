import re

content = open("Day6Input.txt").read().strip()

D = content.split('\n')
col = len(D[0])
row = len(D)


for r in range(row):
    for c in range(col):
        if D[r][c] == "^":
            sr,sc = r,c