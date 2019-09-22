#!/usr/bin/python
#-*-coding:utf-8-*-
##九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d * %d = %d'%(i,j,i*j), end=' ')
#     print(' ')
#
#字符串转整数型
# def a(s):
#     s = s[::-1]
#     n = 0
#     for i,j in enumerate(s):
#         t = '%s*1'%j
#         m = eval(t)
#         n += m*(10 ** i)
#         return n


#创建目录，文件删除文件，目录
import os
# a = os.mkdir('aaa')
# a1 = os.mkdir('a.txt')
# b = os.rmdir('aaa')
# print(a)
# print(a1)
# print(b)


# print(os.remove(r'D:\Users\zyt\AppData\Local\Programs\Python\Python37-32\python.exe E:/PycharmProjects/untitled1/ok/ko/aaa'))

#连接数据库，将a.out文件舔加到数据库中
import pymysql

d = pymysql.connect(host='192.168.10.122',
                    port=3306,
                    user = 'root',
                    passwd='123456',
                    charset='utf8',
                    database = 'yui')
e = d.cursor()
sql = "create table p (name char,id char,age char,asd char)"
e.execute(sql)

f=open(file='a.out',encoding='utf-8')