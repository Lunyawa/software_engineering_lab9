#!/usr/bin/env python 3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    my_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    new_dict = {value: key for key, value in my_dict.items()}
    print("Исходный словарь:\n", my_dict)
    print("\n\nОбратный словарь:\n", new_dict)