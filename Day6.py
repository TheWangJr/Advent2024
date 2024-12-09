import copy
import time

start_time = time.time()

content = open("Day6Input.txt").read().strip()

D = [list(row) for row in content.split('\n')]
col = len(D[0])
row = len(D)

start_row, start_col = None, None



direction_index = [(-1,0),(0,1),(1,0),(0,-1)] # up, right, down, left


for r in range(row):
    for c in range(col):
        if D[r][c] == "^":
            start_row,start_col = r,c
            break
    if start_col is not None:
        break


def cause_loop(obs_row,obs_col):
    
    new_D = copy.deepcopy(D)
    new_D[obs_row][obs_col] = '#'
    direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    
    current_row,current_col = start_row, start_col

    visited_position = set()

    while True:
        if (current_row,current_col,direction) in visited_position:
            return True
        
        visited_position.add((current_row,current_col,direction))

        dx,dy = direction_index[direction]
        new_row,new_col = current_row + dx, current_col + dy      

        if 0 <= new_row < row  and 0 <= new_col < col and new_D[new_row][new_col] == '#':

            direction = (direction + 1) % 4 # turn 90 degree clockwise

        elif 0 <= new_row < row  and 0 <= new_col < col:

            current_row, current_col = new_row, new_col

        else:
            return False

valid_positions = 0

for r in range(row):
    for c in range(col):
        if D[r][c] == '.':
            if cause_loop(r,c):
                valid_positions += 1

end_time = time.time()

ex_time = end_time - start_time

print(ex_time)

print(valid_positions)
