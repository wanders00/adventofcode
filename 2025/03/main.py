import math

score = 0
to_enable_len = 12

def best_battery_in_range(start, end, str):
    index = 0
    val = '0'
    for i in range(start, end):
        c = str[i]
        if c > val:
            val = c
            index = i
    return (val, index)

def max_joltage(str):
    global score
    global to_enable_len
    to_enable = list()

    start = 0
    end = len(str) - to_enable_len + 1

    for i in range(to_enable_len):
        val, start = best_battery_in_range(start,end,str)
        to_enable.append(val)
        start += 1
        end += 1

    multiplicator = math.pow(10, to_enable_len - 1)
    for i in range (to_enable_len):
        score += int(to_enable[i]) * multiplicator
        multiplicator /= 10


with open("input.txt") as f:
    for x in f:
        max_joltage(x.strip())

print(score)