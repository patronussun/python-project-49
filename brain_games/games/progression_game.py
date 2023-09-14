from brain_games.utils import get_random_int
from brain_games.common import make_game


def get_progression():
    step = get_random_int(end_with=5)
    length = get_random_int(start_with=5, end_with=10)
    first_number = get_random_int(end_with=20)
    progression = []
    for number in range(length):
        progression.append(first_number + number * step)

    return progression


def get_hidden_element(progression):
    index = get_random_int(end_with=len(progression) - 1)
    return (index, progression[index])


def generate_question(progression, index):
    progression[index] = '..'
    return ' '.join(str(item) for item in progression)


def brain_progression(start_wins_count):
    progression = get_progression()
    index, correct_answer = get_hidden_element(progression)
    progression_with_missing_index = generate_question(progression, index)

    print('What number is missing in the progression?')
    question = f'Question: {progression_with_missing_index}'

    result = make_game(start_wins_count, question, correct_answer,
                       brain_progression)
    return result
