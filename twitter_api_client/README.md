# Twitter API Client


## Introduction
- A Library for access Twitter RESTful API

## Requirement
- A Twiiter APP
    - Get`CONSUMER_KEY`, `CONSUMER_SECRET` from Twitter Developer Console


## Component Support
- Oauth2 
    - TwitterOAuth2 (application only)
        - https://developer.twitter.com/en/docs/basics/authentication/api-reference/token
- API endpoints
    - TwitterAPI
        - method: rate_limit_status 
            - https://developer.twitter.com/en/docs/developer-utilities/rate-limit-status/api-reference/get-application-rate_limit_status
        - method: user_timeline 
            - https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html
        - method: search_tweets 
            - https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html

## QuickStart

```
from twitter_api_client import twitter_auth
from twitter_api_client import twitter_api
from twitter_api_client import twitter_error
from twitter_api_client import variables

def main():
    try:
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        api = twitter_api.TwitterAPI(twitter_auth.TwitterOAuth2(consumer_key, consumer_secret))
        print(api.rate_limit_status())
        print(api.user_timeline(None, 'HNTweets', options={'count':1}))
        print(api.search_tweets('#HackerNews', options={'count':1}))
    except twitter_error.TwitterRequestError as e:
        for v in e.errors:
            print(v)

if __name__ == '__main__':
    main()
```

## Return Value
- All method return value is dictionary
- It should be like

```
{
    'rate_limit_info': {
        'remaining': 179, 
        'limit': 180, 
        'reset': datetime.datetime(2018, 10, 31, 12, 51, 52)
    },
    'result': { ... }
}
```

- Or

```
{
    'rate_limit_info': {
        'remaining': 179, 
        'limit': 180, 
        'reset': datetime.datetime(2018, 10, 31, 12, 51, 52)
    },
    'results': [{...}, {...}]
}
```

### Details
- `rate_limit_info` is the rate limit info from Twiiter API response headers. It is the common part all return value for user could get rate limt info easily
- `result` or `results` are the data we want to access from Twitter API. Conventionally, while key is `result`, value is an dictionary. And while key is `results`, value is an list.

## Error Handling
- While Twitter API return HTTP status not OK (HTTP status code 200). This client will raise Exception TwitterError. The hierachy is like the following.
- TwitterError
    - TwitterRequestError(HTTP status code > 200 && HTTP status code > 500)
        - TwitterBadRequestError(HTTP status code 400)
        - ...
        - TwitterEnhanceYourCalmError(HTTP status code 420)
        - TwitterTooManyRequestsError(HTTP status code 429)
    - TwitterServerError(HTTP status code >= 500)
        - TwitterInternalServerError(HTTP status code 500)
        - ...
- For known HTTP status code, there is a corresponded exception. Please carefully handle the TwitterEnhanceYourCalmError(HTTP status code 420), witterTooManyRequestsError(HTTP status code 429) to avoid your twitter app to be in a blacklist in Twitter.

## Extend
- This library access Twitter RESTful API with class TwitterAPI and the API endpoint data.
- endpoint data look like
```
ENDPOINT_USER_TIMELINE = {
    'subdomain': 'api',
    'version': VERSION,
    'path': 'statuses/user_timeline.json',
    'method': 'get',
    'return': {
        'from': RETURN_ALL,
        'to': 'results'
    }
}
```
- If you want access the API not implemented in this library. you could simply do it with correct endpoint data & `TwitterAPI.request`

### Example

- https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline

```

from twitter_api_client import twitter_auth
from twitter_api_client import twitter_api
from twitter_api_client import twitter_error
from twitter_api_client import variables

def main():
    try:
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        ENDPOINT_HOME_TIMELINE = {
            'subdomain': 'api',
            'version': variables.VERSION,
            'path': 'statuses/home_timeline.json',
            'method': 'get',
            'return': {
                'from': variables.RETURN_ALL,
                'to': 'results'
            }
        }
        api = twitter_api.TwitterAPI(twitter_auth.TwitterOAuth2(consumer_key, consumer_secret))
        print(api.request(ENDPOINT_HOME_TIMELINE, params={'count':1}, data=None))
    except twitter_error.TwitterRequestError as e:
        for v in e.errors:
            print(v)
```
