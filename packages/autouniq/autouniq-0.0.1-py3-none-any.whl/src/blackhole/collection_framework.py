from uniq.core import find_uniq_count_in_text, find_uniq_count_letters
from uniq.parcer import use_parser


def handler_choice(string, path):
    if path:
        return find_uniq_count_in_text(path)
    elif string:
        return find_uniq_count_letters(string)
    else:
        return "Can not start app with no STRING and no FILE LINK variables"


def main():
    string, path = use_parser()
    try:
        answer = handler_choice(string, path)
    except UnicodeDecodeError:
        answer = "Cant to read this file"
    except FileNotFoundError:
        answer = "Cant to find your file"
    except Exception as error:
        answer=f"Sorry we have an unexpected error."
    print(answer)


if __name__ == "__main__":
    main()
