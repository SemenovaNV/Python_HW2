# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

number = int(input('Введите целое число: '))
list_num = []

for i in range(- number,number +1):
    list_num.append(i)
print(list_num)

element1 = int(input('Введите позицию первого элемента: '))
element2 = int(input('Введите позицию второго элемента: '))
sum = list_num[element1-1]*list_num[element2-1]
print(f'Произведение выбранных элементов = {sum}')

