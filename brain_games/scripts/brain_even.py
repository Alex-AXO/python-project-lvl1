#!/usr/bin/env python3


from random import randint                      # случайные числа
import prompt                                   # функция типа input


def question():
    random_number = randint(1, 30)  # случайное число (включая крайние числа).
    print('Question:', random_number)
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer == 'yes' or random_number % 2 != 0 and answer == 'no':
        return 'Correct!'
    else:
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."


def main():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, ' + player_name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        count += 1
        result = question()
        if result == 'Correct!':
            print(result)
        else:
            print(result)
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')


if __name__ == '__main__':
    main()
