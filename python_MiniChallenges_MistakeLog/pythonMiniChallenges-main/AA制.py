# 你的任务是计算每位顾客的应付金额

total_friends = int(input())
total_bill = float(input())

total_bill += 0.2 * total_bill  # 在账单小计上加上20%的税

share = total_bill/total_friends

print(share)
