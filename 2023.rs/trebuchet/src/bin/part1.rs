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
    let mut first: Option<u32> = None;
    let mut last: Option<u32> = None;
    for c in input.chars() { 
        if c.is_numeric() {
            let c = c.to_digit(10).unwrap();
            if first.is_none() { first = Some(c) };
            last = Some(c);
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
    fn test_process_line(
        #[case] line: &str,
        #[case] expected: u32,
    ) {
        assert_eq!(process_line(line), expected);
    }
}
