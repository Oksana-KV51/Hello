#Разработайте программу, которая использует цикл while для нахождения первых 20 чисел Фибоначчи.

a, b = 0, 1
count = 0
while count < 5:
    print(a)
    a, b = b, a + b
    count += 1

