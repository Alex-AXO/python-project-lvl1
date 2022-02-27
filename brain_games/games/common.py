
import prompt
from random import randint                      # случайные числа
from math import gcd


# Вспомогательные функции


def get_name():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    return player_name


def hello_name(name):
    print('Hello, ' + name + '!')


def congratulations(name):
    print(f'Congratulations, {name}!')


def incorrect_answer(answer, correct_answer, name):
    return f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!"


def question_answer(question):
    print('Question: ' + question)
    answer = prompt.string('Your answer: ')
    return answer


def result(answer, right_answer, name):
    if str(answer) == str(right_answer):
        return 'Correct!'
    else:
        return incorrect_answer(answer, right_answer, name)


def is_prime(number):
    if number < 2:
        return 'no'
    a = 2
    while a <= int(number / 2):
        if number % a == 0:
            return 'no'
        a += 1
    return 'yes'


# Логика игр


def question_even(name):
    random_number = randint(1, 30)  # случайное число (включая крайние числа)
    answer = question_answer(str(random_number))

    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return result(answer, right_answer, name)


def question_calc(name):
    number1 = randint(1, 30)
    number2 = randint(1, 30)
    operation = randint(1, 3)

    if operation == 1:
        question = f'{number1} + {number2}'
        right_answer = number1 + number2
    if operation == 2:
        question = f'Question: {number1} - {number2}'
        right_answer = number1 - number2
    if operation == 3:
        question = f'Question: {number1} * {number2}'
        right_answer = number1 * number2

    answer = question_answer(question)
    return result(answer, right_answer, name)


def question_gcd(name):
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    answer = question_answer(f'{number1} {number2}')
    right_answer = gcd(number1, number2)

    return result(answer, right_answer, name)


def question_progression(name):
    lenght = randint(5, 12)
    start = randint(1, 20)
    step = randint(1, 5)
    hidden_number = randint(0, lenght)

    progression = ''
    a = 0
    element = start

    while a <= lenght:
        if a == hidden_number:
            progression += '.. '
            right_answer = element
        else:
            progression += str(element) + ' '
        a += 1
        element += step

    answer = question_answer(progression)
    return result(answer, right_answer, name)


def question_prime(name):
    number = randint(1, 100)
    answer = question_answer(str(number))
    # if is_prime(number):
    #     right_answer = 'yes'
    # else:
    #     right_answer = 'no'
    right_answer = is_prime(number)
    return result(answer, right_answer, name)
