             
'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

Example 1:
Input: grid = [
  ['0','1', '0'],
  ['1','1', '1'],
  ['0','1', '0'],
]
Output: 1

Example 2:
Input: grid = [
  ['1','0', '1'],
  ['0','1', '0'],
  ['1','0', '1'],
]
Output: 5

Example 3:
Input: grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
Output: 1

Example 4:
Input: grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
Output: 3

Example 5:
Input: grid = [
  ['1','1','1','0','0'],
  ['1','1','1','0','0'],
  ['1','1','1','0','0'],
  ['0','0','0','1','1']
]
Output: 2


'''

from collections import deque

def func(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)]
    result = 0
    
    for x in range(m):
        for y in range(n):
            if not visited[x][y] and grid[x][y] == '1':
                result += 1
                deq = deque()
                deq.append((x, y))
                visited[x][y] = True
                while deq:
                    i, j = deq.popleft()
                    if 0 <= i - 1 < m and 0 <= j < n:
                        if not visited[i - 1][j]:
                            if grid[i - 1][j] == '1':
                                deq.append((i - 1, j))
                            visited[i - 1][j] = True
                    if 0 <= i + 1 < m and 0 <= j < n:
                        if not visited[i + 1][j]:
                            if grid[i + 1][j] == '1':
                                deq.append((i + 1, j))
                            visited[i + 1][j] = True
                    if 0 <= i < m and 0 <= j - 1 < n:
                        if not visited[i][j - 1]:
                            if grid[i][j - 1] == '1':
                                deq.append((i, j - 1))
                            visited[i][j - 1] = True
                    if 0 <= i < m and 0 <= j + 1 < n:
                        if not visited[i][j + 1]:
                            if grid[i][j + 1] == '1':
                                deq.append((i, j + 1))
                            visited[i][j + 1] = True
                
    return result

if __name__ == '__main__':
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]

    print(func(grid))
