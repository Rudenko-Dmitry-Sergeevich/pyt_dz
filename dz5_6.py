# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons_dict = {}
with open('lessons.txt', 'r', encoding='utf-8') as lessons_obj:
    for i in lessons_obj:
        lessons_dict[i.split(':')[0]] = sum([int(k) for k in ''.join(x for x in i if x.isdigit() or x == '(').split('(')[:-1]])
        q = sum([int(k) for k in ''.join(x for x in i if x.isdigit() or x == '(').split('(')[:-1]])
        w = i.split(':')[0]
#        q = ''.join(x for x in i if x.isdigit() or x == '(').split('(')[:-1]
#        s = ''.join(x for x in i if x.isdigit() or x == '(')

print(lessons_dict)

# Записал в одну строку:
with open('lessons.txt', 'r', encoding='utf-8') as lessons_obj:
    lessons_dict = {t.split(':')[0]: sum([int(k) for k in ''.join(x for x in t if x.isdigit() or x == '(').split('(')[:-1]]) for t
         in lessons_obj}
print(lessons_dict)