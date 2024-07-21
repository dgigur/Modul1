dictionary = dict()
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)

#for i in range(len(grades)):
#    dictionary.update({students[i]: round(sum(grades[i])/len(grades[i]), 1)})
#print(dictionary)

AAron_index = students.index('Aaron')
Bilbo_index = students.index('Bilbo')
Johny_index = students.index('Johny')
Khendrik_index = students.index('Khendrik')
Steve_index = students.index('Steve')
AAron_average_mark = sum(grades[AAron_index])/len(grades[AAron_index])
Bilbo_average_mark = sum(grades[Bilbo_index])/len(grades[Bilbo_index])
Johny_average_mark = sum(grades[Johny_index])/len(grades[Johny_index])
Khendrik_average_mark = sum(grades[Khendrik_index])/len(grades[Khendrik_index])
Steve_average_mark = sum(grades[Steve_index])/len(grades[Steve_index])
dictionary.update({students[AAron_index]: AAron_average_mark})
dictionary.update({students[Bilbo_index]: Bilbo_average_mark})
dictionary.update({students[Johny_index]: Johny_average_mark})
dictionary.update({students[Khendrik_index]: Khendrik_average_mark})
dictionary.update({students[Steve_index]: Steve_average_mark})
print(dictionary)
