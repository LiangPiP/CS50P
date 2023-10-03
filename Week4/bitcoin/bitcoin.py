import sys
import requests

try:
    n=float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
amount=n*float(r["bpi"]["USD"]["rate"].replace(',',''))
print(f"${amount:,.4f}")
