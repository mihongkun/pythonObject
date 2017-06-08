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

    def self_infermation(self):
        print('My name is %s.\nI am %s years old!' % (self.name, self._age))


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language


if __name__ == '__main__':
    programer = BackendProgramer('mihongkun', 25, 80, 'Python')
    print(type(programer))
    print(dir(programer))
    print(programer.__dict__)
    print(isinstance(programer, Programer))
