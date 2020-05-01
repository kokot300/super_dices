#!/usr/bin/python3

from random import randint


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


def find_x(usr_str):
    x = 0
    for i in usr_str:
        if i == 'd':
            break
        elif i == 'D':
            break
        else:
            try:
                x += int(i)
                return x
            except:
                return 'unable to find x'


def find_y(usr_str):
    y = 0

    for i in range(len(usr_str)):
        if usr_str[i] == 'd' or usr_str[i] == 'D':
            starting_point = i + 1
            break
        else:
            starting_point = 0

    if starting_point == 0:  # might be referenced before assignment, but no idea how
        return 'unable to find y'
    short_str = usr_str[starting_point:]
    for i in short_str:
        try:
            y += int(i)
        except:
            # y = 'unable to find y'
            break
    if y == 0:
        y = 'unable to find y'
    return y


def find_z(usr_str):
    if len(usr_str.split('+')) == 2:
        lst = usr_str.split('+')
    elif len(usr_str.split('-')) == 2:
        lst = usr_str.split('-')
        usr_str = str(lst[0] + '+-' + lst[1])
        lst = usr_str.split('+')
    else:
        usr_str = usr_str + '+0'
        lst = usr_str.split('+')

    z = lst[1]
    try:
        z = int(z)
        return z
    except:
        return 'format for z is incorrect!'


def input_checker(usr_str):
    ok_flag = True
    allowed_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'd', 'D', '+', '-']
    for i in usr_str:
        for ii in allowed_chars:
            if i == ii:
                ok_flag = True
                break
            else:
                ok_flag = False
        if ok_flag == False:
            return ok_flag
    return ok_flag


def throw_standardizer(usr_str):
    ok_flag = input_checker(usr_str)
    if ok_flag == False:
        return 'input incorrect', 'input incorrect', 'input incorrect'
    x = find_x(usr_str)
    y = find_y(usr_str)
    z = find_z(usr_str)
    return x, y, z
    # if len(usr_str.split('+')) == 2:
    #     lst = usr_str.split('+')
    # elif len(usr_str.split('-')) == 2:
    #     lst = usr_str.split('-')
    #     usr_str = str(lst[0] + '+-' + lst[1])
    #     lst = usr_str.split('+')
    # else:
    #     usr_str = usr_str + '+0'
    #     lst = usr_str.split('+')
    #
    # z=lst[1]
    # try:
    #     z=int(z)
    # except:
    #     exit('format for z is incorrect!')
    #
    # xy=lst[0]
    # if len(xy.split('d')) == 2:
    #     xy=xy.split('d')
    #     x=xy[0]
    #     y=xy[1]
    # elif len(xy.split('D')) == 2:
    #     xy = xy.split('D')
    #     x = xy[0]
    #     y = xy[1]
    # else:
    #     xy='0'+xy
    #     if len(xy.split('d')) == 2:
    #         xy = xy.split('d')
    #         x = xy[0]
    #         y = xy[1]
    #     elif len(xy.split('D')) == 2:
    #         xy = xy.split('D')
    #         x = xy[0]
    #         y = xy[1]
    # return x, y, z
