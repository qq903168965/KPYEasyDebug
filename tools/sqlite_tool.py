#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from tools.file_tool import *


def create_db():
    try:
        database_name = get_main_db_path()

        # 先检查文件是否存在
        db_existed = os.path.exists(database_name)

        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()

        # 检查是否有表存在
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if db_existed:
            if tables:
                print(f"数据库已存在且包含 {len(tables)} 个表: {database_name}")
            else:
                print(f"数据库已存在但不包含任何表: {database_name}")
        else:
            print(f"新建数据库文件: {database_name}")
            if tables:  # 理论上新建的数据库不应该有表
                print(f"警告: 新建的数据库包含 {len(tables)} 个表")

        connection.close()

    except sqlite3.Error as error:
        print("数据库错误: ", error)


if __name__ == '__main__':
    create_db()
