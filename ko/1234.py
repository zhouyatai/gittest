#/user/bin/python
#-*-coding:utf-8-*-

import pymysql
import xlrd

d = pymysql.connect(
                host = '192.168.10.64',
                port = 3306,
                user = 'root',
                passwd = '123456',
                charset = 'utf8'
                )

e = d.cursor()

sql_1 = 'create database yu'
e.execute(sql_1)
sql = ("use yu")
e.execute(sql)
sql_2 = "create table ppp (name char(10),sex char(10))"
e.execute(sql_2)


a = xlrd.open_workbook(filename=r'C:\Users\zyt\Desktop\1.xlsx')
table = a.sheets()[0]
for i in range(table.nrows):
    t = table.row_values(i)
    sql5 = ("insert into ppp(name,sex) values (%s,%s)")
    e.execute(sql5,(t[0],t[1]))