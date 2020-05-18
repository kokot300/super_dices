#!/usr/bin/python3

from random import randint
from re import split, findall


def dice_throw(kind_of_dice):
    return randint(1, kind_of_dice)


def lets_throw(throw_tulpe):
    result = 0
    number_of_throws = throw_tulpe[0]
    kind_of_dice = throw_tulpe[1]
    final_add = throw_tulpe[2]
    for i in range(number_of_throws):
        result += dice_throw(kind_of_dice)
    result += final_add
    return result


def throw_validator(user_wish='D66+-2'):
    throws_number = split("[d|D]", user_wish)[0]
    if throws_number == '':
        throws_number = '1'
    print('throws_number ', throws_number)

    kind_of_dice = split("[d|D]|[+|-]", user_wish)[1]
    if kind_of_dice == '':
        kind_of_dice = '6'
    print('kind_of_dice ', kind_of_dice)

    if findall("[+-]|[-+]", user_wish) == []:
        return print('some')
    elif findall("[+|-]", user_wish) == []:
        user_wish = user_wish + '+0'
    final_add = split("[+|-]", user_wish)[1]
    if final_add == '':
        final_add = '0'
    if findall('[-]', user_wish):
        final_add = '-' + final_add
    print(final_add)

    try:
        int(throws_number)
        int(kind_of_dice)
        int(final_add)
    except ValueError:
        print('input incorrect')


if __name__ == '__main__':
    throw_validator()
