# Day 1

[link](https://adventofcode.com/2023/day/1)

## Description

Decided to do this challenge in Rust. I've been wanting to learn it for a while now, but it always seemed to hard to do it in a actual project so I decided to do it here.

### Part 1

Part 1 was very straight forward. I just read the input file and looped through all the lines and then a nested looped through all the characters in the line. I then checked if the character `is_numeric()` whether to `append_value()` or not. Then after each character I added the the `first_digit` & `last_digit` to the sum.

  - Time elapsed: ~1 ms

### Part 2

The way I solved part 2 was also straight forward. However, it is a bit expensive, 75x time elapsed as part 1. There are definitely better ways to solve this, but I was just trying to get it done. The solution being that if the character `is_numeric() == false` I have an else statement that checks whether `matches_letter_number() > 0` (i.e it equals a number).

This function takes a slice of characters and an index as input. It creates a HashMap mapping string representations of numbers to their numeric values. It then checks each character in the input slice against these number words. If a match is found, it returns the numeric value of the matched number word. If no match is found, it returns 0.

 - Time elapsed: ~75 ms

## How to run

### Install Rust

Follow the instructions [here](https://www.rust-lang.org/tools/install) to install Rust.

### Run the code

1. Clone the repo
2. Navigate into day1 folder `cd day1`
3. Run `cargo run`
