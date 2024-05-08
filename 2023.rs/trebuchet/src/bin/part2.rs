fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let output = input
        .lines()
        .map(process_line)
        .sum::<u32>();
    return output.to_string();
}

fn process_line(input: &str) -> u32 {
    let numerals = vec!["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    let mut first: Option<u32> = None;
    let mut last: Option<u32> = None;
    for (i, c) in input.chars().enumerate() { 
        if c.is_numeric() {
            let c = c.to_digit(10).unwrap();
            if first.is_none() { first = Some(c) };
            last = Some(c);
        }
        let substring = input.get(i..);
        for (j, n) in numerals.iter().enumerate() {
            if substring.expect("invalid substring result").starts_with(n) {
                if first.is_none() { first = Some(j as u32) };
                last = Some(j as u32);
            }
        }
    }
    return 10 * first.unwrap() + last.unwrap();
}


#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("1abc2", 12)]
    #[case("pqr3stu8vwx", 38)]
    #[case("a1b2c3d4e5f", 15)]
    #[case("treb7uchet", 77)]
    #[case("two1nine", 29)]
    #[case("eightwothree", 83)]
    #[case("abcone2threexyz", 13)]
    #[case("xtwone3four", 24)]
    #[case("4nineeightseven2", 42)]
    #[case("zoneight234", 14)]
    #[case("7pqrstsixteen", 76)]
    fn test_process_line(
        #[case] line: &str,
        #[case] expected: u32,
    ) {
        assert_eq!(process_line(line), expected);
    }
}
