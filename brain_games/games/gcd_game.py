import math
from brain_games.utils import get_random_int
from brain_games.common import make_game


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first, second):
    return math.gcd(first, second)


def generate_round():
    random_first = get_random_int(start_with=1, end_with=100)
    random_second = get_random_int(start_with=1, end_with=300)

    question = f'Question: {random_first} {random_second}'
    correct_answer = get_gcd(random_first, random_second)
    return (question, correct_answer)


def brain_gcd(start_wins_count):
    question, correct_answer = generate_round()
    result = make_game(start_wins_count, question, correct_answer, brain_gcd)
    return result
