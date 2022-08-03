import requests

date = input(f'\nEnter the date in format YYYY-MM-DD or press ENTER for today\'s date: ')

url=f'http://api.nbp.pl/api/exchangerates/tables/A/{date}?format=json'
response = requests.get(url)

if response.status_code != 200:
   print(f'No data, code {response.status_code}')
   exit(1)

data = response.json()
table = data[0]
print(f'table: {table["no"]} date: {table["effectiveDate"]}')
list = table["rates"]
print()
for currency in list:
   print(f'{currency["code"]}: {currency["mid"]:10.8f} - {currency["currency"]}')

while True:
   currency_code = input(f'\nEnter currency code: ').upper()
   if not currency_code:
       break
   amount = float(input(f'Enter the amount: '))

   for currency in list:
       if currency["code"] == currency_code:
           result = amount * currency["mid"]
           print(f'{amount} {currency_code} = {result} PLN')
           break
   else:
       print(f'There is no currency {currency_code}')

print(f'End of program')


