# Okay, this problem is a bit cheesy. As it is very hard. However, the data allows for a very simple solution.
# Either the data is way too much to fit in the area, or so small that you dont need to even attempt to structure the grid with the gifts to fit.
# Better explanation is here https://jjeii.github.io/AdventOfCode/2025.html#day12p1


from dataclasses import dataclass


@dataclass
class Tree:
    width: int
    height: int
    gifts: list[int]


gifts = [
    ["###", "#.#", "#.#"],  # 0
    ["#..", "##.", ".##"],  # 1
    ["##.", "###", "#.#"],  # 2
    ["..#", ".##", "###"],  # 3
    ["##.", "##.", "###"],  # 4
    ["###", ".#.", "###"]   # 5
]

gifts_size = [7, 5, 7, 6, 7, 7]

trees = list[Tree]()

with open("input.txt") as f:
    for line in f:
        if line.strip():
            cur = line.split()
            (width, height) = cur[0].rstrip(":").split("x")
            tree = Tree(
                width=int(width),
                height=int(height),
                gifts=[int(x) for x in cur[1:]]
            )
            trees.append(tree)

score = 0
for tree in trees:
    amt_gifts = 0
    for gift in tree.gifts:
        amt_gifts += gift
    if amt_gifts * 3 * 3 <= tree.width * tree.height:
        score += 1
print(score)
