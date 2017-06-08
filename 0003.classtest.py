#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Test(object):
    def test(self):
        return 'hi'


if __name__ == '__main__':
    a = Test()
    print(a.test)

    a.test = 'hello world'
    print(a.test)
    print(a.__dict__)
