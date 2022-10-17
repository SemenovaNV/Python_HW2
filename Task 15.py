# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

number = int(input('Введите целое число: '))
product_numbers = 1
result_product_numbers = []
for i in range(1,number+1):
    product_numbers*=i
    result_product_numbers.append(product_numbers)
print(f'Набор произведений от 1 до {number} = {result_product_numbers}')