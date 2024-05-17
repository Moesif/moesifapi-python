# -*- coding: utf-8 -*-

"""
    moesifapi.models.event_model


"""
from .event_request_model import EventRequestModel
from .event_response_model import EventResponseModel
from .base_model import BaseModel
import uuid

class EventModel(BaseModel):

    """Implementation of the 'models.Event' model.

    API Call Event

    Attributes:
        request (EventRequestModel): API request object
        response (EventResponseModel): API response Object
        session_token (string): End user's auth/session token
        tags (string): comma separated list of tags, see documentation
        user_id (string): End user's user_id string from your app
        company_id (string): End user's company_id string from your app
        metadata (object): Any custom data for the event.
        direction (string): API direction, incoming or outgoing
        weight (int): Weight of an API call
        blocked_by (string): Any governance rule that applied to the event
    """

    def __init__(self,
                 request = None,
                 response = None,
                 session_token = None,
                 tags = None,
                 user_id = None,
                 company_id=None,
                 metadata = None,
                 direction=None,
                 weight=None,
                 blocked_by=None,
                 transaction_id=None):
        """Constructor for the EventModel class"""

        # Initialize members of the class
        self.request = request
        self.response = response
        self.session_token = session_token
        self.tags = tags
        self.user_id = user_id
        self.company_id = company_id
        self.metadata = metadata
        self.direction = direction
        self.weight = weight
        self.blocked_by = blocked_by
        if transaction_id is None:
            self.transaction_id = str(uuid.uuid4())
        else:
            self.transaction_id = transaction_id

        # Create a mapping from Model property names to API property names
        self.names = {
            "request" : "request",
            "response" : "response",
            "session_token" : "session_token",
            "tags" : "tags",
            "user_id" : "user_id",
            "company_id" : "company_id",
            "metadata" : "metadata",
            "direction": "direction",
            "weight": "weight",
            "blocked_by": "blocked_by",
            "transaction_id": "transaction_id"
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
            company_id = dictionary.get("company_id")
            metadata = dictionary.get("metadata")
            direction = dictionary.get("direction")
            weight = dictionary.get("weight")
            blocked_by = dictionary.get("blocked_by")
            transaction_id = dictionary.get("transaction_id", str(uuid.uuid4()))
            # Return an object of this model
            return cls(request,
                       response,
                       session_token,
                       tags,
                       user_id,
                       company_id,
                       metadata,
                       direction,
                       weight,
                       blocked_by,
                       transaction_id
                       )
