grid_size = 20
grid = [[1] * (grid_size + 1) for _ in range(grid_size + 1)]

for i in range(1, grid_size + 1):
    for j in range(1, grid_size + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

print(grid[grid_size][grid_size])
