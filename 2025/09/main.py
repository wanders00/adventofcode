# Inspiration taken from:
# https://www.youtube.com/watch?v=-w5mFTtRLE8
# https://gitlab.com/0xdf/aoc2025/-/tree/main/day09

import functools


@functools.cache
def point_in_polygon(x, y):
    inside = False

    for (x1, y1), (x2, y2) in edges:
        if (
            x == x1 == x2
            and min(y1, y2) <= y <= max(y1, y2)
            or y == y1 == y2
            and min(x1, x2) <= x <= max(x1, x2)
        ):
            return True
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside


def edge_intersects_rectangle(x1, y1, x2, y2, rx_min, ry_min, rx_max, ry_max):
    if x1 == x2:
        y_min, y_max = min(y1, y2), max(y1, y2)
        if rx_min < x1 < rx_max:
            if y_min < ry_max and y_max > ry_min:
                return True
    else:
        x_min, x_max = min(x1, x2), max(x1, x2)
        if ry_min < y1 < ry_max:
            if x_min < rx_max and x_max > rx_min:
                return True


def rectangle_in_polygon(rx_min, ry_min, rx_max, ry_max):
    for cx, cy in [(rx_min, ry_min), (rx_min, ry_max), (rx_max, ry_min), (rx_max, ry_max)]:
        if (cx, cy) not in coordinates_set:
            if not point_in_polygon(cx, cy):
                return False

    for (x1, y1), (x2, y2) in edges:
        if edge_intersects_rectangle(x1, y1, x2, y2, rx_min, ry_min, rx_max, ry_max):
            return False

    return True


score = 0
coordinates = list()
edges = list()

with open("input.txt") as f:
    for line in f:
        coordinates.append(tuple(map(int, line.strip().split(','))))

coordinates_set = set(coordinates.copy())

for i in range(len(coordinates)):
    p1 = coordinates[i]
    p2 = coordinates[(i + 1) % len(coordinates)]
    edges.append((p1, p2))


for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        (x1, y1), (x2, y2) = coordinates[i], coordinates[j]
        rx_min, rx_max = min(x1, x2), max(x1, x2)
        ry_min, ry_max = min(y1, y2), max(y1, y2)
        area = (rx_max - rx_min + 1) * (ry_max - ry_min + 1)

        if area > score and rectangle_in_polygon(rx_min, ry_min, rx_max, ry_max):
            score = area

print(score)
