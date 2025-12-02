score = 0
end = 0

# part 1
# def invalid(cur_string):
#     global score
#     global end
#     cur = int(cur_string)
#     while cur < end:
#         length = len(cur_string)
#         mid = int(length / 2)
#         if cur_string[:mid] == cur_string[mid:]:
#             score += cur
#         cur += 1
#         cur_string = str(cur)

def invalid(cur_string):
    global score
    global end
    cur = int(cur_string)
    while cur < end:
        length = len(cur_string)
        for i in range(1, int(length / 2) + 1):
            if length % i != 0:
                continue
            iteration = 1
            prev = cur_string[:i]
            next = cur_string[i:i*2]
            while prev == next:
                iteration+=1
                prev = next
                next = cur_string[i*iteration:i*(iteration+1)]
                if iteration * i >= length:
                    score += cur
                    break
            else:
                continue
            break

        cur += 1
        cur_string = str(cur)

with open("input.txt") as f:
    ranges = [r.split('-') for r in f.readline().split(',')]
    for r in ranges:
        end = int(r[1]) + 1
        invalid(r[0])

print(score)