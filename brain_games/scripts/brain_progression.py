#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.common import game_result
from brain_games.games.progression_game import brain_progression


def main():
    name = welcome_user()
    result = brain_progression(start_wins_count=1)
    game_result(name, result)


if __name__ == '__main__':
    main()
