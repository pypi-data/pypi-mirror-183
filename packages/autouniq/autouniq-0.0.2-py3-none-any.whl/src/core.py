from collections import Counter
from functools import lru_cache


@lru_cache()
def find_uniq_count_letters(string):
    assert isinstance(string, str), "should be a string"
    letters_count = Counter(string)
    values = tuple(value for value in letters_count.values() if value == 1)
    return len(values)


def find_uniq_count_from_list(income: list):
    assert isinstance(income, list), "should be a list"
    return list(map(find_uniq_count_letters, income))


def open_file(path: str) -> str:
    with open(path, "r") as file:
        print(file)
        text = file.read()
        file.close()
        return text


def make_list_from_text(text):
    assert isinstance(text,str)
    result = text.split(" ")
    return result


def find_uniq_count_in_text(path: str) -> list:
    text = open_file(path)
    income = make_list_from_text(text)
    return find_uniq_count_from_list(income)



