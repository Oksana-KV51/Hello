#пишите программу на Python, которая запрашивает у пользователя
# # числа до тех пор, пока не будет введен 0, и затем выводит сумму введенных чисел.

n = None
sum = 0

while n != 0:
    n = float(input("введите число"))
    sum += n

print(sum)