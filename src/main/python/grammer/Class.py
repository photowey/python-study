# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Class.py
# @description Class
# @author WcJun
# @date 2020/06/25
# ---------------------------------------------


class Person(object):

    def __init__(self, name):
        self.name = name
        self.__hidden_name = name

    def get_name(self):
        return self.name

    def get_hidden_name(self):
        return self.__hidden_name


person = Person("photowey")
print(person.name)
person.name = "hellwey"
print(person.name)

print(person.get_name())
print(person.get_hidden_name())
print(person._Person__hidden_name)
