import prompt
from brain_games.cli import welcome_user

GAMES_TO_WIN = 3

def run_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)

    wins_count = 0
    while wins_count < 3: 
        question, correct_answer = game.generate_round()
        print(question)
        answer = prompt.string('Your answer: ')
    
        if str(answer) != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
            wins_count += 1
        
        print(f'Congratulations, {name}!')