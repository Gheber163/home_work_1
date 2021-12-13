#задание 1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

#задание 2
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, el in enumerate(my_list):
    try:
        int(el)
        my_list[i] = "'" + el + "'"
    except ValueError: continue
print(*my_list)




