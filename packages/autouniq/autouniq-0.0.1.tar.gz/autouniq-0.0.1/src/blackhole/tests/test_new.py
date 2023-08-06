from unittest.mock import patch

from src.blackhole.tests import case
from src.blackhole.collection_framework import main


def test_main_easy(capsys):
    """Негативный тест с без аргументов"""
    with patch('sys.argv', ['collection_framework.py']):
        from src.blackhole.collection_framework import main
        main()
        captured = capsys.readouterr()
        assert captured.out == "Can not start app with no STRING and no FILE LINK variables\n"


@patch('sys.argv', ['collection_framework.py','--string', 'fwfowifjw'])
def test_main_1(capsys):
    """Позитивный тест со строкой"""
    main()
    captured = capsys.readouterr()
    assert captured.out == "3\n"


@patch('sys.argv', ['collection_framework.py', '--file', 'uniq\\file.png'])
@patch('uniq.core.open_file')
def test_main_1(open_mock, capsys):
    """Позитивный тест с файлом 1 аргумент"""
    open_mock.return_value = case.TEXT
    main()
    captured = capsys.readouterr()
    assert captured.out == str(case.result) + "\n"


@patch('sys.argv', ['collection_framework.py', '--file', 'uniq\\file.png', '--string', 'fwfowifjw'])
@patch('uniq.core.open_file')
def test_main_1(open_mock,capsys):
    """Позитивный тест с файлом 2 аргумента"""
    open_mock.return_value = case.TEXT
    main()
    captured = capsys.readouterr()
    assert captured.out == str(case.result) + "\n"


@patch('sys.argv',['collection_framework.py', '--file', 'uniq\\file.png'])
def test_main_2(capsys):
    """Тест файл не найден 1 аргумент"""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Cant to find your file\n"


@patch('sys.argv',['collection_framework.py', '--file', 'uniq\\file.png', '--string', 'fwfowifjw'])
def test_main_3(capsys):
    """Тест файл не найден 2 аргумента"""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Cant to find your file\n"


@patch('sys.argv', ['collection_framework.py', '--file', 'uniq\\file.png', '--string', 'fwfowifjw'])
@patch('uniq.core.open_file')
def test_main_broken_text(open_mock, capsys):
    """Негативный тест """
    open_mock.return_value = b'\x03\x00\x15\x07\nY\x1c\n\x0b\x07\x01'
    main()
    captured = capsys.readouterr()
    assert captured.out == "Sorry we have an unexpected error." + "\n"

