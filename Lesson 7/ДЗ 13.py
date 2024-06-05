import json
import datetime
import urllib.request
import bs4

class ParserCBRF:
    """
    Загружает с сайта ЦБ РФ страницу с официальными курсами валют на сегодняшнюю
    дату (текущую на момент запуска скрипта), вытаскивает данные из HTML-кода
    страницы, пересчитывает курс в рублях на единицу валюты (для некоторых валют
    ЦБ указывает количество рублей за 100 и больше единиц валюты) и сохраняет их
    в JSON-файл в текущем каталоге. Имя файла формируется автоматически из
    текущей даты по шаблону "YYYY-MM-DD.json".
    """

    @staticmethod
    def start():
        today = datetime.date.today()
        url = ParserCBRF._get_url_for_date(today)
        soup = ParserCBRF._download_and_parse_page(url)
        rates = ParserCBRF._extract_currency_rates(soup)

        file_name = ParserCBRF._get_file_name_for_date(today)
        ParserCBRF._save_to_file(file_name, rates)

    @staticmethod
    def _get_url_for_date(date):
        return f"https://cbr.ru/currency_base/daily?UniDbQuery.Posted=True&UniDbQuery.To={date:%d.%m.%Y}"

    @staticmethod
    def _get_file_name_for_date(date):
        return f"{date:%Y-%m-%d}.json"

    @staticmethod
    def _download_and_parse_page(url):
        with urllib.request.urlopen(url) as f:
            return bs4.BeautifulSoup(f, 'html.parser')

    @staticmethod
    def _extract_currency_rates(soup):
        matches = soup.select('table.data > tbody > tr')

        rates = {}
        for m in matches:
            cells = m.findAll('td')
            if len(cells) != 5:
                continue

            code = cells[1].text
            a = ParserCBRF._parse_number(cells[4].text)
            b = ParserCBRF._parse_number(cells[2].text)
            rates[code] = a / b

        return rates

    @staticmethod
    def _parse_number(text):
        return float(text.replace(',', '.'))

    @staticmethod
    def _save_to_file(file_name, rates):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(rates, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    ParserCBRF.start()