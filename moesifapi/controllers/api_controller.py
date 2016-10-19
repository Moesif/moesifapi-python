# -*- coding: utf-8 -*-

"""
    moesifapi.controllers.api_controller


"""

from .base_controller import *



class ApiController(BaseController):

    """A Controller to access Endpoints in the moesifapi API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def create_event(self,
                     body):
        """Does a POST request to /v1/events.

        Add Single API Event Call

        Args:
            body (EventModel): TODO: type description here. Example:

        Returns:
            void: Response from the API. success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        _query_builder += '/v1/events'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'X-Moesif-Application-Id': Configuration.application_id,
            'X-Moesif-Application-Id': Configuration.application_id
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)

    def create_events_batch(self,
                            body):
        """Does a POST request to /v1/events/batch.

        Add multiple API Events in a single batch (batch size must be less
        than 250kb)

        Args:
            body (list of EventModel): TODO: type description here.
                Example:

        Returns:
            void: Response from the API. success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        _query_builder += '/v1/events/batch'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'content-type': 'application/json; charset=utf-8',
            'X-Moesif-Application-Id': Configuration.application_id,
            'X-Moesif-Application-Id': Configuration.application_id
        }

        # Prepare the API call.
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_request)

        # Wrap the request and the response in an HttpContext object
        _context = HttpContext(_request, _response)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)
