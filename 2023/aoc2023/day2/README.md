# Day 1

[link](https://adventofcode.com/2023/day/1)

## Description

First time using Python, cool huh.

This problem was kinda similar to the day 1 problems. I used a similar approach of splitting the input into rows then reading them in a certain way to receive the answer.

### Part 1

I solved part 1 by splitting the input data into lines, then for each line I split it up further whenever there was a `:` or `;` character. Afterwards, I once again split it, by this time by ` ` (space) characters. Lastly, I then checked which color I was dealing with and whether it was above the allowed maximum or not. All around, a very straight forward approach.


  - Time elapsed: ~1 ms

### Part 2

For part 2, I more or less copied over my solution for part 1 but changed the last check to check if the color was below the minimum needed instead of above the maximum allowed. Overall, a very simple solution.

 - Time elapsed: ~1 ms

## How to run

### Install Python

[Python](https://www.python.org/downloads/)

### How to run

```bash
python3 main.py
```

