import prompt
from brain_games.utils import get_random_int
from brain_games.common import is_win


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    result_even = is_even(number)
    return 'yes' if result_even is True else 'no'


def brain_even(start_wins_count):
    random_num = get_random_int(end_with=100)

    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_num}')

    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_num)

    result = is_win(start_wins_count, answer, correct_answer, brain_even)
    return result
