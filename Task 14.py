# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.  

# number = float(input('Введите вещественное число: '))
# def sumNum(number):
#     sum = 0
#     for i in str(number):
#         if i != ".":
#             sum += int(i)
#     return sum
# print(f"Сумма цифр = {sumNum(number)}")


number = float(input('Введите вещественное число: '))
integer_number = int(str(abs(number)).replace('.', ''))
sum = 0

while integer_number != 0:
    sum += integer_number % 10
    integer_number = integer_number // 10

# если введено отрицательное число, то и сумма будет отрицательной
if number > 0:
    print(f'{number} -> {sum}')
else:
    print(f'{number} -> {-sum}')




