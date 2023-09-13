from brain_games.cli import welcome_user

def is_win(wins_count, answer, correct_answer, game):
    GAMES_TO_WIN = 3
    if wins_count == GAMES_TO_WIN and str(answer) == str(correct_answer):
        print('Correct!')
        return True
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    elif str(answer) == str(correct_answer) and wins_count < GAMES_TO_WIN:
        print('Correct!')
        return game(wins_count + 1)


def game_result(name, result):
    if result is False:
        print(f'Let\'s try again, {name}!')
    if result is True:
        print(f'Congratulations, {name}!')

def game(current_game):
    name = welcome_user()
    result = current_game(start_wins_count=1)
    game_result(name, result)