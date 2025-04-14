#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_main_db_path():
    """获取主目录下的数据库路径"""
    # 获取当前脚本的绝对路径
    script_path = os.path.abspath(__file__)

    # 找到主目录（假设主目录是脚本所在目录的父目录）
    main_dir = os.path.dirname(os.path.dirname(script_path))

    # 或者如果主目录就是脚本所在目录：
    # main_dir = os.path.dirname(script_path)

    # 构建数据库路径
    db_dir = os.path.join(main_dir, "db")
    db_path = os.path.join(db_dir, "KPYEasyDebug.db")

    # 确保目录存在
    os.makedirs(db_dir, exist_ok=True)
    return db_path


def get_files(path="./"):
    file_list = os.listdir(path)
    file_names = []
    for item in file_list:
        if os.path.isfile(item):
            file_names.append(item)
    return file_names


if __name__ == '__main__':
    print(get_files())
