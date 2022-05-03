
from task_04_4_utils import currency_rates


url = 'http://www.cbr.ru/scripts/XML_daily.asp'
print(currency_rates(url, 'dkk'))
print(currency_rates(url, 'aud'))
print(currency_rates(url, 'usd'))
print(currency_rates(url, 'eur'))
print(currency_rates(url, 'XXX'))