# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
with open('workers.txt', 'r', encoding='utf-8') as worker_list:
    worker_str = (i.split() for i in worker_list)
    worker_dict = {a[0]: a[1] for a in worker_str}
    print(f'перевел строки из файла в словарь: {worker_dict}')
    worker_min = [i for i in worker_dict if float(worker_dict[i]) < 20000]
    print(f'сотрудники с окладом менее 20 тысяч: {worker_min}')
    print(f'средняя зарплата сотрудников: {round(sum([float(i) for i in worker_dict.values()]) / len(worker_dict), 2)}')