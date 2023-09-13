import prompt
import math
from brain_games.utils import get_random_int
from brain_games.common import is_win


def get_gcd(first, second):
    return math.gcd(first, second)


def brain_gcd(start_wins_count):
    random_first = get_random_int(start_with=1, end_with=100)
    random_second = get_random_int(start_with=1, end_with=300)

    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {random_first} {random_second}')

    answer = prompt.string('Your answer: ')
    correct_answer = get_gcd(random_first, random_second)

    result = is_win(start_wins_count, answer, correct_answer, brain_gcd)
    return result
