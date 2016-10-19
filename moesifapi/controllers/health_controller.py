# -*- coding: utf-8 -*-

"""
    moesifapi.controllers.health_controller


"""

from .base_controller import *

from ..models.status_model import StatusModel


class HealthController(BaseController):

    """A Controller to access Endpoints in the moesifapi API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def get_health_probe(self):
        """Does a GET request to /health/probe.

        Health Probe

        Returns:
            StatusModel: Response from the API. success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        _query_builder += '/health/probe'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'X-Moesif-Application-Id': Configuration.application_id,
            'X-Moesif-Application-Id': Configuration.application_id
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers)

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

        # Return appropriate type
        return APIHelper.json_deserialize(_response.raw_body, StatusModel.from_dictionary)
