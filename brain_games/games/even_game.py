from brain_games.utils import get_random_int
from brain_games.common import make_game


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    result_even = is_even(number)
    return 'yes' if result_even is True else 'no'


def brain_even(start_wins_count):
    random_num = get_random_int(end_with=100)

    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = f'Question: {random_num}'

    correct_answer = get_correct_answer(random_num)

    result = make_game(start_wins_count, question, correct_answer, brain_even)
    return result
