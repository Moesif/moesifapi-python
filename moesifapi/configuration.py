# -*- coding: utf-8 -*-

"""
   moesifapi.configuration


"""

class Configuration(object):
    # The base Uri for API calls
    BASE_URI = 'https://api.moesif.net'

    # Your Application Id for authentication/authorization
    application_id = 'SET_ME'
    version = 'moesifapi-python/1.4.6'

    pool_connections = 10
    pool_maxsize = 10
