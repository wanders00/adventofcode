use std::fs::File;
use std::io::Read;
use std::io::Result;
use std::collections::HashMap;
use std::time::Instant;

fn main() {
    let start = Instant::now();

    let mut contents = String::new();
    match read_file("src/input.txt") {
        Ok(file_contents) => {
            contents = file_contents;
        }
        Err(error) => println!("Error: {}", error),
    }

    let mut first_digit: u32 = 0;
    let mut last_digit: u32 = 0;
    let mut sum: u32 = 0;

    for line in contents.lines() {
        let chars: Vec<_> = line.chars().collect();
        for i in 0..chars.len() {
            let char = chars[i];
            // Part 1
            if char.is_numeric() {
                append_value(
                    &mut first_digit,
                    &mut last_digit,
                    char.to_digit(10).unwrap(),
                );
                // Part 2
            } else {
                let matching = matches_letter_number(&chars, i.clone());
                if matching > 0 {
                    append_value(&mut first_digit, &mut last_digit, matching);
                }
            }
        }
        sum += first_digit + last_digit;

        first_digit = 0;
        // last_digit = 0; // each row has at least one number, so we don't need to reset this
    }

    println!("Sum: {}", sum);

    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
    // Part 1: Sum = 54239 in 1~ ms
    // Part 2: Sum = 55343 in 75~ ms
}

#[allow(dead_code)]
fn matches_letter_number(chars: &[char], i: usize) -> u32 {
    let mut map = HashMap::new();
    map.insert("one", 1);
    map.insert("two", 2);
    map.insert("three", 3);
    map.insert("four", 4);
    map.insert("five", 5);
    map.insert("six", 6);
    map.insert("seven", 7);
    map.insert("eight", 8);
    map.insert("nine", 9);

    let letter_numbers: [&str; 9] = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    let mut matching = 0;
    for letter_number in letter_numbers.iter() {
        let mut match_count = 0;
        for (j, letter) in letter_number.chars().enumerate() {
            if i + j < chars.len() && chars[i + j] == letter {
                match_count += 1;
            }
        }
        if match_count == letter_number.len() {
            matching = *map.get(letter_number).unwrap();
        }
    }

    return matching;
}

fn append_value(first_digit: &mut u32, last_digit: &mut u32, char_as_int: u32) {
    // first digit == 0 means we haven't set it yet
    if *first_digit == 0 {
        *first_digit = char_as_int * 10;
    }
    *last_digit = char_as_int;
}

fn read_file(path: &str) -> Result<String> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}
