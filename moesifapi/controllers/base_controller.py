# -*- coding: utf-8 -*-

"""
    moesifapicontrollers.base_controller


"""

from ..exceptions import *
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.http_context import HttpContext
from ..http.http_request import HttpRequest
from ..http.http_response import HttpResponse
from ..http.requests_client import RequestsClient

class BaseController(object):

    """All controllers inherit from this base class. It manages shared 
	HTTP clients and global API errors."""
    
    http_call_back = None
    http_client = RequestsClient()

    def __init__(self, client, call_back):
        if client != None:
            self.http_client = client
        if call_back != None:
            self.http_call_back = call_back

    def validate_response(self, context):
        """Validates an HTTP response by checking for global errors.
       
        Args:
            context (HttpContext): The HttpContext of the API call.            
            
        """
        if (context.response.status_code < 200) or (context.response.status_code > 208): #[200,208] = HTTP OK
            raise APIException("HTTP response not OK.", context)
