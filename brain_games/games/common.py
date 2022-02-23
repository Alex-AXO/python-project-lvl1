
import prompt
from random import randint                      # случайные числа
from math import gcd


def get_name():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    return player_name


def hello_name(name):
    print('Hello, ' + name + '!')


def congratulations(name):
    print(f'Congratulations, {name}!')


def incorrect_answer(answer, correct_answer, name):
    return f"'{answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\nLet's try again, {name}!"


def question_even(name):
    random_number = randint(1, 30)  # случайное число (включая крайние числа)
    print('Question:', random_number)
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer == 'yes' or (
        random_number % 2 != 0 and answer == 'no'
    ):
        return 'Correct!'
    else:
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return incorrect_answer(answer, correct_answer, name)


def question_calc(name):
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    operation = randint(1, 3)
    if operation == 1:
        print(f'Question: {number1} + {number2}')
        right_answer = number1 + number2
    if operation == 2:
        print(f'Question: {number1} - {number2}')
        right_answer = number1 - number2
    if operation == 3:
        print(f'Question: {number1} * {number2}')
        right_answer = number1 * number2
    answer = prompt.string('Your answer: ')
    if int(answer) == right_answer:
        return 'Correct!'
    else:
        return incorrect_answer(answer, right_answer, name)


def question_gcd(name):
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    print(f'Question: {number1} {number2}')
    answer = prompt.string('Your answer: ')
    right_answer = gcd(number1, number2)
    if int(answer) == right_answer:
        return 'Correct!'
    else:
        return incorrect_answer(answer, right_answer, name)
