import json


def load_data(path_to_file):
    with open(path_to_file, 'r', encoding="utf-8") as data_file:
        raw_json = json.loads(data_file.read())
    return raw_json


def pretty_print_json(raw_json):
    print(json.dumps(raw_json, indent=4, sort_keys=True))


if __name__ == '__main__':
    filepath = input('Input path to file >> ')
    raw_json = load_data(filepath)
    pretty_print_json(raw_json)
