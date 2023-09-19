import math
from brain_games.utils import get_random_int


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'


def generate_round():
    random_num = get_random_int(end_with=100)
    question = f'Question: {random_num}'
    correct_answer = get_correct_answer(random_num)
    return (question, correct_answer)
