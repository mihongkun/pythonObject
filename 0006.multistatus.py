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

    def self_introduction(self):
        print('My name is %s.\nI am %s years old.' % (self.name, self._age))


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My name is %s .\nMy favorite language is %s.' % (self.name, self.language))


def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    programer = Programer('mihongkun', 25, 80)
    backend_programer = BackendProgramer('mihongkun-backend', 25, 80, 'Python')
    introduce(programer)
    introduce(backend_programer)
