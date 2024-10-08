# -*- coding: utf-8 -*-

"""
    moesifapi.http.requests_client


"""

import requests
from requests.adapters import HTTPAdapter
from ..configuration import Configuration
from .http_client import HttpClient
from .http_response import HttpResponse
from .http_method_enum import HttpMethodEnum
from requests.packages.urllib3.util.retry import Retry


# Decorator to refresh connection pool on ConnectionError
def refresh_session(func):
    # Wrap function with retry once on ConnectionError
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except requests.exceptions.ConnectionError as e:
            print(f"ConnectionError: Attempt to reestablish the connection")
            # Attempt to reestablish the connection
            self.__refresh_connection_pool__()

            # retry
            result = func(self, *args, **kwargs)

        return result

    return wrapper


class RequestsClient(HttpClient):

    """An implementation of HttpClient that uses Requests as its HTTP Client
    
    """

    # connection pool here
    def __create_connection_pool__(self):
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        self.session = requests.Session()
        self.adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=Configuration.pool_connections,
            pool_maxsize=Configuration.pool_maxsize
        )
        self.session.mount('http://', self.adapter)
        self.session.mount('https://', self.adapter)

    def __refresh_connection_pool__(self):
        # Attempt to reestablish the connection.
        # clear closes all open connections - leaves in-flight connections, but it will not be re-used after completion.
        # It automatically opens a new ConnectionPool if no open connections exist for the request.
        self.adapter.poolmanager.clear()

    def __init__(self):
        self.__create_connection_pool__()

    @refresh_session
    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """	
        auth = None

        if request.username or request.password:
            auth = (request.username, request.password)

        # connection pool to make request
        response = self.session.request(HttpMethodEnum.to_string(request.http_method),
                                        request.query_url,
                                        headers=request.headers,
                                        params=request.query_parameters,
                                        data=request.parameters,
                                        files=request.files,
                                        auth=auth)

        return self.convert_response(response, False)

    @refresh_session
    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """
        auth = None

        if request.username or request.password:
            auth = (request.username, request.password)
        
        response = requests.request(HttpMethodEnum.to_string(request.http_method), 
                                    request.query_url, 
                                    headers=request.headers,
                                    params=request.query_parameters, 
                                    data=request.parameters, 
                                    files=request.files,
                                    auth=auth)
                                   
        return self.convert_response(response, True)
    
    def convert_response(self, response, binary):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.
       
        Args:
            response (dynamic): The original response object.
            
        Returns:
            HttpResponse: The converted HttpResponse object.
            
        """
        if binary == True:
            return HttpResponse(response.status_code, response.headers, response.content)
        else:
            return HttpResponse(response.status_code, response.headers, response.text)
