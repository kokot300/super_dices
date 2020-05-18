#!/usr/bin/python3

import dices_lib as dl


def main():
    """
    main function for program. function is practically an infinite loop that makes user introduce kind of throw
    and displays points scored.
    :return: None
    """
    print('Format: xDy+z \nx - how many throws y - size of the dice z - what to sum to the result')
    while True:
        kind_of_throw = input('tell me what do you want to throw: \n')


        standarized_throw = dl.throw_validator(kind_of_throw)
        print(standarized_throw)

        # try:
        #     int(standarized_throw[0])
        #     int(standarized_throw[1])
        #     int(standarized_throw[2])
        #     print('input correct')
        # except TypeError:
        #     print('you messed up the input. please try again')
        #     continue
        # if len(standarized_throw) != 3:
        #     print('something is rotten in the state of Denmark')
        #     continue
        # print(dl.lets_throw(standarized_throw))


if __name__ == '__main__':
    main()
