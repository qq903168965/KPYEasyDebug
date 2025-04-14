#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from tools.file_tool import *


class SqlLiteDb(object):

    def __init__(self):
        self._connection = None

    def __enter__(self):
        self.create_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        self._connection.close()
        print("数据库关闭")
        if exc_type is not None:
            # 处理异常
            print(f"Exception: {exc_type}, {exc_val}")
        return False

    def create_db(self):
        try:
            database_name = get_main_db_path()
            # 先检查文件是否存在
            db_existed = os.path.exists(database_name)
            self._connection = sqlite3.connect(database_name)
            cursor = self._connection.cursor()
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
            # connection.close()

        except sqlite3.Error as error:
            print("数据库错误: ", error)

    def execute_sql(self, str=None):
        reuslt = self._connection.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(reuslt)


if __name__ == '__main__':
    with SqlLiteDb() as db:
        db.execute_sql()


