# twitter-api
Trying about build an api to query data with twitter api


## Overview

## Installation

### PreRequirements:

* Python 3.6+
* venv
* Ref: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

#### Install steps in Ubuntu
- `$ sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools`
- `$ sudo apt install python3-venv`

#### venv 
- You could create venv 
- `$ python3.6 -m venv venv`
- `$ source venv/bin/activate`

### Dependencies
- `$ source venv/bin/activate`
- `$ pip install -r requirements.txt`

## Develop

### Run
- There is a Makefile for using easily.
- If your venv is in the project directory like following

```
├── api
├── config
├── doc
├── twitter_api_client
└── venv
``` 
- You could use `$ make run` to run the develop server
- Otherwise, you just activate your venv 
- `$ source venv/bin/activate`
- `$ python server.py`

### Test
- There is a Makefile for using easily.
- If your venv is in the project directory like following

```
├── api
├── config
├── doc
├── twitter_api_client
└── venv
``` 
- You could use `$ make test` to run the develop server
- Otherwise, you just activate your venv 
- `$ source venv/bin/activate`
- `$ pytest`

## Config 

### Required
- Using Environment Variable for Critical configuration
- `APPLICATION_HOST` the ip api bind
- `APPLICATION_PORT` the port api bind
- `TWITTER_API_CONSUMER_KEY` consumer key for access Twitter API
- `TWITTER_API_CONSUMER_SECRET` consumer secret for access Twitter API

### Optional
- There is an Environment Variable for load config file
- `APPLICATION_CONFIG_PATH` set the config file path

## API Endpoints

### Swagger
- while api server is running, (`make run` or `python server.py`)
- access the `/apidoc`, will see the swagger doc pages
- e.g using browser open `127.0.0.1:5000/apidocs`

### hashtags
- `/hashtags/<hashtag>?limit={limit}`
    - Query tweets with hashtag
    - limit is the number of tweets default is 30

```
$ curl http://127.0.0.1:5000/hashtags/Halloween?limit=1
[
  {
    "account": {
      "fullname": "ぼくいか",
      "href": "/seven_ika",
      "id": 733615095733870600
    },
    "date": "7:31 AM - 1 Nov 2018",
    "hashtags": [
      "#SMTOWN",
      "#SMTOWNWONDERLAND",
      "#HALLOWEEN",
      "#LEEDONGWOO",
      "#JMIN",
      "#WENDY",
      "#YERI",
      "#IRENE",
      "#SMTSEOUL",
      "#SMmakesIT",
      "#MAKEsIT"
    ],
    "likes": 0,
    "retweets": 7365,
    "text": "RT @SMTOWNGLOBAL: #SMTOWN #SMTOWNWONDERLAND #HALLOWEEN #LEEDONGWOO #JMIN #WENDY #YERI #IRENE #SMTSEOUL #SMmakesIT #MAKEsIT https://t.co/Ouu…"
  }
]
```


### users
- `/users/<user>?limit={limit}`
    - Query tweets with user(screen_name)
    - limit is the number of tweets , default is 30

```
$ curl http://127.0.0.1:5000/users/seven_ika?limit=1
[
  {
    "account": {
      "fullname": "ぼくいか",
      "href": "/seven_ika",
      "id": 733615095733870600
    },
    "date": "7:31 AM - 1 Nov 2018",
    "hashtags": [
      "#SMTOWN",
      "#SMTOWNWONDERLAND",
      "#HALLOWEEN",
      "#LEEDONGWOO",
      "#JMIN",
      "#WENDY",
      "#YERI",
      "#IRENE",
      "#SMTSEOUL",
      "#SMmakesIT",
      "#MAKEsIT"
    ],
    "likes": 0,
    "retweets": 7365,
    "text": "RT @SMTOWNGLOBAL: #SMTOWN #SMTOWNWONDERLAND #HALLOWEEN #LEEDONGWOO #JMIN #WENDY #YERI #IRENE #SMTSEOUL #SMmakesIT #MAKEsIT https://t.co/Ouu…"
  }
]
```
