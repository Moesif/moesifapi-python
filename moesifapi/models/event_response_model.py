# -*- coding: utf-8 -*-

"""
    moesifapi.models.event_response_model


"""
import dateutil.parser
from .base_model import BaseModel

class EventResponseModel(BaseModel):

    """Implementation of the 'models.EventResponse' model.

    API Response

    Attributes:
        time (DateTime): Time when response received
        status (int): HTTP Status code such as 200
        headers (object): Key/Value map of response headers
        body (object): Response body
        ip_address (string): IP Address from the response, such as the server
            IP Address

    """

    def __init__(self,
                 time = None,
                 status = None,
                 headers = None,
                 body = None,
                 ip_address = None):
        """Constructor for the EventResponseModel class"""

        # Initialize members of the class
        self.time = time
        self.status = status
        self.headers = headers
        self.body = body
        self.ip_address = ip_address

        # Create a mapping from Model property names to API property names
        self.names = {
            "time" : "time",
            "status" : "status",
            "headers" : "headers",
            "body" : "body",
            "ip_address" : "ip_address",
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
            status = dictionary.get("status")
            headers = dictionary.get("headers")
            body = dictionary.get("body")
            ip_address = dictionary.get("ip_address")
            # Return an object of this model
            return cls(time,
                       status,
                       headers,
                       body,
                       ip_address)
