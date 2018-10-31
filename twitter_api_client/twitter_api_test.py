# -*- coding: utf-8 -*-

from .twitter_api import TwitterAPI
from .twitter_auth import TwitterOAuth2
from .twitter_error import *
from .utils import generate_url
from .variables import *

from datetime import datetime

import pytest
import requests

def test_search_tweets(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    test_headers = {
        'x-rate-limit-limit': '1500',
        'x-rate-limit-remaining': '1497',
        'x-rate-limit-reset': '1540917079'
    }
    requests_mock.get(generate_url(ENDPOINT_SEARCH), headers=test_headers, json={'statuses': [{'created_at': 'Tue Oct 30 14:02:19 +0000 2018', 'id': 1057271484823961600, 'id_str': '1057271484823961600', 'text': "Can't wait to see #Harrier in full Black colour @BosePratap", 'truncated': False, 'entities': {'hashtags': [{'text': 'Harrier', 'indices': [18, 26]}], 'symbols': [], 'user_mentions': [{'screen_name': 'BosePratap', 'name': 'Pratap Bose', 'id': 468207519, 'id_str': '468207519', 'indices': [48, 59]}], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 211234109, 'id_str': '211234109', 'name': 'Sudharson', 'screen_name': 'sudharson007', 'location': 'chennai', 'description': 'Tweets are personal and random, PROUD INDIAN,6.1ft, Introvert,Messi ,Nadal,Thala, Modi, Mani Rathnam,ARR, Politics,Books,movie buff, PS4,nature lover,Cars,bikes', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 1566, 'friends_count': 1172, 'listed_count': 13, 'created_at': 'Tue Nov 02 18:02:38 +0000 2010', 'favourites_count': 11969, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 21193, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'EBEBEB', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1034031995976744960/uh7BPSUA_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1034031995976744960/uh7BPSUA_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/211234109/1539234950', 'profile_link_color': '990000', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'F3F3F3', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': False, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}], 'search_metadata': {'completed_in': 0.035, 'max_id': 1057271484823961600, 'max_id_str': '1057271484823961600', 'next_results': '?max_id=1057271484823961599&q=%23Harrier&count=1&include_entities=1', 'query': '%23Harrier', 'refresh_url': '?since_id=1057271484823961600&q=%23Harrier&include_entities=1', 'count': 1, 'since_id': 0, 'since_id_str': '0'}})
    consumer_key = 'key'
    consumer_secret = 'secret'
    client = TwitterAPI(TwitterOAuth2(consumer_key, consumer_secret))
    ret = client.search_tweets('#Harrier', {'count':1})
    assert ret.get('results')  == [{'created_at': 'Tue Oct 30 14:02:19 +0000 2018', 'id': 1057271484823961600, 'id_str': '1057271484823961600', 'text': "Can't wait to see #Harrier in full Black colour @BosePratap", 'truncated': False, 'entities': {'hashtags': [{'text': 'Harrier', 'indices': [18, 26]}], 'symbols': [], 'user_mentions': [{'screen_name': 'BosePratap', 'name': 'Pratap Bose', 'id': 468207519, 'id_str': '468207519', 'indices': [48, 59]}], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 211234109, 'id_str': '211234109', 'name': 'Sudharson', 'screen_name': 'sudharson007', 'location': 'chennai', 'description': 'Tweets are personal and random, PROUD INDIAN,6.1ft, Introvert,Messi ,Nadal,Thala, Modi, Mani Rathnam,ARR, Politics,Books,movie buff, PS4,nature lover,Cars,bikes', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 1566, 'friends_count': 1172, 'listed_count': 13, 'created_at': 'Tue Nov 02 18:02:38 +0000 2010', 'favourites_count': 11969, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 21193, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'EBEBEB', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme7/bg.gif', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1034031995976744960/uh7BPSUA_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1034031995976744960/uh7BPSUA_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/211234109/1539234950', 'profile_link_color': '990000', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'F3F3F3', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': False, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}]

def test_user_timeline(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    test_headers = {
        'x-rate-limit-limit': '1500',
        'x-rate-limit-remaining': '1497',
        'x-rate-limit-reset': '1540917079'
    }
    requests_mock.get(generate_url(ENDPOINT_USER_TIMELINE), headers=test_headers, json=[{'created_at': 'Tue Oct 30 14:59:38 +0000 2018', 'id': 1057285909681446912, 'id_str': '1057285909681446912', 'text': 'Apple finally announces an overhauled Mac mini: https://t.co/DrbQStD4sF Comments: https://t.co/Pmshu2AsjB', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/DrbQStD4sF', 'expanded_url': 'https://arstechnica.com/gadgets/2018/10/apple-finally-announces-an-overhauled-mac-mini/', 'display_url': 'arstechnica.com/gadgets/2018/1…', 'indices': [48, 71]}, {'url': 'https://t.co/Pmshu2AsjB', 'expanded_url': 'https://news.ycombinator.com/item?id=18336846', 'display_url': 'news.ycombinator.com/item?id=183368…', 'indices': [82, 105]}]}, 'source': '<a href="http://github.com/d4nt/HNTweets" rel="nofollow">HNTweets Bot</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 116276133, 'id_str': '116276133', 'name': 'Hacker News', 'screen_name': 'HNTweets', 'location': '', 'description': 'Tweets the stories on the front page of Hacker News. Maintained by @d4nt and in no way affiliated with Y Combinator.', 'url': 'http://t.co/6bUL0JHSrz', 'entities': {'url': {'urls': [{'url': 'http://t.co/6bUL0JHSrz', 'expanded_url': 'http://news.ycombinator.com', 'display_url': 'news.ycombinator.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 16837, 'friends_count': 1, 'listed_count': 817, 'created_at': 'Sun Feb 21 21:22:43 +0000 2010', 'favourites_count': 1, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 358468, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/3025237318/1d08a308d4c8581ab30cd9a3755e13b2_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/3025237318/1d08a308d4c8581ab30cd9a3755e13b2_normal.png', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}])
    consumer_key = 'key'
    consumer_secret = 'secret'
    client = TwitterAPI(TwitterOAuth2(consumer_key, consumer_secret))
    ret = client.user_timeline(None, 'HNTweets', {'count':1})
    assert ret.get('results')   == [{'created_at': 'Tue Oct 30 14:59:38 +0000 2018', 'id': 1057285909681446912, 'id_str': '1057285909681446912', 'text': 'Apple finally announces an overhauled Mac mini: https://t.co/DrbQStD4sF Comments: https://t.co/Pmshu2AsjB', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/DrbQStD4sF', 'expanded_url': 'https://arstechnica.com/gadgets/2018/10/apple-finally-announces-an-overhauled-mac-mini/', 'display_url': 'arstechnica.com/gadgets/2018/1…', 'indices': [48, 71]}, {'url': 'https://t.co/Pmshu2AsjB', 'expanded_url': 'https://news.ycombinator.com/item?id=18336846', 'display_url': 'news.ycombinator.com/item?id=183368…', 'indices': [82, 105]}]}, 'source': '<a href="http://github.com/d4nt/HNTweets" rel="nofollow">HNTweets Bot</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 116276133, 'id_str': '116276133', 'name': 'Hacker News', 'screen_name': 'HNTweets', 'location': '', 'description': 'Tweets the stories on the front page of Hacker News. Maintained by @d4nt and in no way affiliated with Y Combinator.', 'url': 'http://t.co/6bUL0JHSrz', 'entities': {'url': {'urls': [{'url': 'http://t.co/6bUL0JHSrz', 'expanded_url': 'http://news.ycombinator.com', 'display_url': 'news.ycombinator.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 16837, 'friends_count': 1, 'listed_count': 817, 'created_at': 'Sun Feb 21 21:22:43 +0000 2010', 'favourites_count': 1, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 358468, 'lang': 'en', 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/3025237318/1d08a308d4c8581ab30cd9a3755e13b2_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/3025237318/1d08a308d4c8581ab30cd9a3755e13b2_normal.png', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}]


def test_user_timeline(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    consumer_key = 'key'
    consumer_secret = 'secret'
    client = TwitterAPI(TwitterOAuth2(consumer_key, consumer_secret))
    expected = 'user_id, screen_name only should use only one at the same time'
    with pytest.raises(ValueError, match=expected):
        ret = client.user_timeline(1234567, 'HNTweets', {'count':1})
    

def test_rate_limit_status(requests_mock):
    requests_mock.post(generate_url(ENDPOINT_AUTH), json={'token_type': 'bearer', 'access_token': 'ACCESSTOKENAAAAAAAAAALYX8wAAAAAAsgM6MD8%2F%2BqU75lSu8vhowzkfuZQ%3Db2MlUpIakaSUtLi0JsSSCsg53v5BTBPu9e3t4Bcgt7i5rzn6e9'})
    test_headers = {
        'x-rate-limit-limit': '1500',
        'x-rate-limit-remaining': '1497',
        'x-rate-limit-reset': '1540917079'
    }
    requests_mock.get(generate_url(ENDPOINT_RATE_LIMIT_STATUS), headers=test_headers, json={'resources': {'lists': {'/lists/list': {'limit': 15, 'remaining': 15, 'reset': 1540947383}}}})
    consumer_key = 'key'
    consumer_secret = 'secret'
    client = TwitterAPI(TwitterOAuth2(consumer_key, consumer_secret))
    expected = {
        'lists': {
            '/lists/list': {
                'limit': 15,
                'remaining': 15,
                'reset': datetime(2018, 10, 31, 8, 56, 23)
            }
        }
    }
    ret = client.rate_limit_status()
    assert ret.get('result') == expected
    
