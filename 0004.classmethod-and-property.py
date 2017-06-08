#!/usr/bin/env python3
# -*- coding=utf-8 -*-
class Programer(object):
    hobby = 'play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_information(self):
        print('My name is %s .\nI am %s years old.' % (self.name, self._age))


if __name__ == '__main__':
    programer = Programer('mihongkun', 25, 80)
    print(programer.get_weight)
    print(dir(programer))
    print(Programer.get_hobby())
    print(Programer.get_weight)
    print(programer.__dict__)
    programer.self_information()
