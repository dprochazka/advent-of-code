import pytest

from cube_conundrum import Game, Cubes, find_possible_games, find_cube_powers

EXAMPLE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

POSSIBILITY_CONDITION = Cubes(red=12, green=13, blue=14)

POSSIBLE_GAMES = {1, 2, 5}

CUBE_POWERS = [48, 12, 1560, 630, 36]


def test_game_parser():
    game = Game.parse_from_text(
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    )

    assert game.rounds[0].red == 0
    assert game.rounds[0].blue == 1
    assert game.rounds[0].green == 2
    assert game.rounds[1].red == 1
    assert game.rounds[1].green == 3
    assert game.rounds[1].blue == 4
    assert game.rounds[2].red == 0
    assert game.rounds[2].blue == 1
    assert game.rounds[2].green == 1


@pytest.mark.parametrize(
    "game, possible",
    [
        (game, n in POSSIBLE_GAMES)
        for n, game in enumerate(EXAMPLE.splitlines(), start=1)
    ],
)
def test_game_check_possibility(game, possible):
    assert Game.parse_from_text(game).check_possible(POSSIBILITY_CONDITION) == possible


def test_find_possible_games():
    assert (
        set(find_possible_games(EXAMPLE.splitlines(), POSSIBILITY_CONDITION))
        == POSSIBLE_GAMES
    )


def test_game_cubes_required():
    game = Game.parse_from_text(
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    )
    assert game.cubes_required() == Cubes(1, 3, 4)


def test_find_cube_powers():
    assert find_cube_powers(EXAMPLE.splitlines()) == CUBE_POWERS
