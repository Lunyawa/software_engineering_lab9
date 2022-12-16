#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список успеваемости
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input('>>> ').lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            FIO = input('Ваши фамилия и инициалы: ')
            group = input('введите номер своей группы: ')
            grade = int(input('Ваша успеваемость: '))

            # Создать словарь.
            student = {
                'FIO': FIO,
                'group': group,
                'grade': grade,
            }

            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(student) > 1:
                students.sort(key=lambda item: item.get(grade, ' '))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 20,
                '-' * 20,
                '-' * 15
                )
            print(line)
            print(
                '| {:^4} | {:^20} | {:^20} | {:^15} |'.format(
                    "No",
                    "ФИО.",
                    "номер группы",
                    "успеваемость"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<20} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('FIO', ''),
                        student.get('group', 0),
                        student.get('grade', 0)
                    )
                )
            print(line)

        elif command == 'find':
            count = 0
            for student in students:
                if (student.get('grade') == 4) or (student.get('grade') == 5):
                    count += 1
                    print(
                        f"ФИО: {student.get('FIO', '')}\n"
                        f"группа: {student.get('group', '')}\n"
                        f"успеваемость: {student.get('grade', '')}\n"

                    )
            if count == 0:
                print("студенты с оценками 4 и 5 не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("find - вывод на фамилий и номеров групп студента с оценками 4 и 5 ;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)