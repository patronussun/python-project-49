import prompt
from brain_games.cli import welcome_user
import games

GAMES_TO_WIN = 3

def run_game(game):
    question, correct_answer = game.generate_round()
    name = welcome_user()

    print(games.DESCRIPTION)
    print(question)

    answer = prompt.string('Your answer: ')

    if game.wins_count == GAMES_TO_WIN and str(answer) == str(correct_answer):
        print('Correct!')
        print(f'Congratulations, {name}!')
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f'Let\'s try again, {name}!')
    elif str(answer) == str(correct_answer) and game.wins_count < GAMES_TO_WIN:
        print('Correct!')
        return game(game.wins_count + 1)
