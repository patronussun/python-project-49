import random
from brain_games.utils import get_random_int
from brain_games.common import make_game


DESCRIPTION = 'What is the result of the expression?'


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


def get_random_math():
    return random.choice(['+', '-', '*'])


def brain_calc(start_wins_count):
    random_first = get_random_int(start_with=5, end_with=10)
    random_second = get_random_int(start_with=0, end_with=5)
    random_sign = get_random_math()

    print(DESCRIPTION)
    question = f'Question: {random_first} {random_sign} {random_second}'

    correct_answer = get_correct_answer(random_first,
                                        random_second, random_sign)

    result = make_game(start_wins_count, question, correct_answer, brain_calc)
    return result
