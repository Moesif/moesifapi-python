# -*- coding: utf-8 -*-

"""
    moesifapi.http.http_request


"""

from .http_method_enum import HttpMethodEnum

class HttpRequest(object):

    """Information about an HTTP Request including its method, headers,
        parameters, URL, and Basic Auth details

    Attributes:
        http_method (HttpMethodEnum): The HTTP Method that this request should
            perform when called.
        headers (dict): A dictionary of headers (key : value) that should be
            sent along with the request.
        query_url (string): The URL that the request should be sent to.
        parameters (dict): A dictionary of parameters that are to be sent along
            with the request in the form body of the request
        username (string): If this request is to use Basic Authentication for
            authentication then this property represents the corresponding
            username.
        password (string): If this request is to use Basic Authentication for
            authentication then this property represents the corresponding
            password.

    """

    def __init__(self,
                 http_method,
                 query_url,
                 headers = None,
                 query_parameters = None,
                 parameters = None,
                 files = None,
                 username = None,
                 password = None):
        """Constructor for the HttpRequest class
        
        Args:
            http_method (HttpMethodEnum): The HTTP Method.
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            parameters (dict, optional): Form or body parameters to be included in the body.
            files (dict, optional): Files to be sent with the request.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
        
        """
        self.http_method = http_method
        self.query_url = query_url
        self.headers = headers
        self.query_parameters = query_parameters
        self.parameters = parameters
        self.files = files
        self.username = username
        self.password = password
