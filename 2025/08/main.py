import math


def find_head(n):
    global circuit
    if circuit[n][0] == n:
        return n
    return find_head(circuit[n][0])


boxes = list()


with open("input.txt") as f:
    for line in f:
        boxes.append(tuple(map(int, line.strip().split(','))))


circuit = [[i, 1] for i in range(len(boxes))]
connections = list()


for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        d = math.dist(boxes[i], boxes[j])
        connections.append([d, i, j])

connections.sort(key=lambda x: x[0])

amt_circuits = len(circuit)

# part 2
last = (0,0)
i = 0
while amt_circuits > 1:
# for i in range(1000): part 1
    box1 = connections[i][1]
    box2 = connections[i][2]
    head1 = find_head(box1)
    head2 = find_head(box2)

    i += 1 # part 2

    if head1 == head2:
        continue
    
    amt_circuits -= 1
    circuit[head1][1] += circuit[head2][1]
    circuit[head2][1] = 0
    circuit[head2][0] = head1

    last = (box1, box2)

# part 1
# circuit.sort(key=lambda x: x[1], reverse=True)
# result = circuit[0][1] * circuit[1][1] * circuit[2][1]
# print(result)

result = boxes[last[0]][0] * boxes[last[1]][0]
print(result)