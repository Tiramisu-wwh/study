# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
dict = {}
dict['one'] = 'April'
dict[2] = 22

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}


print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values())  # 输出所有值


April = {x: x**2 for x in (2, 4, 6)}
print(April)
