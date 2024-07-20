number_of_homework = 12
number_of_hours_spent = 1.5
course_name = 'Python' #Изменение для Git
time_per_task = number_of_hours_spent/number_of_homework
print('Курс:', course_name + ",", 'всего задач:', str(number_of_homework) + ",",
      'затрачено часов:', str(number_of_hours_spent) + ",", 'среднее время выполнения',
      time_per_task, 'часа') # Чтобы убрать пробел между числом и запятой нужно привести их к одному типу
