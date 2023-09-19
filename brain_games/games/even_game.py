from brain_games.utils import get_random_int


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
