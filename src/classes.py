from src.utils import split_text_numbers, encrypt_bill_num
import datetime


class Operation:
    def __init__(self, operation_data):
        self.operation_data = operation_data

    def get_date(self):
        """
        Метод переделывает формат даты

        """
        operation_time = self.operation_data['date']
        change_time = operation_time.split('T')
        operation_time_new = " ".join(change_time)
        date_time_obj = datetime.datetime.strptime(operation_time_new, '%Y-%m-%d %H:%M:%S.%f')
        new_time = date_time_obj.strftime('%d.%m.%Y')
        return new_time

    def encrypt_bill(self):
        """
        Шифрование реквизитов
        """
        if "from" in self.operation_data:
            sender = split_text_numbers(self.operation_data["from"])
            receiver = split_text_numbers(self.operation_data["to"])

            sender[1] = encrypt_bill_num(sender[1])
            receiver[1] = encrypt_bill_num(receiver[1])

            sender_new = " ".join(sender)
            receiver_new = " ".join(receiver)

            return sender_new, receiver_new

        else:
            receiver = split_text_numbers(self.operation_data["to"])
            receiver[1] = encrypt_bill_num(receiver[1])

            receiver_new = " ".join(receiver)

            return receiver_new