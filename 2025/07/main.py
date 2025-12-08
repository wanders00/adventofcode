score = 0
visited = dict()
streams = list()

with open("example.txt") as f:
    grid = [line.strip() for line in f]

height = len(grid)
width = len(grid[0])

start_pos = 0
while grid[0][start_pos] != 'S':
    start_pos += 1

streams.append([1, start_pos])

while len(streams) > 0:
    cur = streams.pop(0)
    h = cur[0]
    w = cur[1]
    if h >= height or w < 0 or w >= width:
        continue

    if grid[h][w] == '^':
        score += 1
        streams.append([h+1, w+1])
        streams.append([h+1, w-1])
    else:
        streams.append([h+1, w])


print(score)