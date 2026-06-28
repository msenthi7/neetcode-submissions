class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    grid[r][c] = '0'          # mark visited immediately
                    q = deque([(r, c)])
                    while q:
                        x, y = q.popleft()    # FIFO → explores layer by layer
                        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'   # mark on ENQUEUE, not dequeue
                                q.append((nx, ny))
                    #count  # blob fully sunk
        return count

        
        