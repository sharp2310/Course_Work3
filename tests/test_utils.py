from src.utils import get_data, split_text_numbers, encrypt_bill_num


def test_get_data():
    assert type(get_data()) == list
    assert type(get_data()[1]) == dict


def test_split_text_numbers():
    assert split_text_numbers("Счет 24763316288121894080") == ['Счет', '24763316288121894080']
    assert split_text_numbers('Visa Platinum 2256483756542539') == ['Visa Platinum', '2256483756542539']


def test_check_bill_name():
    assert encrypt_bill_num('24763316288121894080') == '**4080'
    assert encrypt_bill_num('2256483756542539') == '2256 48** **** 2539'