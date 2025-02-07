# 将N个巧克力均分给M个儿童。假设巧克力的数量总是大于孩子的数量。Input：两个整数值

chocolates = int(input())
children = int(input())

choco_per_child = chocolates // children  #整除
choco_remain = chocolates % children  #余数

print(choco_per_child)
print(choco_remain)