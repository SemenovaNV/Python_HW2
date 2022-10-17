# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

number = int(input('Введите целое число: '))
sequence = []
sum_sequence = 0

for i in range(1, number+1):
    calculation = round((1 + 1 / i)**i, 2)
    sequence.append(calculation)
    sum_sequence += calculation
    
print (f' Список из {number} чисел последовательности (1+1/n)^n  = {sequence}')
print (f' Сумма чисел этой последовательности = {sum_sequence}')
