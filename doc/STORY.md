# STORY


## EPIC
- A Restful API to provide data from Twitter.
- Get data from Twitter by scarping in real-time or Twitter API
    - Get tweets by a hashtag
    - Get tweets by a user ID

## Before Story
- Checkt Twitter API workablility.
- A lot of details of implementation will depend on it.
- [Twittwer API Survey](TWITTER_API_SURVEY.md)

### Twitter API need to know
- Auth
    - application auth
    - sample user auth
    - pin auth
- Rate lmit
    - header handling
    - api check status
- Error handling

## Milestones

### Milestone 1
- Twitter API library
    - Auth: application auth
    - Error handling
    - get hashtag
    - get user timeline
- Twitter Service + API structure

### Milestone 2
- Twitter API library
    - Auth: sample user auth
    - Rate limit
        - Header Handling
        - Error handling
- API Build, Package, Release
- API Document 

### Milestone 3 
- Enhance feature backlog
    - Integrated with lambda
    - Multi-Auth?
    - Caching ?