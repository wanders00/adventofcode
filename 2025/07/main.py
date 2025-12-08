import functools


@functools.cache
def stream_split(h, w):
    global streams

    if h >= height or w < 0 or w >= width:
        return 0

    output = 0
    if grid[h][w] == '^':
        output += 1
        output += stream_split(h+1, w+1)
        output += stream_split(h+1, w-1)
    else:
        output += stream_split(h+1, w)

    return output


streams = list()

with open("input.txt") as f:
    grid = [line.strip() for line in f]

height = len(grid)
width = len(grid[0])

start_pos = 0
while grid[0][start_pos] != 'S':
    start_pos += 1

streams.append([1, start_pos])

result = stream_split(1, start_pos) + 1
print(result)
