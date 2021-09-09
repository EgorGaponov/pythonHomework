#Задание №2

import requests


def currency_rates(currency, currencies):
    return round(currencies.get(currency.lower()), 2)


currencies = dict()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36'}
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp', headers=headers)
if r.status_code == 200:
    for info_text in r.text.split('<Nominal>')[1:]:
        info = info_text.split("</value")[0].split('</Nominal><Name>')
        nominal = int(info[0])
        info2 = info[1].split('</Name><Value>')
        currency_type = info2[0]
        value = float(info2[1].replace(',','.'))
        currencies[currency_type.lower()] = value / nominal

print(currency_rates('Доллфк США', currencies))
print(currency_rates('Евро', currencies))

