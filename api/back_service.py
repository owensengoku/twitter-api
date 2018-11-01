# -*- coding: utf-8 -*-

from twitter_api_client import twitter_api, twitter_auth, variables
from twitter_api_client import twitter_error as te
from flask_api import exceptions as fa_exc

from .util import strftime, strptime

class TwitterBackService(object):

    """This class is used to control the Twitter API Client integration to one
    or more Flask applications.  
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """This callback can be used to initialize an application for the
        use with this database setup.  Never use a database in the context
        of an application not initialized that way or connections will
        leak.
        """
        if (
            'TWITTER_API_CONSUMER_KEY' not in app.config and
            'TWITTER_API_CONSUMER_SECRET' not in app.config
        ):
            warnings.warn(
                'Neither TWITTER_API_CONSUMER_KEY nor TWITTER_API_CONSUMER_SECRET is set. '
            )
            raise ValueError('Wrong Argument for TwitterBackService')

        self.client = twitter_api.TwitterAPI(
                        twitter_auth.TwitterOAuth2(
                            app.config.get('TWITTER_API_CONSUMER_KEY'), 
                            app.config.get('TWITTER_API_CONSUMER_SECRET')
                        )
                    )
    
    def _call(self, method, *args, **kwargs):
        f = getattr(self.client, method)
        try:
            return f(*args, **kwargs)
        except (te.TwitterBadRequestError, te.TwitterNotFoundError, te.TwitterGoneError) as e:
            raise fa_exc.ParseError('Invalid Request to Twiiter API %s ' % e)
        except te.TwitterForbiddenError as e:
            raise fa_exc.PermissionDenied('Forbbiden to Twiiter API %s ' % e)
        except (te.TwitterEnhanceYourCalmError, te.TwitterTooManyRequestsError) as e:
            raise fa_exc.Throttled('Twitter API Rate Limit %s ' % e)
        except (te.TwitterRequestError, te.TwitterServerError) as e:
            raise fa_exc.APIException('Twitter API Error %s' % e)
        except Exception as e:
            raise fa_exc.APIException('Server Error %s' % e)

    def convert_date_str(self, input):
        return strftime(strptime(input))


    # Notice: 
    def convert_record(self, record):
        """
        Expected Reult
        {   
            "account":{
                "fullname":"Raymond Hettinger",
                "href":"/raymondh",
                  "id":14159138
            },
            "date":"12:57 PM - 7 Mar 2018",
            "hashtags":[
              "#python"
            ],
            "likes":169,
            "replies":13,
            "retweets":27,
            "text":"Historically, ..."
        }

        """
        user = record.get('user',{})
        return {
            'account': {
                'fullname': user.get('name'),
                'href': '/%s' % user.get('screen_name'),
                'id': user.get('id'),
            },
            'date': self.convert_date_str(record.get('created_at')),
            'hashtags': [ '#%s' % d.get('text') for d in record.get('entities',{}).get('hashtags',[])],
            'likes': record.get('favorite_count'),
            'retweets': record.get('retweet_count'),
            'text':  record.get('text')
        }
        
    def convert_records(self, records):
        ret = []
        for v in records:
            ret.append(self.convert_record(v))
        return ret

    def search_tweets(self, keyword, limit):
        ret = self._call('search_tweets', keyword, options={'count':limit})
        return self.convert_records(ret.get('results',[]))

    def user_timeline(self, user, limit):
        ret =self._call('user_timeline', screen_name=user, options={'count':limit})
        return self.convert_records(ret.get('results',[]))