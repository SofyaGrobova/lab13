#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def individual_func(*args):
    if args:
        result = 0
        flag = 0
        for arg in args:
            if isinstance(arg, (float, int, str)):
                if float(arg) < 0:
                    flag += 1
                elif flag == 1:
                    result += float(arg)
        if flag == 1:
            result = 0
        return result
    else:
        return None


if __name__ == "__main__":
    print(individual_func())
    print(individual_func(-3, 7, 1, 6, -9))
    print(individual_func(1, -5, 8, -4, 3, 9, -4, 5, -6))
