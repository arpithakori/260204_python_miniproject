# Testing functions to test files exist or not
import currency_converter


def test_file():
    try:
        output = currency_converter.check_file('2021-04-29.txt')
        assert output.__eq__(True)
    except FileNotFoundError:
        print("No such file exists")
    except AssertionError:
        print("assert false")


def test_file_2():
    try:
        output = currency_converter.check_file('2021-04-30.txt')
        assert output.__eq__(True)
    except FileNotFoundError:
        print("No such file exists")
    except AssertionError:
        print("assert false")
