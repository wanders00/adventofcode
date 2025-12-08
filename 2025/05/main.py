score = 0
min_max = list()

def optimize_minmax(min_max):
    min_max.sort()
    optimized = list()
    current_min, current_max = min_max[0]
    for m_m in min_max[1:]:
        if m_m[0] <= current_max:
            if m_m[1] > current_max:
                current_max = m_m[1]
        else:
            optimized.append((current_min, current_max))
            current_min, current_max = m_m
    optimized.append((current_min, current_max))
    return optimized

def fresh_amount(min_max):
    total = 0
    for m_m in min_max:
        total += m_m[1] - m_m[0] + 1
    return total

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        a, b = line.split('-')
        a = int(a)
        b = int(b)
        min_max.append((a, b))

    # Part 2
    min_max = optimize_minmax(min_max)
    print(fresh_amount(min_max))
    # Part 2 end

    for line in f:
        val = int(line)
        for m_m in min_max:
            if val >= m_m[0] and val <= m_m[1]:
                score +=1
                break

print(score)