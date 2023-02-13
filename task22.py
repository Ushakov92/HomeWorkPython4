#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

#11 6
#2 4 6 8 10 12 10 8 6 4 2
#3 6 9 12 15 18
#6 12

print('Введите через пробел кол-во элементов первого и второго множества')
n,m = [int(x) for x in input().split()[:2]]  

print(f'Введите чисел через пробел: {n}')
list_1 = [int(x) for x in input().split()[:n]]
set_1 = set(list_1)

print(f'Введите чисел через пробел: {m}')
list_2 = [int(x) for x in input().split()[:m]]
set_2 = set(list_2)
print('Встречающиеся числа в обоих множествах')
print(*sorted(set_1.intersection(set_2)))