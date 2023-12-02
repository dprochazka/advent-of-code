from dataclasses import dataclass


@dataclass
class Cubes:
    red: int
    green: int
    blue: int

    @classmethod
    def parse_from_text(cls, text):
        red, green, blue = 0, 0, 0
        cubes = text.split(", ")
        for cube in cubes:
            num, color = cube.split()
            if color == "red":
                red += int(num)
            elif color == "green":
                green += int(num)
            elif color == "blue":
                blue += int(num)
        return cls(red, green, blue)

    def check_possible(self, other):
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    @property
    def power(self):
        return self.red * self.green * self.blue


@dataclass
class Game:
    rounds: list[Cubes]

    @classmethod
    def parse_from_text(cls, text):
        game, rounds = text.split(":")
        rounds = rounds.split(";")
        rounds = [Cubes.parse_from_text(r) for r in rounds]
        return cls(rounds)

    def check_possible(self, max_round: Cubes):
        return all(r.check_possible(max_round) for r in self.rounds)

    def cubes_required(self) -> Cubes:
        red, green, blue = 0, 0, 0
        for r in self.rounds:
            red = max(red, r.red)
            green = max(green, r.green)
            blue = max(blue, r.blue)
        return Cubes(red, green, blue)


def find_possible_games(input_file, condition) -> list[int]:
    possible_games = []
    for num, line in enumerate(input_file, start=1):
        if Game.parse_from_text(line).check_possible(condition):
            possible_games.append(num)
    return possible_games


def find_cube_powers(input_file) -> list[int]:
    return [Game.parse_from_text(line).cubes_required().power for line in input_file]


if __name__ == "__main__":
    with open("input.txt") as input_file:
        possible_games = find_possible_games(
            input_file, Cubes(red=12, green=13, blue=14)
        )
    with open("input.txt") as input_file:
        cube_powers = find_cube_powers(input_file)
    print(sum(possible_games))
    print(sum(cube_powers))
