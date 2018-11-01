# -*- coding: utf-8 -*-

from flask_api import exceptions as fa_exc
from .api import app
from .back_service import TwitterBackService

import pytest
import requests

@pytest.fixture
def service():
    svc = TwitterBackService()
    yield svc

@pytest.fixture
def invoke_error_service(requests_mock):
    requests_mock.post('https://api.twitter.com/oauth2/token', json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    requests_mock.get('https://api.twitter.com/1.1/search/tweets.json?q=403&count=1', json={"errors":[]}, status_code=403)
    requests_mock.get('https://api.twitter.com/1.1/search/tweets.json?q=400&count=1', json={"errors":[]}, status_code=400)
    requests_mock.get('https://api.twitter.com/1.1/search/tweets.json?q=429&count=1', json={"errors":[]}, status_code=429)
    requests_mock.get('https://api.twitter.com/1.1/search/tweets.json?q=500&count=1', json={"errors":[]}, status_code=500)
    svc = TwitterBackService()
    app.config['TWITTER_API_CONSUMER_KEY'] = 'key'
    app.config['TWITTER_API_CONSUMER_SECRET'] = 'secret'
    svc.init_app(app)
    yield svc

@pytest.fixture
def mock_service(requests_mock):
    test_headers = {
        'x-rate-limit-limit': '1500',
        'x-rate-limit-remaining': '1497',
        'x-rate-limit-reset': '1540917079'
    }
    search_expected = {
        'statuses':[{
           'created_at':'Thu Nov 01 01:09:56 +0000 2018',
           'id':1057801884436717568,
           'id_str':'1057801884436717568',
           'text':'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB',
           'truncated':False,
           'entities':{
              'hashtags':[
                 {
                    'text':'HappyHalloween',
                    'indices':[
                       87,
                       102
                    ]
                 }
              ],
           },
           'metadata':{
              'iso_language_code':'en',
              'result_type':'recent'
           },
           'user':{
              'id':1047332071281217500,
              'id_str':'1047332071281217536',
              'name':'Queen Jenn77',
              'screen_name':'QJenn77',
              'location':'',
              'description':'',
              'url':None,
              'entities':{
                 'description':{
                    'urls':[

                    ]
                 }
              },
              'protected':False,
              'followers_count':218,
              'friends_count':1000,
              'listed_count':5,
              'created_at':'Wed Oct 03 03:46:39 +0000 2018',
              'favourites_count':6762,
              'utc_offset':None,
              'time_zone':None,
              'geo_enabled':False,
              'verified':False,
              'statuses_count':6808,
              'lang':'en',
              'contributors_enabled':False,
           },
           'geo':None,
           'coordinates':None,
           'place':None,
           'contributors':None,
           'is_quote_status':False,
           'retweet_count':412,
           'favorite_count':0,
           'favorited':False,
           'retweeted':False,
           'possibly_sensitive':False,
           'lang':'en'
        }]
    }
    user_expected = [{
           'created_at':'Thu Nov 01 01:09:56 +0000 2018',
           'id':1057801884436717568,
           'id_str':'1057801884436717568',
           'text':'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB',
           'truncated':False,
           'entities':{
              'hashtags':[
                 {
                    'text':'HappyHalloween',
                    'indices':[
                       87,
                       102
                    ]
                 }
              ],
           },
           'metadata':{
              'iso_language_code':'en',
              'result_type':'recent'
           },
           'user':{
              'id':1047332071281217500,
              'id_str':'1047332071281217536',
              'name':'Queen Jenn77',
              'screen_name':'QJenn77',
              'location':'',
              'description':'',
              'url':None,
              'entities':{
                 'description':{
                    'urls':[

                    ]
                 }
              },
              'protected':False,
              'followers_count':218,
              'friends_count':1000,
              'listed_count':5,
              'created_at':'Wed Oct 03 03:46:39 +0000 2018',
              'favourites_count':6762,
              'utc_offset':None,
              'time_zone':None,
              'geo_enabled':False,
              'verified':False,
              'statuses_count':6808,
              'lang':'en',
              'contributors_enabled':False,
           },
           'geo':None,
           'coordinates':None,
           'place':None,
           'contributors':None,
           'is_quote_status':False,
           'retweet_count':412,
           'favorite_count':0,
           'favorited':False,
           'retweeted':False,
           'possibly_sensitive':False,
           'lang':'en'
        }]
    requests_mock.post('https://api.twitter.com/oauth2/token', json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    requests_mock.get('https://api.twitter.com/1.1/search/tweets.json?q=#HappyHalloween&count=1', headers=test_headers, json=search_expected )
    requests_mock.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=QJenn77&count=1', headers=test_headers, json=user_expected )
    
    svc = TwitterBackService()
    app.config['TWITTER_API_CONSUMER_KEY'] = 'key'
    app.config['TWITTER_API_CONSUMER_SECRET'] = 'secret'
    svc.init_app(app)
    yield svc

def test_convert_date_str(service):
    ret = service.convert_date_str('Wed Oct 2 15:41:56 +0000 2018')
    assert ret == '3:41 PM - 2 Oct 2018'

def test_convert_record(service):
    raw      = {
       'created_at':'Thu Nov 01 01:09:56 +0000 2018',
       'id':1057801884436717568,
       'id_str':'1057801884436717568',
       'text':'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB',
       'truncated':False,
       'entities':{
          'hashtags':[
             {
                'text':'HappyHalloween',
                'indices':[
                   87,
                   102
                ]
             }
          ],
          'symbols':[

          ],
          'user_mentions':[
             {
                'screen_name':'Simpsons_tweets',
                'name':'🎃 The Simpsons👻',
                'id':292116015,
                'id_str':'292116015',
                'indices':[
                   3,
                   19
                ]
             }
          ],
          'urls':[

          ],
          'media':[
             {
                'id':1057723599975575552,
                'id_str':'1057723599975575552',
                'indices':[
                   103,
                   126
                ],
                'media_url':'http://pbs.twimg.com/media/Dq3KApcXcAAPw43.jpg',
                'media_url_https':'https://pbs.twimg.com/media/Dq3KApcXcAAPw43.jpg',
                'url':'https://t.co/gaaiFNYRLB',
                'display_url':'pic.twitter.com/gaaiFNYRLB',
                'expanded_url':'https://twitter.com/Simpsons_tweets/status/1057724112716660736/photo/1',
                'type':'photo',
                'sizes':{
                   'thumb':{
                      'w':150,
                      'h':150,
                      'resize':'crop'
                   },
                   'medium':{
                      'w':640,
                      'h':480,
                      'resize':'fit'
                   },
                   'large':{
                      'w':640,
                      'h':480,
                      'resize':'fit'
                   },
                   'small':{
                      'w':640,
                      'h':480,
                      'resize':'fit'
                   }
                },
                'source_status_id':1057724112716660736,
                'source_status_id_str':'1057724112716660736',
                'source_user_id':292116015,
                'source_user_id_str':'292116015'
             }
          ]
       },
       'metadata':{
          'iso_language_code':'en',
          'result_type':'recent'
       },
       'user':{
          'id':1047332071281217500,
          'id_str':'1047332071281217536',
          'name':'Queen Jenn77',
          'screen_name':'QJenn77',
          'location':'',
          'description':'',
          'url':None,
          'entities':{
             'description':{
                'urls':[

                ]
             }
          },
          'protected':False,
          'followers_count':218,
          'friends_count':1000,
          'listed_count':5,
          'created_at':'Wed Oct 03 03:46:39 +0000 2018',
          'favourites_count':6762,
          'utc_offset':None,
          'time_zone':None,
          'geo_enabled':False,
          'verified':False,
          'statuses_count':6808,
          'lang':'en',
          'contributors_enabled':False,
       },
       'geo':None,
       'coordinates':None,
       'place':None,
       'contributors':None,
       'is_quote_status':False,
       'retweet_count':412,
       'favorite_count':0,
       'favorited':False,
       'retweeted':False,
       'possibly_sensitive':False,
       'lang':'en'
    }

    expected = {
        'account': {
          'fullname': 'Queen Jenn77',
          'href': '/QJenn77',
          'id': 1047332071281217500
        },
        'date': '1:09 AM - 1 Nov 2018',
        'hashtags': [
          '#HappyHalloween'
        ],
        'likes': 0,
        'retweets': 412,
        'text': 'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB'
    }
    assert service.convert_record(raw) == expected

def test_convert_records(service):
    raw      = [{
       'created_at':'Thu Nov 01 01:09:56 +0000 2018',
       'id':1057801884436717568,
       'id_str':'1057801884436717568',
       'text':'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB',
       'truncated':False,
       'entities':{
          'hashtags':[
             {
                'text':'HappyHalloween',
                'indices':[
                   87,
                   102
                ]
             }
          ],
       },
       'metadata':{
          'iso_language_code':'en',
          'result_type':'recent'
       },
       'user':{
          'id':1047332071281217500,
          'id_str':'1047332071281217536',
          'name':'Queen Jenn77',
          'screen_name':'QJenn77',
          'location':'',
          'description':'',
          'url':None,
          'entities':{
             'description':{
                'urls':[

                ]
             }
          },
          'protected':False,
          'followers_count':218,
          'friends_count':1000,
          'listed_count':5,
          'created_at':'Wed Oct 03 03:46:39 +0000 2018',
          'favourites_count':6762,
          'utc_offset':None,
          'time_zone':None,
          'geo_enabled':False,
          'verified':False,
          'statuses_count':6808,
          'lang':'en',
          'contributors_enabled':False,
       },
       'geo':None,
       'coordinates':None,
       'place':None,
       'contributors':None,
       'is_quote_status':False,
       'retweet_count':412,
       'favorite_count':0,
       'favorited':False,
       'retweeted':False,
       'possibly_sensitive':False,
       'lang':'en'
    }]

    expected = [{
        'account': {
          'fullname': 'Queen Jenn77',
          'href': '/QJenn77',
          'id': 1047332071281217500
        },
        'date': '1:09 AM - 1 Nov 2018',
        'hashtags': [
          '#HappyHalloween'
        ],
        'likes': 0,
        'retweets': 412,
        'text': 'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB'
    }]
    assert service.convert_records(raw) == expected

def test_exceptions(invoke_error_service):
    with pytest.raises(fa_exc.ParseError):
        invoke_error_service.search_tweets('400',1)
    with pytest.raises(fa_exc.PermissionDenied):
        invoke_error_service.search_tweets('403',1)
    with pytest.raises(fa_exc.Throttled):
        invoke_error_service.search_tweets('429',1)
    with pytest.raises(fa_exc.APIException):
        invoke_error_service.search_tweets('500',1)

def test_search_tweets(mock_service):
    expected = [{
        'account': {
          'fullname': 'Queen Jenn77',
          'href': '/QJenn77',
          'id': 1047332071281217500
        },
        'date': '1:09 AM - 1 Nov 2018',
        'hashtags': [
          '#HappyHalloween'
        ],
        'likes': 0,
        'retweets': 412,
        'text': 'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB'
    }]
    assert mock_service.search_tweets('HappyHalloween',1) == expected



def test_user_timeline(mock_service):
    expected = [{
        'account': {
          'fullname': 'Queen Jenn77',
          'href': '/QJenn77',
          'id': 1047332071281217500
        },
        'date': '1:09 AM - 1 Nov 2018',
        'hashtags': [
          '#HappyHalloween'
        ],
        'likes': 0,
        'retweets': 412,
        'text': 'RT @Simpsons_tweets: \'So you like donuts, eh? Well, have all the donuts in the world!\' #HappyHalloween https://t.co/gaaiFNYRLB'
    }]
    assert mock_service.user_timeline('QJenn77',1) == expected


