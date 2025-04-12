#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_files(path="./"):
    file_list = os.listdir(path)
    file_names = []
    for item in file_list:
        if os.path.isfile(item):
            file_names.append(item)
    return file_names


if __name__ == '__main__':
    print(get_files())
