#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Минимум из чисел


def minimum(**kwargs):
    x = 0
    temp = []
    for array in kwargs.values():
        if isinstance(array, (float, int)):
            temp.append(float(array))
        else:
            for num in array:
                if isinstance(num, (float, int)):
                    temp.append(num)
    print('Минимум из чисел: ', min(temp))


if __name__ == '__main__':
    minimum(a=[5, -1, -2, -3], b='a', c=['abgf', 'asd'], d=[1, 2, 3])
