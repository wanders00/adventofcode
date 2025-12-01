import re
import time

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    part1(lines)

    part2(lines)


def part1(lines):
    start_time = time.time()

    answer = 0

    for line in lines:
        okay = True
        segments = re.split(':|;', line)

        for i in range(1, len(segments)):
            colors = re.split(',', segments[i])
            for color in colors:
                number_color = color.strip().split(' ')
                if number_color[1] == 'red':
                    if int(number_color[0]) > MAX_RED:
                        okay = False
                        break
                elif number_color[1] == 'green':
                    if int(number_color[0]) > MAX_GREEN:
                        okay = False
                        break
                elif number_color[1] == 'blue':
                    if int(number_color[0]) > MAX_BLUE:
                        okay = False
                        break
        if okay:
            game_number = segments[0].split(' ')[1]
            answer += int(game_number)

    print("part1: ", answer)
    print("time: ", time.time() - start_time)


def part2(lines):
    start_time = time.time()

    answer = 0

    for line in lines:
        min_red = 0
        min_green = 0
        min_blue = 0

        segments = re.split(':|;', line)

        for i in range(1, len(segments)):
            colors = re.split(',', segments[i])
            for color in colors:
                number_color = color.strip().split(' ')
                if number_color[1] == 'red':
                    if min_red < int(number_color[0]):
                        min_red = int(number_color[0])
                elif number_color[1] == 'green':
                    if min_green < int(number_color[0]):
                        min_green = int(number_color[0])
                elif number_color[1] == 'blue':
                    if min_blue < int(number_color[0]):
                        min_blue = int(number_color[0])

        answer += min_red * min_green * min_blue

    print("part2: ", answer)
    print("time: ", time.time() - start_time)


if __name__ == "__main__":
    main()
