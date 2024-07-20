immutable_var = ([1, 4], 'Tasty', False, (5, 12.4))
print(immutable_var)
#immutable_var[1] = 'apple' кортеж содержит не сам объект, а ссылку на него. Если менять объект
    #внутри кортежа то ссылка на него не изменится а соответственно кортеж останеся прежним.
    #чтобы поменять состав кортежа, нужно создать новый кортеж.
immutable_var[0][1] = 2
print(immutable_var)

mutable_list = [[1, 4], 'Tasty', False, [5, 12.4]]
print(mutable_list)
mutable_list[1] = 'apple'
mutable_list[3][1] = 13
print(mutable_list)
