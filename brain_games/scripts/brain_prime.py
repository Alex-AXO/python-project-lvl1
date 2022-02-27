#!/usr/bin/env python3

from brain_games.games import common            # импорт модулей игр


def main():
    player_name = common.get_name()
    common.hello_name(player_name)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < 3:
        count += 1
        result = common.question_prime(player_name)
        if result == 'Correct!':
            print(result)
        else:
            print(result)
            return
    common.congratulations(player_name)


if __name__ == '__main__':
    main()
