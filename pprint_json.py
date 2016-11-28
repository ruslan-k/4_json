import json

import sys


def load_data(filepath):
    with open(filepath) as infile:
        return json.loads(infile.read())


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=3, ensure_ascii=False)



if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        print(pretty_print_json(load_data(filepath)))
    except IndexError:
        print('Не указан путь к файлу')
    except FileNotFoundError:
        print('Неверный путь к файлу или имя файла')
    except json.decoder.JSONDecodeError:
        print('Указанный файл не является json-файлом')