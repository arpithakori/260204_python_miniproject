# Testing whether the dictionary is empty
import currency_converter


def test_dict():
    try:
        output = currency_converter.rates_exists(currency_converter.dictionary_check)
        assert output.__eq__(True)
    except KeyError:
        print("Dictionary is empty")
