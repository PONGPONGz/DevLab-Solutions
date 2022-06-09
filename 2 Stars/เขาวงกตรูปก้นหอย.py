# https://www.borntodev.com/devlab/task/749?languageId=71
import math
n = int(input())
size = math.isqrt(n)

NORTH, SOUTH, WEST, EAST = (0, -1), (0, 1), (-1, 0), (1, 0)
DIRECTIONS = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}

count, x, y = 0, 0, 0
current_direction = SOUTH

matrix = [[None]*size for _ in range(size)]

while True:
  count += 1
  matrix[y][x] = count
  new_x, new_y = x + current_direction[0], y + current_direction[1]
  if 0 <= new_x < size and 0 <= new_y < size and matrix[new_y][new_x] is None:
    x, y = new_x, new_y
  else:
    new_direction = DIRECTIONS[current_direction]
    x, y = x + new_direction[0], y + new_direction[1]
    current_direction = new_direction
    if matrix[y][x] is not None:
      break
            
for i in matrix:
  print(*map(lambda j: '0'*(3-len(str(j)))+str(j), i))

print('UP : {}\nDOWN : {}\nLEFT : {}\nRIGHT : {}'.format(size//2,size//2+1 if size % 2 != 0 else size // 2,size//2 if size % 2 != 0 else size // 2 - 1,size//2))