#!/usr/bin/python
# -*- coding:utf8 -*-
i = input('输入一个大于等于3的整数：')   # 第3项加了1次，第i项要加i-2次
i = i - 2   # i用于计算加的次数
if i >= 1:
    print 1
    print 1
    a = 1
    b = 1
    for i in xrange(i):
        c = a + b
        a = b   # 斐波纳契数列的前n项的重点在于发现：下一项的a是上一项的b；下一项的b是上一项的c(要打个草稿）
        b = c   # 体现了计算机迭代的思想
        print c

else:
    print '输入一个大于等于3的整数：'