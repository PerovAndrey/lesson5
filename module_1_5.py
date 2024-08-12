# food = ['apple', 'coconut', 'banana']
# print(food)
# food[0] = 'peach'
# print(food)
# food.append(True)
# print(food)
# food.extend(["string", 2])
# print(food)
# food.remove('peach')
# print(food)
# print('coconut' in food)
# print('banana' not in food)
# print(food[1:4:2])

# tuple_ = 1, 2, 3, 4, 5, True, "string"
# print(tuple_)
# tuple_1 = ([1, 2], 0)
# print(tuple_1)
# tuple_1[0][1] = 3
# print(tuple_1)

immutable_var = 5, 6, 7, "числа", False
print(immutable_var)
#immutable_var[1] = 9 # "Кортеж не изменяемая коллекция элементов, он не поддерживает обращение к элементам внутри себя"
print(immutable_var)
mutable_list = [9, 8, 7, "знаки", True]
print(mutable_list)
mutable_list[3] = False
mutable_list[1] = 5
print(mutable_list)