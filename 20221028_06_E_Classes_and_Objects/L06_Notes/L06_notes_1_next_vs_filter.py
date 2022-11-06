# Lambda examples

tasks = ['Asen', 'Ivan', 'George', 'Scott Young']


print('\n-------- ex. 1 -----------\n')


tsk = filter(lambda x: x == 'Scott Young', tasks)

for el in tsk:
    print(el)


print('\n-------- ex. 2 -----------\n')


tsk = next(filter(lambda x: x == 'Scott Young', tasks))
print(tsk)


print('\n-------- ex. 3 -----------\n')


tsk = filter(lambda x: x, tasks)

for el in tsk:
    print(el)
