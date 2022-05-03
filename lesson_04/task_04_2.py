from requests import get, utils


def currency_rates(url, valute):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # print(content) # <!DOCTYPE html><html><head>...
    # Находим индекс кода валюты в строке
    valute_index = content.find(valute.upper())
    if valute_index == -1:
        return None
    else:
        value_index = content.find('<Value>', valute_index)
        value = float(content[value_index+7: value_index+14].replace(',', '.'))
        return value

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
print(type(currency_rates(url, 'dkk')))
print(currency_rates(url, 'dkk'))
print(currency_rates(url, 'aud'))
print(currency_rates(url, 'usd'))
print(currency_rates(url, 'eur'))
print(currency_rates(url, 'XXX'))
