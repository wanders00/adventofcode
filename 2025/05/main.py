score = 0
min_max = list()

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        a, b = line.split('-')
        a = int(a)
        b = int(b)
        min_max.append((a, b))

    for line in f:
        val = int(line)
        for m_m in min_max:
            if val >= m_m[0] and val <= m_m[1]:
                score +=1
                break

print(score)