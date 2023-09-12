def is_win(wins_count, games_to_win, answer, correct_answer, game):
    if wins_count == games_to_win and str(answer) == str(correct_answer):
        print('Correct!')
        return True
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    elif str(answer) == str(correct_answer) and wins_count < games_to_win:
        print('Correct!')
        return game(wins_count + 1)

    
def game_result(name, result):
    if result is False:
        print(f'Let\'s try again, {name}!')
    if result is True:
        print(f'Congratulations, {name}!')