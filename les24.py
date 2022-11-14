List = []
n = int(input('Введите кол-во строк матрицы'))
m = int(input('Введите кол-во столбцов матрицы'))
list1 = []
for i in range(n):
    list2 = []
    list1.append(list2)
    for j in range(m):
        a = int(input())
        list2.append(a)
for i in list1:
    print(i) #матрица
for i in range(len(list1)):
    print(list1[i][i]) #'главная диагональ'
print('максимальное число по главной диагонали', max(list1[i][i] for i in range(len(list1))))
for i in range(len(list1)):
    print(list1[i][-i-1]) #побочная диагональ
print('максимальное число по побочной диагонали', max(list1[i][-i-1] for i in range(len(list1))))


