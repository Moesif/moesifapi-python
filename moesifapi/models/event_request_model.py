# -*- coding: utf-8 -*-

"""
    moesifapi.models.request_model


"""
import dateutil.parser
from .base_model import BaseModel

class EventRequestModel(BaseModel):

    """Implementation of the 'models.EventRequest' model.

    API Request

    Attributes:
        time (DateTime): Time when request was made
        uri (string): full uri of request such as
            https://www.example.com/my_path?param=1
        verb (string): verb of the API request such as GET or POST
        headers (object): Key/Value map of request headers
        api_version (string): Optionally tag the call with your API or App
            version
        ip_address (string): IP Address of the client if known.
        body (object): Request body

    """

    def __init__(self,
                 time = None,
                 uri = None,
                 verb = None,
                 headers = None,
                 api_version = None,
                 ip_address = None,
                 body = None):
        """Constructor for the EventRequestModel class"""

        # Initialize members of the class
        self.time = time
        self.uri = uri
        self.verb = verb
        self.headers = headers
        self.api_version = api_version
        self.ip_address = ip_address
        self.body = body

        # Create a mapping from Model property names to API property names
        self.names = {
            "time" : "time",
            "uri" : "uri",
            "verb" : "verb",
            "headers" : "headers",
            "api_version" : "api_version",
            "ip_address" : "ip_address",
            "body" : "body",
        }


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            time = dateutil.parser.parse(dictionary.get("time")) if dictionary.get("time") else None
            uri = dictionary.get("uri")
            verb = dictionary.get("verb")
            headers = dictionary.get("headers")
            api_version = dictionary.get("api_version")
            ip_address = dictionary.get("ip_address")
            body = dictionary.get("body")
            # Return an object of this model
            return cls(time,
                       uri,
                       verb,
                       headers,
                       api_version,
                       ip_address,
                       body)
