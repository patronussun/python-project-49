import math
from brain_games.utils import get_random_int


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first, second):
    return math.gcd(first, second)


def generate_round():
    random_first = get_random_int(start_with=1, end_with=100)
    random_second = get_random_int(start_with=1, end_with=300)

    question = f'Question: {random_first} {random_second}'
    correct_answer = get_gcd(random_first, random_second)
    return (question, correct_answer)
