#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random
import numpy as np
from dao.dbconnect import open_db_connection2, close_db_connection
# 范围时间
# d_time = datetime.datetime.strptime('2019-03-01', '%Y-%m-%d')
# d_time1 = datetime.datetime.strptime('2019-03-31', '%Y-%m-%d')

d_time = datetime.datetime.strptime('00:%d:00'%(1), '%H:%M:%S').time()
d_time1 = datetime.datetime.strptime('23:59:59', '%H:%M:%S')
dtime = datetime.datetime.now()

print(d_time)

# # 当前时间
# n_time = datetime.datetime.now().time()
#
# # 判断当前时间是否在范围时间内
# if n_time >= d_time and n_time <= d_time1:
#     print("True")
# else:
#     print("False")

print(random.random())

d = dict()
d[1] = [1,2,3]
d[3] = [2,3,4,5,6]
print(d[3][3])
a = [1]
print(a)
a = [a]
print(a)

x_sdjf = a
list = [[1,2],[2,3],[3,4]]
print(np.mean(np.array(list), axis=0))

y = 1
def fun(y):
    y = 2
print(y)
fun(y)
print(y)

cnn = open_db_connection2()
# 插入路程安排到数据库
# 使用cursor()方法获取操作游标
cursor = cnn.cursor()
# SQL插入语句
#q = "insert into schedule(conditions,driverid,latitude,longitude,remain) values (%d,%d,%f,%f,%d)"%(1,1,1,1,1)
q = "insert into schedule(conditions,driverid,latitude,longitude,remain,time) values (" + str(1) + "," + str(2) + "," + str(2) + "," + str(2) + "," + str(2) + ", str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))"%(dtime.strftime("%Y-%m-%d %H:%M:%S"))
# try:
#     # 执行sql语句
#     # cursor.execute(q)
#     # # 提交到数据库执行
#     # cnn.commit()
#     recount = cursor.execute("select * from schedule")
#     rows = cursor.fetchall()
#     cursor.close()
#     close_db_connection(cnn)
#     for row in rows:
#         print(row)
# # except:
# #     # Rollback in case there is any error
# #     cnn.rollback()
# #     print("halo")
# 执行sql语句
cursor.execute(q)
# 提交到数据库执行
cnn.commit()
cnn.close()