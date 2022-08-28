from math import factorial

n = int(input())
list_pascal = []
for i in range(n + 1):
        list_pascal.append(round(factorial(n) / (factorial(i) * factorial(n - i))))
print(list_pascal)


