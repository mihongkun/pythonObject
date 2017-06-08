# -*- encoding=utf-8 -*-

class OldObjecct:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NewObject(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


if __name__ == '__main__':
    old = OldObjecct('old', 'Old style class')
    print(old)
    print(type(old))
    print(dir(old))
    new = NewObject('new', 'New style class')
    print(new)
    print(type(new))
    print(dir(new))
