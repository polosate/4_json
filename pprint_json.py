import json


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as data_file:
        data = json.loads(data_file.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    data = load_data('alco_shops.json')
    pretty_print_json(data)
