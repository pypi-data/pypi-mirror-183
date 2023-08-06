from unittest.mock import patch
import pytest
import collection_framework
from core import find_uniq_count_from_list, find_uniq_count_letters, find_uniq_count_in_text
from case import TEXT, result


@pytest.mark.parametrize("income, output", [
    ("asdasdf", 1),
    ("asdasdff", 0),
    ("!", 1),
    ("123321asd4", 4),
    ("z,xcmvnbpfe12", 13)
])
def test_find_count(income, output):
    assert find_uniq_count_letters(income) == output


@pytest.mark.parametrize("example", [
    True,
    122,
    1.22,
    ("223",),
])
def test_find_count_types(example):
    with pytest.raises(AssertionError, match="should be a string"):
        find_uniq_count_letters(example)


@pytest.mark.parametrize("example", [
    True,
    122,
    1.22,
    (0,),
])
def test_find_count_from_list_types(example):
    with pytest.raises(AssertionError, match="should be a list"):
        find_uniq_count_from_list(example)


def test_find_count_in_list():
    strings = [
        "example strings",
        "u can change it and put text",
        "a;lkjfowiangirgegreargasgr",
        "aikmfowijfoiwjgoierjgoisoi",
        "alkdmwifmewoijgmeioprjgeopg",
        "adoijwoifjowigoergoeijgoiejgpajpgforeajgoijsea[g"
        "porijse[ropgijprgjkepgkeporkgspokgpesokg,"
        "[peoksg[poirmbv;psijkt;sp",
        "adoijwoifjowigoergoeijgoiejgpajpgforeajgoijsea["
        "gporijse[ropgijprgjkepgkeporkgspokgpesokg,"
        "[peoksg[poirmbv;psijkt;sp",
        "adoijwoifjowigoergoeijgoiejgpajpgforeajgoijsea"
        "gporijse[ropgijprgjkepgkeporkgspokgpesokg,"
        "[peoksg[poirmbv;psijkt;sp",
        "adoijwoifjowigoergoeijgoiejgpajpgforeajg"
        "oijsea[gporijse[ropgijprgjkepgkeporkgspokgpesokg,"
        "[peoksg[poirmbv;psijkt;sp",
        "adoijwoifjowigoergoeijgoiejg",
        "adoijwoifjowigoergoeijgoiejg",
        "asdasdasdasdjjf"
    ]
    results = [11, 6, 9, 6, 6, 6, 6, 6, 6, 4, 4, 1]
    assert find_uniq_count_from_list(strings) == results


def test_force_easy_working_cashe():
    """
    Кеш точно пустой?
    В кеш точно есть 1 запись?
    При повторной передачи одного и того же значения в кеше все равно 1 запись?
    """
    find_uniq_count_letters.cache_clear()
    assert find_uniq_count_letters.cache_info().currsize == 0
    find_uniq_count_letters('first string')
    assert find_uniq_count_letters.cache_info().currsize == 1
    assert find_uniq_count_letters.cache_info().hits == 0
    assert find_uniq_count_letters.cache_info().misses == 1
    find_uniq_count_letters('first string')
    assert find_uniq_count_letters.cache_info().currsize == 1
    assert find_uniq_count_letters.cache_info().hits == 1
    assert find_uniq_count_letters.cache_info().misses == 1
    find_uniq_count_letters('first string')
    assert find_uniq_count_letters.cache_info().currsize == 1
    assert find_uniq_count_letters.cache_info().hits == 2
    assert find_uniq_count_letters.cache_info().misses == 1
    find_uniq_count_letters('first string')
    assert find_uniq_count_letters.cache_info().currsize == 1
    assert find_uniq_count_letters.cache_info().hits == 3
    assert find_uniq_count_letters.cache_info().misses == 1
    find_uniq_count_letters("second string")
    assert find_uniq_count_letters.cache_info().currsize == 2
    assert find_uniq_count_letters.cache_info().hits == 3
    assert find_uniq_count_letters.cache_info().misses == 2


def test_unic_count_in_text(mocker):
    mocker.patch('src.blackhole.uniq.core.open_file', return_value=TEXT)
    assert find_uniq_count_in_text('any') == result


@pytest.mark.parametrize("string , file, comeback", [
    ("String", None, "one count"),
    (None, "uniq/file.txt", "list of count"),
    (None, None, "Can not start app with no STRING and no FILE LINK variables"),
    ("String", "uniq/file.txt", "list of count")])
def test_start_foo(string, file, comeback, mocker):
    mocker.patch("src.blackhole.collection_framework.find_uniq_count_letters", return_value="one count")
    mocker.patch("src.blackhole.collection_framework.find_uniq_count_in_text", return_value="list of count")
    assert collection_framework.handler_choice(string, file) == comeback


@pytest.mark.parametrize("fake_args, expected_string, expected_path", [
    (['collection_framework.py', '--file', 'uniq\\file.png'], None, 'uniq\\file.png'),
    (['collection_framework.py', '--file', 'uniq\\file.png', '--string', 'fwfowifjw'], 'fwfowifjw', 'uniq\\file.png'),
    (['collection_framework.py', '--string', 'fwfowifjw'], 'fwfowifjw', None), ])
def test_parcer(fake_args, expected_string, expected_path):
    with patch('sys.argv', fake_args):
        from parcer import use_parser
        string, file = use_parser()
        assert string == expected_string
        assert file == expected_path


