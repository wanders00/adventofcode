score = 0
cur = 50

# part 2 helper
def modulo_info(n):
    wraps = n // 100
    remainder = n % 100
    return abs(wraps), remainder

def change_cur(dir, amt):
    global cur
    global score
    if dir == 'L':
        amt = amt * -1
    
    old_cur = cur # part 2
    cur += amt

    # part 1
    # cur = cur % 100
    # if cur == 0:
    #     score += 1
    
    # part 2
    increment, cur = modulo_info(cur)

    if dir == 'L':
        if old_cur == 0:
            increment -= 1
        elif cur == 0:
            increment += 1
        
    score += increment


with open("input.txt") as f:
    for x in f:
        change_cur(x[0], int(x[1:]))

print(score)