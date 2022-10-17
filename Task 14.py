# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.  

number = float(input('Введите вещественное число: '))
def sumNum(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum
print(f"Сумма цифр = {sumNum(number)}")







