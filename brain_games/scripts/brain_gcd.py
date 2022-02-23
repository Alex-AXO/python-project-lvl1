#!/usr/bin/env python3

from brain_games.games import common            # импорт модулей игр


def main():
    player_name = common.get_name()
    common.hello_name(player_name)
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < 3:
        count += 1
        result = common.question_gcd(player_name)
        if result == 'Correct!':
            print(result)
        else:
            print(result)
            return
    common.congratulations(player_name)


if __name__ == '__main__':
    main()
