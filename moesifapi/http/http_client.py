# -*- coding: utf-8 -*-

"""
    moesifapi.http.http_client


"""

from .http_request import HttpRequest
from .http_response import HttpResponse
from .http_method_enum import HttpMethodEnum
from ..exceptions.api_exception import APIException

class HttpClient(object):

    """An interface for the methods that an HTTP Client must implement
    
    This class should not be instantiated but should be used as a base class
    for HTTP Client classes.
    
    """
    
    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """
        raise NotImplementedError("Please Implement this method")
    
    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """
        raise NotImplementedError("Please Implement this method")
    
    def convert_response(self, response):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.
       
        Args:
            response (dynamic): The original response object.
            
        Returns:
            HttpResponse: The converted HttpResponse object.
            
        """
        raise NotImplementedError("Please Implement this method")

    def get(self, query_url,
            headers = None,
            query_parameters = None,
            username = None,
            password = None):
        """Create a simple GET HttpRequest object for the given parameters
        
        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
            
        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.
            
        """
        return HttpRequest(HttpMethodEnum.GET,
                           query_url,
                           headers,
                           query_parameters,
                           None,
                           None,
                           username,
                           password)
    
    def post(self, query_url,
             headers = None,
             query_parameters = None,
             parameters = None,
             files = None,
             username = None,
             password = None):
        """Create a simple POST HttpRequest object for the given parameters
        
        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            parameters (dict, optional): Form or body parameters to be included in the body.
            files (dict, optional): Files to be sent with the request.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
            
        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.
            
        """
        return HttpRequest(HttpMethodEnum.POST,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files,
                           username,
                           password)
    
    def put(self, query_url,
            headers = None,
            query_parameters = None,
            parameters = None,
            files = None,
            username = None,
            password = None):
        """Create a simple PUT HttpRequest object for the given parameters
        
        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            parameters (dict, optional): Form or body parameters to be included in the body.
            files (dict, optional): Files to be sent with the request.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
            
        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.
            
        """
        return HttpRequest(HttpMethodEnum.PUT,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files,
                           username,
                           password)
    
    def patch(self, query_url,
              headers = None,
              query_parameters = None,
              parameters = None,
              files = None,
              username = None,
              password = None):
        """Create a simple PATCH HttpRequest object for the given parameters
        
        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            parameters (dict, optional): Form or body parameters to be included in the body.
            files (dict, optional): Files to be sent with the request.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
            
        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.
            
        """
        return HttpRequest(HttpMethodEnum.PATCH,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files,
                           username,
                           password)
    
    def delete(self, query_url,
               headers = None,
               query_parameters = None,
               username = None,
               password = None):
        """Create a simple DELETE HttpRequest object for the given parameters
        
        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the URL.
            username (string, optional): Username for Basic Auth requests.
            password (string, optional): Password for Basic Auth requests.
            
        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.
            
        """
        return HttpRequest(HttpMethodEnum.DELETE,
                           query_url,
                           headers,
                           query_parameters,
                           None,
                           None,
                           username,
                           password)
