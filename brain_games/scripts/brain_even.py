#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import welcome_user


def get_random_int(min=1, max=100):
    return random.randint(min, max)


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    result_even = is_even(number)
    return 'yes' if result_even is True else 'no'


def brain_even(wins_count):
    games_to_win = 3
    random_num = get_random_int(max=100)

    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_num}')

    answer = prompt.string('Your answer: ')

    correct_answer = get_correct_answer(random_num)

    if wins_count == games_to_win:
        return True
    if str(answer) == str(correct_answer) and wins_count < games_to_win:
        print('Correct')
        return brain_even(wins_count + 1)
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def game():
    name = welcome_user()
    start_with = 1
    result = brain_even(start_with)
    if result is False:
        print(f'Let\'s try again, {name}!')
    if result is True:
        print(f'Congratulations, {name}!')


def main():
    game()


if __name__ == '__main__':
    main()
