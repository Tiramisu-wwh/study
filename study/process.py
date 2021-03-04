def print1(a):
    if a == 1:
        print('ok')
        print('a is 1')


def print2(b):
    if b == 1:
        print('ok')
    print('a is 1')


print1(0)
print('-----------')
print2(0)

a = '记得一键三连'
if (n := len(a)) < 10:
    print(n)

x = 5
print(f'{x + 3}')
print(f'{x + 3 = }')

April = True
July = 5
print(April)
print(July == 5)
print(July > 1)

# elif就是else if的缩写

if x == 0:
    print('x is 0')
elif x < 0:
    print('x is less than 0')
else:
    print('x is more than 0')

# for循环结构：
# for...in...

a = [1, 2, 3, 4]
for x in a:
    print(x)
print('end1')

# while循环结构：
# while 表达式

i = 0
while i < 6:
    i += 1
    print(i)
print('end2')

a = [1, 2, 3, 4]
for x in a:
    if x == 3:
        continue
    print(x)
print('end3')

a = [1, 2, 3, 4]
for x in a:
    if x == 3:
        break
    print(x)
print('end4')

my_list = [1, 2, 3]
if (count := len(my_list)) >= 3:
    print(f"Error, {count} is too many items")



