from src.classes import Operation

operation = Operation({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
})

second_operation = Operation({
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
        "amount": "79931.03",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  })


def test_new_time():
    assert operation.get_date() == "26.08.2019"


def test_encrypt_bill():
    assert operation.encrypt_bill() == ("Maestro 1596 83** **** 5199", "Счет **9589")
    assert second_operation.encrypt_bill() == ("Счет **6215")