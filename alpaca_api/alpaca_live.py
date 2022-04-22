import config, requests, json

minute_bars_url = config.BARS_URL + '/5Min?symbols=MSFT'
r = requests.get(minute_bars_url, headers=config.HEADERS)

print(json.dumps(r.json(),indent=4)) 