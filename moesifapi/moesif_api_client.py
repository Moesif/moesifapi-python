# -*- coding: utf-8 -*-

"""
    moesifapi.moesif_api_client


"""

from .http import *
from .models import *
from .exceptions import *
from .decorators import *
from .controllers import *

class MoesifAPIClient(object):
    def __init__(self, application_id):
        Configuration.application_id = application_id

    @lazy_property
    def api(self):
        return ApiController()

    @lazy_property
    def health(self):
        return HealthController()
