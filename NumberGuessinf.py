import random


def user_guessed_number(lower_limit, higher_limit):
    user_guessed = int(input('guess the number between {} to {} : '.format(lower_limit, higher_limit)))
    return user_guessed


if __name__ == '__main__':
    low_limit = 1
    high_limit = 100
    chances = 5
    actual_number = random.randint(low_limit, high_limit)
    previous_guessed_number = 0

    while chances:
        print('{} chances are remaining for guessing the correct number'.format(chances))
        if chances != 5:
            print('previous guessed number is {}'.format(previous_guessed_number))
        guessed_number = user_guessed_number(low_limit, high_limit)
        if guessed_number == actual_number:
            print('you guessed the correct number and guessed number is {}'.format(guessed_number))
            break
        elif guessed_number < actual_number - 2:
            print('too low')
        elif guessed_number > actual_number + 2:
            print('too high')
        else:
            print('near to correct number')

        chances -= 1
        previous_guessed_number = guessed_number

    if chances == 0:
        print('OOPS! Better Luck Next Time!')
