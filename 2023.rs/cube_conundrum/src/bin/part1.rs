const LIMIT: RGB = RGB {
    red: 12,
    green: 13,
    blue: 14,
};

fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    let output: u32 = input
        .lines()
        .enumerate()
        .filter(|(_, x)| process_line(x, LIMIT))
        .map(|(n, _)| (n as u32) + 1)
        .sum();
    return output.to_string();
}

struct RGB {
    red: u32,
    green: u32,
    blue: u32,
}

fn parse_draw(input: &str) -> RGB {
    let mut red: u32 = 0;
    let mut green: u32 = 0;
    let mut blue: u32 = 0;
    input.split(",").for_each(|draw| {
        let (count, color) = draw.trim().split_once(" ").unwrap();
        let n = count.parse::<u32>().unwrap();
        if color == "red" {
            red = n
        } else if color == "green" {
            green = n
        } else if color == "blue" {
            blue = n
        }
    });
    return RGB { red, green, blue };
}

fn process_line(input: &str, limit: RGB) -> bool {
    let (_game, draws) = input.split_once(":").unwrap();

    return draws
        .split(";")
        .map(|x| {
            let draw = parse_draw(x);
            draw.red <= limit.red && draw.green <= limit.green && draw.blue <= limit.blue
        })
        .all(|x| x);
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", true)]
    #[case("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", true)]
    #[case("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", false)]
    #[case("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", false)]
    #[case("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", true)]
    fn test_process_line(#[case] line: &str, #[case] possible: bool) {
        assert_eq!(process_line(line, LIMIT), possible);
    }

    #[test]
    fn test_part1() {
        assert_eq!(
            part1(
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
            ),
            "8"
        )
    }
}
