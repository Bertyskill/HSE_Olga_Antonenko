import csv
import json


def load_txt(file_name):
    lines = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for ln in f.readlines():
            lines.append(ln.strip())

    return lines


def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_trader_by_inn(traders_json, inn):
    for t in traders_json:
        if t['inn'] == inn:
            return t

    return None


def main():
    trader_inn_list = load_txt('traders.txt')
    traders_json = load_json('traders.json')

    with open('traders.csv', 'w', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['INN', 'OGRN', 'Address'])

        for inn in trader_inn_list:
            t = find_trader_by_inn(traders_json, inn)
            if t is None:
                continue

            w.writerow([t['inn'], t['ogrn'], t['address']])


if __name__ == '__main__':
    main()
