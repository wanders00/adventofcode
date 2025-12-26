import functools

lines = dict()


@functools.cache
def traverse(node, goal) -> int:
    paths = 0
    if node == goal:
        return 1
    for path in lines.get(node, []):
        paths += traverse(path, goal)
    return paths


with open("input.txt") as f:
    for line in f:
        if line.strip():
            cur = line.split()
            cur[0] = cur[0].rstrip(":")
            lines[cur[0]] = cur[1:]

# score = traverse("you", "out") # part 1
score = 0
score += traverse("dac", "out") * traverse("fft", "dac") * traverse("svr", "fft")
score += traverse("fft", "out") * traverse("dac", "fft") * traverse("svr", "dac")
print(score)
