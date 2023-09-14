import math
from brain_games.utils import get_random_int
from brain_games.common import make_game


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'


def brain_prime(start_wins_count):
    random_num = get_random_int(end_with=100)

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question = f'Question: {random_num}'

    correct_answer = get_correct_answer(random_num)

    result = make_game(start_wins_count, question, correct_answer, brain_prime)
    return result
