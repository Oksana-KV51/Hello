#Создайте программу, которая выводит все числа от 1 до N, заменяя числа,
# #кратные 3, на "Fizz", числа, кратные 5, на "Buzz", и числа, кратные и 3, и 5, на "FizzBuzz".

n = float(input("введите число: "))
if n%3 == 0 and n%5 == 0:
    print("FizzBuzz")
elif n%5 == 0:
    print("Buzz")
elif n%3 == 0:
    print("Fizz")
else:
    print(n)
