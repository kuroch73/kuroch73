# 1.вывести числа в диапазоне кратные 7
# a = int(input("Start interval: "))
# b = int(input("End interval: "))
# for i in range(a,b+1):
#     if i % 7 == 0:
#         print(i)
# 2.
# a = int(input("Start interval: "))
# b = int(input("End interval: "))
# sum = 0
# for i in range(a,b+1):
#     print("весь список: ", i)
# for j in range(b,a-1,-1):
#     print("в обратном порядке: ", j)
# for k in range(a,b):
#     if k % 7 == 0:
#         print("число кратное 7: ", k)
# for l in range(a,b+1):
#     if l % 5 == 0:
#         sum += 1
# print("количество чисел кратных 5: " , sum)
# 3.
a = int(input("Start interval: "))
b = int(input("End interval: "))
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)
    else:
        None