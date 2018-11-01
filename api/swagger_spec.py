# -*- coding: utf-8 -*-

haghtags_spec = {
  "tags": [
    "haghtags"
  ],
  "parameters": [
    {
      "name": "haghtag",
      "in": "path",
      "type": "string",
      "required": True,
      "description": "The haghtag for query tweets"
    },
    {
      "name": "limit",
      "in": "query",
      "type": "integer",
      "required": False,
      "minimum": 1,
      "mamimum": 3200,
      "default": 30,
      "description": "The number of tweets for querying"
    }
  ],
  "operationId": "get_tweets_with_haghtag",
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "schemes": [
    "http",
    "https"
  ],
  "deprecated": False,
  "externalDocs": {
    "description": "Project repository",
    "url": "http://github.com/rochacbruno/flasgger"
  },
  "definitions": {
    "Tweets": {
      "type": "array",
      "items":{
        "$ref": "#/definitions/Tweet"
      }    
    },
    "Tweet": {
      "type": "object",
      "properties":{
        "account":{
            "type": "object",
            "properties":{
                "fullname": {
                    "type": "string"
                },
                "href": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
            }
        },
        "date": {
            "type": "integer"
        },
        "hashtags": {
            "type": "array",
            "items":{
                "type": "string"
            }
        },    
        "likes": {
            "type": "integer"
        },
        "retweets": {
            "type": "integer"
        },
        "text": {
            "type": "string"
        },
      }
    }
  },
  "responses": {
    "200": {
      "description": "A list of colors (may be filtered by palette)",
      "schema": {
        "$ref": "#/definitions/Tweets"
      },
      "examples": [
          {
            "account": {
              "fullname": "Hayley🦋🦝LovesRaccoons🦝🦋",
              "href": "/RunWithRaccoons",
              "id": 1281427944
            },
            "date": "6:17 AM - 1 Nov 2018",
            "hashtags": [
              "#Halloween"
            ],
            "likes": 0,
            "retweets": 0,
            "text": "Happy #Halloween everyone!! \nHope everyone had a fun, safe night! 🎃 \nFriendly reminder to everybody munching on cho… https://t.co/4g5oa6gtGK"
          }
        ]
    },
    "400": {
        "description": "Bad Request"
    },
    "403": {
        "description": "Forbidden"
    },
    "429": {
        "description": "Too Manay Requests(rate limit)"
    }

  }
}



users_spec = {
  "tags": [
    "users"
  ],
  "parameters": [
    {
      "name": "user",
      "in": "path",
      "type": "string",
      "required": True,
      "description": "The user screen name for query his timeline"
    },
    {
      "name": "limit",
      "in": "query",
      "type": "integer",
      "required": False,
      "minimum": 1,
      "mamimum": 3200,
      "default": 30,
      "description": "The number of tweets for querying"
    }
  ],
  "operationId": "get_tweets_with_user",
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "schemes": [
    "http",
    "https"
  ],
  "deprecated": False,
  "externalDocs": {
    "description": "Project repository",
    "url": "http://github.com/rochacbruno/flasgger"
  },
  "definitions": {
    "Tweets": {
      "type": "array",
      "items":{
        "$ref": "#/definitions/Tweet"
      }    
    },
    "Tweet": {
      "type": "object",
      "properties":{
        "account":{
            "type": "object",
            "properties":{
                "fullname": {
                    "type": "string"
                },
                "href": {
                    "type": "string"
                },
                "id": {
                    "type": "integer"
                },
            }
        },
        "date": {
            "type": "integer"
        },
        "hashtags": {
            "type": "array",
            "items":{
                "type": "string"
            }
        },    
        "likes": {
            "type": "integer"
        },
        "retweets": {
            "type": "integer"
        },
        "text": {
            "type": "string"
        },
      }
    }
  },
  "responses": {
    "200": {
      "description": "A list of colors (may be filtered by palette)",
      "schema": {
        "$ref": "#/definitions/Tweets"
      },
      "examples": [
          {
            "account": {
              "fullname": "Hayley🦋🦝LovesRaccoons🦝🦋",
              "href": "/RunWithRaccoons",
              "id": 1281427944
            },
            "date": "6:17 AM - 1 Nov 2018",
            "hashtags": [
              "#Halloween"
            ],
            "likes": 0,
            "retweets": 0,
            "text": "Happy #Halloween everyone!! \nHope everyone had a fun, safe night! 🎃 \nFriendly reminder to everybody munching on cho… https://t.co/4g5oa6gtGK"
          }
        ]
    },
    "400": {
        "description": "Bad Request"
    },
    "403": {
        "description": "Forbidden"
    },
    "429": {
        "description": "Too Manay Requests(rate limit)"
    }

  }
}
