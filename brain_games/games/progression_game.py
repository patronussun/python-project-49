#!/usr/bin/env python3
import prompt
from brain_games.utils import get_random_int
from brain_games.games.common import is_win


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
    games_to_win = 3
    progression = get_progression()
    index, correct_answer = get_hidden_element(progression)
    question = generate_question(progression, index)

    print('What number is missing in the progression?')
    print(f'Question: {question}')

    answer = prompt.string('Your answer: ')

    result = is_win(start_wins_count, games_to_win, answer, correct_answer, brain_progression)
    return result
