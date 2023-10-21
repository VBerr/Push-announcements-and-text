numbers = []

for i in range(10):
    num = int(input("请输入第{}个数：".format(i + 1)))
    numbers.append(num)

sum1 = sum(numbers)
sum2 = sum1 - max(numbers) - min(numbers)
result = sum2 / 8
print(result)