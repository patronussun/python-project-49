from brain_games.utils import get_random_int
from brain_games.common import make_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    result_even = is_even(number)
    return 'yes' if result_even is True else 'no'


def generate_round():
    random_num = get_random_int(end_with=100)
    correct_answer = get_correct_answer(random_num)
    question = f'Question: {random_num}'

    return (question, correct_answer)


def brain_even(start_wins_count):
    print(DESCRIPTION)
    question, correct_answer = generate_round()

    result = make_game(start_wins_count, question, correct_answer, brain_even)
    return result
