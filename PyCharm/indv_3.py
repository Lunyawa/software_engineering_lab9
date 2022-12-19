#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime as DT

if __name__ == '__main__':
    # Список успеваемости
    humans = []

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
            number = input('введите номер телефона: ')
            temp = input('Ваша дата рождения (dd/mm/yy): ')
            birthday = DT.datetime.strptime(temp, '%d/%m/%Y').date()


            # Создать словарь.
            human = {
                'FIO': FIO,
                'number': number,
                'date': birthday,
            }

            # Добавить словарь в список.
            humans.append(human)
            # Отсортировать список в случае необходимости.
            if len(human) > 1:
                humans.sort(key=lambda item: item.get('date'))

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
                    "номер телефона",
                    "дата рождения"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, human in enumerate(humans, 1):
                print(
                    '| {:>4} | {:<20} | {:<20} | {}      |'.format(
                        idx,
                        human.get('FIO', ''),
                        human.get('number', 0),
                        human.get('date')
                    )
                )
            print(line)

        elif command == 'find':
            count = 0
            find = input("Введите номер телефона человека ")
            for human in humans:
                if human.get('number') == find:
                    count += 1
                    print(
                        f"ФИО: {human.get('FIO', '')}\n"
                        f"номер: {human.get('number', '')}\n"
                        f"дата рождения: {human.get('date', '')}\n"

                    )
            if count == 0:
                print("человек с этим номером не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("find - вывод человека номер которого запросили ;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)