# 找出三个数字中最大/最小的一个

# My method 1：题目要求:找出三个数字中最小的一个
number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 < number2 and number1 < number3:
    print(number1)

elif number2 < number1 and number2 < number3:
    print(number2)

else: 
    print(number3)



# Method 2: 容器法
def max_min(x, y, z):
    max = min = x
    if y > max:
        max = y
    else:
        min = y

    if z > max:
        max = z
    else:
        min = z
    return (max, min)
 
print(max_min(15, 10, 39))
print(f'中间值={x + y + z - min - max}')



# Method 3: 上下限
a = int(input("请输入a的值:"))#Input录入的是字符，但我们使用的是整形，所以要类型转换一下
b = int(input("请输入b的值:"))
c = int(input("请输入c的值:"))
if(a < b):
    max = b
    min = a
else:
    max = a
    min = b
if(max < c):
    max = c
if(min > c):
    min = c
print("最小值:%d\t中间值:%d\t最大值:%d\n"%(min,a + b + c - min - max,max))
