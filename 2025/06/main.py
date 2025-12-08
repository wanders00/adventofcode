score = 0
lines = list()

with open("input.txt") as f:
    for line in f:
        lines.append(line)

height = len(lines)
width = len(lines[height-1])

i = 0
while i < width:
    operator = lines[height-1][i]
    length = 0
    j = i+1
    while j < width and lines[height-1][j] == ' ':
        j+=1
    length = j - i - 1

    nums = list()
    for w in range(i, i+length):
        cur_num = list()
        for h in range(height-1):
            cur_num.append(lines[h][w])
        multiply = 1
        val = 0
        for n in reversed(cur_num):
            if n != ' ':
                val += int(n) * multiply
                multiply *= 10
        nums.append(val)
    
    cur = nums[0]
    for n in nums[1:]:
        if operator == '+':
            cur += int(n)
        else:
            cur *= int(n)
    score += cur

    i+=length+1

print(score)