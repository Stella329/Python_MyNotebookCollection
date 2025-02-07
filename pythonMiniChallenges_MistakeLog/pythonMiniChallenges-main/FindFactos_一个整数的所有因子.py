# 打印出一个数字的所有因子: 因子就是所有可以整除这个数的数,不包括这个数自身

number = int(input())

for i in range(1, number):
    modulo = number % i
    
    if modulo ==0:
        print(i)