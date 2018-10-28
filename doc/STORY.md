# STORY


## EPIC
- A Restful API to provide data from Twitter.
- Get data from Twitter by scarping in real-time or Twitter API
    - Get tweets by a hashtag
    - Get tweets by a user ID

## Before Story
- Checkt Twitter API workablility.
- A lot of details of implementation will depend on it.


## Twiiter API survey
- Notice
```
As a reminder, you have agreed to our [Developer Agreement and Policy](https://developer.twitter.com/en/developer-terms/agreement-and-policy).

Please be mindful of the following [restricted use cases](https://developer.twitter.com/en/developer-terms/more-on-restricted-use-cases)

Sensitive Information

Be careful about using Twitter data to derive or infer potentially sensitive characteristics about Twitter users (ie. health, political or religious affiliation, ethnic origin, sexual orientation, and more).

Government use and surveillance

We prohibit the use of Twitter Data and Twitter APIs by any entity for surveillance purposes. Period.

Automation

If your app will be used to post Tweets, follow accounts, or send Direct Messages, you should carefully review the Automation Rules to ensure you comply with our guidelines and never perform bulk, aggressive, or spammy actions.
```
- Develper account
- Create a Twitter APP
    - Change permission from `Read and write` to `Read-only`
- Q: API access throttle ?
    - https://developer.twitter.com/en/docs/basics/rate-limiting.html
        - 15 calls every 15 minutes, and 180 calls every 15 minutes.
        - HTTP headers
            - `x-rate-limit-limit`
            - `x-rate-limit-remaining`
            - `x-rate-limit-reset`
        - exceeds the rate limit
            - HTTP 429 “Too Many Requests” 
            - `{ "errors": [ { "code": 88, "message": "Rate limit exceeded" } ] } `
        
        - When using app-only auth, they indicate the rate limit for the application context. When using user-based auth, they indicate the rate limit for that user-application context.
        - https://developer.twitter.com/en/docs/basics/rate-limits
        - To better predict the rate limits available, consider periodically using GET application / rate_limit_status.
        - Tips to avoid being Rate Limited
            - Streaming APIs
            - Caching
            - Use application-only auth as a “reserve”
                - Requests using Application-only authentication are evaluated in a separate context to an application’s per-user rate limits. For many scenarios, you may want to use this additional rate limit pool as a “reserve” for your typical user-based operations.
        - There are pagination limits
            - Clients may access a theoretical maximum of 3,200 statuses via the page and count parameters for the user_timeline REST API methods. Other timeline methods have a theoretical maximum of 800 statuses. Requests for more than the limit will result in a reply with a status code of 200 and an empty result in the format requested. T


### Basic
- https://developer.twitter.com/en/docs/basics/things-every-developer-should-know
    - https://developer.twitter.com/en/docs/basics/response-codes.html
- https://developer.twitter.com/en/docs/basics/authentication/overview/application-only.html
### Twitter API tool
- twurl
    - https://usabilityetc.com/articles/ruby-on-mac-os-x-with-rvm/
-