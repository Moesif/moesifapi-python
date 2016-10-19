# -*- coding: utf-8 -*-

"""
    moesifapi.http.requests_client


"""

import requests

from .http_client import HttpClient
from .http_response import HttpResponse
from .http_method_enum import HttpMethodEnum

class RequestsClient(HttpClient):

    """An implementation of HttpClient that uses Requests as its HTTP Client
    
    """
    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """	
        auth = None

        if request.username or request.password:
            auth=(request.username, request.password)

        response = requests.request(HttpMethodEnum.to_string(request.http_method), 
                                    request.query_url, 
                                    headers=request.headers,
                                    params=request.query_parameters, 
                                    data=request.parameters,
                                    files=request.files,
                                    auth=auth)

        return self.convert_response(response, False)
    
    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back
       
        Args:
            request (HttpRequest): The given HttpRequest to execute.
            
        Returns:
            HttpResponse: The response of the HttpRequest.
            
        """
        auth = None

        if request.username or request.password:
            auth=(request.username, request.password)
        
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