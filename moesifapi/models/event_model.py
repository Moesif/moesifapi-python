# -*- coding: utf-8 -*-

"""
    moesifapi.models.event_model


"""
from .event_request_model import EventRequestModel
from .event_response_model import EventResponseModel
from .base_model import BaseModel

class EventModel(BaseModel):

    """Implementation of the 'models.Event' model.

    API Call Event

    Attributes:
        request (EventRequestModel): API request object
        response (EventResponseModel): API response Object
        session_token (string): End user's auth/session token
        tags (string): comma separated list of tags, see documentation
        user_id (string): End user's user_id string from your app

    """

    def __init__(self,
                 request = None,
                 response = None,
                 session_token = None,
                 tags = None,
                 user_id = None):
        """Constructor for the EventModel class"""

        # Initialize members of the class
        self.request = request
        self.response = response
        self.session_token = session_token
        self.tags = tags
        self.user_id = user_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "request" : "request",
            "response" : "response",
            "session_token" : "session_token",
            "tags" : "tags",
            "user_id" : "user_id",
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
            request = EventRequestModel.from_dictionary(dictionary.get("request")) if dictionary.get("request") else None
            response = EventResponseModel.from_dictionary(dictionary.get("response")) if dictionary.get("response") else None
            session_token = dictionary.get("session_token")
            tags = dictionary.get("tags")
            user_id = dictionary.get("user_id")
            # Return an object of this model
            return cls(request,
                       response,
                       session_token,
                       tags,
                       user_id)
