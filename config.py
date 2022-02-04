
import os

class Config:

    NEWS_API_KEY_URL = 'https://newsapi.org/v2/sources?apiKey=00bfddaf170f4c68a96a0ae194cffcc5'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    NEWS_API_SOURCES_URL='http://newsapi.org/v2/top-headlines?''country=us&''apiKey=00bfddaf170f4c68a96a0ae194cffcc5'
    
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
