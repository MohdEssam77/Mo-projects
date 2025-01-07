import sys

import requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        Bitcoin = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = r.json()
    bpi = x["bpi"]
    usd = bpi["USD"]
    rate = usd["rate_float"]
    output = Bitcoin * rate
    print(f"${output:,.4f}")
except requests.RequestException:
    pass
