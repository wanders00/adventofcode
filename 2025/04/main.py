with open("input.txt") as f:
    grid = [line.strip() for line in f]

h = len(grid)
w = len(grid[0])

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

out = [list(r) for r in grid]
score = 0


def remove(grid):
    out = [list(r) for r in grid]
    accessible = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != '@':
                continue

            count = 0
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '@':
                    count += 1

            if count < 4:
                out[i][j] = 'x'
                accessible += 1
    return accessible, out


output, grid = remove(grid)
score += output
while output != 0:
    output, grid = remove(grid)
    score += output

print(score)
