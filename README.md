# Subscribe open data with LINE Bot/Notify/LIFF

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://badge.fury.io/py/lotify)

# Env

- LINE LIFF v2.3 concat mode
- Flask / python3.7

# Developer Side

## Local testing

1. first terminal window

```
cp .env.sample .env
pip install -r requirements.txt --user
python api.py
```

2. Create a provisional Https:

```
ngrok http 5000
```

or maybe you have npm environment:

```
npx ngrok http 5000
```

![](https://i.imgur.com/azVdG8j.png)

3. Copy url to LINE Developer Console

![](https://i.imgur.com/xOingAO.png)

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click `Configure Add-ons` and input `Heroku Scheduler` to install scheduler.

![](https://i.imgur.com/cval2jv.png)

Add two jobs on Heroku Schedular:

- `python scripts/sync_to_sqlite.py`
- `python scripts/notify_me.py`

If you are not sure where are files in, use following up commands:

```
heroku run bash
heroku logs --tail
```

# License

MIT License
