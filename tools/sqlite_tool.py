#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


def create_db(database_name="../db/KPYEasyDebug.db"):
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if len(tables) > 0:
            print("数据库 {} 存在。".format(database_name))
        else:
            print("数据库 {} 不存在，已新建。".format(database_name))

        connection.close()

    except sqlite3.Error as error:
        print("数据库错误: ", error)


if __name__ == '__main__':
    create_db("KPYEasyDebug.db")
