import prompt
import math
from brain_games.utils import get_random_int
from brain_games.games.common import is_win


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
    games_to_win = 3
    random_num = get_random_int(end_with=100)

    print('Answer "yes" if the number is prime, otherwise answer "no".')
    print(f'Question: {random_num}')

    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_num)

    result = is_win(start_wins_count, games_to_win, answer, correct_answer,
                    brain_prime)
    return result
