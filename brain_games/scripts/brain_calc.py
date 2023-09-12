#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import welcome_user


def get_random_int(start_with=1, end_with=100):
    return random.randint(start_with, end_with)


def calc_result(first, second):
    return first + second


def get_correct_answer(first, second, sign):
    match sign:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case _:
            return 'wrong sign'


def brain_calc(wins_count):
    games_to_win = 3
    random_first = get_random_int(end_with=10)
    random_second = get_random_int(end_with=10)
    random_sign = random.choice(['+', '-', '*'])

    print('What is the result of the expression?')
    print(f'Question: {random_first} {random_sign} {random_second}')

    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_first,
                                        random_second, random_sign)

    if wins_count == games_to_win:
        return True
    if str(answer) == str(correct_answer) and wins_count < games_to_win:
        print('Correct')
        return brain_calc(wins_count + 1)
    elif str(answer) != str(correct_answer):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


def game():
    name = welcome_user()
    start_with = 1
    result = brain_calc(start_with)
    if result is False:
        print(f'Let\'s try again, {name}!')
    if result is True:
        print(f'Congratulations, {name}!')


def main():
    game()


if __name__ == '__main__':
    main()
