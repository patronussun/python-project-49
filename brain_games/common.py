import prompt
from brain_games.cli import welcome_user


def make_game(wins_count, question, correct_answer, current_game):
    GAMES_TO_WIN = 3

    print(question)
    answer = prompt.string('Your answer: ')

    if wins_count == GAMES_TO_WIN and str(answer) == str(correct_answer):
        print('Correct!')
        return True
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    elif str(answer) == str(correct_answer) and wins_count < GAMES_TO_WIN:
        print('Correct!')
        return current_game(wins_count + 1)


def print_game_result(name, result):
    if result is False:
        print(f'Let\'s try again, {name}!')
    if result is True:
        print(f'Congratulations, {name}!')


def game(current_game):
    name = welcome_user()
    result = current_game(start_wins_count=1)
    print_game_result(name, result)
