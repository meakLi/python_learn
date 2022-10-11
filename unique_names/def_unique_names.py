"""
author：小李不吃西红柿
time：2022.10.11
"""
# def unique_names(name1, name2):
#     # lis = []
#     # for item in names1:
#     #     # print(item)
#     #     lis.append(item)
#     for item2 in name2:
#         # print(item2)
#         if item2 not in name1:
#             name1.append(item2)
#     return name1
#
#
# if __name__ == "__main__":
#     names1 = ["Ava", "emma", "olivia"]
#     names2 = ["olivia", "sophia", "emma"]
#     print(unique_names(names1, names2))


# class UniqueNames(object):
#     names1 = ["Ava", "emma", "olivia"]
#     names2 = ["olivia", "sophia", "emma"]
#
#     def __init__(self, names1, names2):
#         self.names1 = names1
#         self.names2 = names2
#
#     def solution(self,names1,names2):
#         for item in self.names1:
#             if item not in self.names2:
#                 self.names2.append(item)
#         print(self.names1)
#
#
# t1 = UniqueNames()
# t1.solution()


# class Person(object):
#     name = "meak"
#     age = 18
#
#     def __init__(self):
#         self.name = "meak"
#         self.age = 18
#
#     def printf(self):
#         print(f"{self.name}的年龄是{self.age}")
#
#
# P1 = Person()
# P1.printf()


# class UniqueNames(object):
#     names1 = ["Ava", "emma", "olivia"]
#     names2 = ["olivia", "sophia", "emma"]
#
#     # def __init__(self, names1, names2):
#     #     self.names1 = names1
#     #     self.names2 = names2
#     #     print(self.names1)
#     #     print(self.names2)
#     def solution(self):
#         print(1)
#         for item in self.names2:
#             if item not in self.names1:
#                 self.names1.append(item)
#         print(self.names1)
#
#
# t1 = UniqueNames()
# t1.solution()

# class MyClass:
#     """this is a example class"""
#     age = 19
#     def fun(self):
#         return 'hello world'
#
# # 类的实例化
# x = MyClass()
#
# # 访问类的属性和方法
# print("MtClass类的属性i为：",x.age)
# print("MtClass类的方法fun为：",x.fun())

# 类的定义
# class People:
#     # 定义基本属性
#     name = ''
#     age = 18
#     # 定义私有属性
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speck(self):
#         print(f"{self.name}说{self.age}岁")
#
# p = People('meak',99,77)
# p.speck()
# print(p.age)
# print(People.age)


# 将两个列表合成一个列表，重复的部分只保留一个
class UniqueNames:
    # 基本属性，调用类属性用到
    name = 'meak'
    age = 18

    # 构造方法，构造实例对象之后，首先调用实例方法
    def __init__(self):
        # 类属性
        self.names1 = ["Ava", "emma", "olivia"]
        self.names2 = ["olivia", "sophia", "emma"]

    def solution(self):
        for item in self.names2:
            if item not in self.names1:
                self.names1.append(item)
        print(self.names1)
        return self.names1


P1 = UniqueNames()
lis = P1.solution()
print(lis)
