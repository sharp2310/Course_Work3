from src.classes import Operation
from src.utils import get_data
import datetime


def main():
    # Берём данные из файла
    data = get_data()
    executed_operations = []
    sorted_list = []

    # Берём все выполненные операции
    for i in range(len(data) - 1):
        if data[i] == {}:
            continue
        if data[i]["state"] == "EXECUTED":
            executed_operations.append(data[i])
        else:
            continue

    # Сортируем по датам
    for i in range(len(executed_operations) - 1):
        unsorted_operation = Operation(executed_operations[i])

        executed_operations[i]['date'] = unsorted_operation.get_date()

    executed_operations = sorted(executed_operations, key=lambda k: '.'.join(reversed(k['date'].split('.'))))

    # Берем последние пять операций
    executed_operations.reverse()
    new_operations = executed_operations[:5]

    # Запускаем цикл и выводим на экран данные, соответствующие заданию

    for i in range(len(new_operations)):
        operation = Operation(new_operations[i])
        date = new_operations[i]['date']
        description = new_operations[i]["description"]
        amount = new_operations[i]["operationAmount"]["amount"]
        currency_name = new_operations[i]["operationAmount"]["currency"]["name"]

        if "from" in new_operations[i]:
            sender = operation.encrypt_bill()[0]
            receiver = operation.encrypt_bill()[1]
            print(f'{date} {description}\n'
                  f'{sender} -> {receiver}\n'
                  f'{amount} {currency_name}\n')
        else:
            receiver = operation.encrypt_bill()
            print(f'{date} {description}\n'
                  f'{receiver}\n'
                  f'{amount} {currency_name}\n')

if __name__ == '__main__':
    main()