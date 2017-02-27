# -*- coding: utf-8 -*-

"""
    moesifapi.models.user_model


"""
import dateutil.parser
from .base_model import BaseModel

class UserModel(BaseModel):

    """Implementation of the 'models.UserModel' model.

    API Request

    Attributes:
        user_id (string): the id of the user.
        modified_time (DateTime): Time when modification is made.
        ip_address (string): IP Address of the client if known.
        session_token (string): session token of the user if known.
        user_agent_string (string): the string representation of user agent if
            available.
        metadata (object): any custom data for the user. include standard ones such as email and name.
    """

    def __init__(self,
                 user_id = None,
                 modified_time = None,
                 ip_address = None,
                 session_token = None,
                 user_agent_string = None,
                 metadata = None):
        """Constructor for the UserModel class"""

        # Initialize members of the class
        self.user_id = user_id
        self.modified_time = modified_time
        self.ip_address = ip_address
        self.session_token = session_token
        self.user_agent_string = user_agent_string
        self.metadata = metadata

        # Create a mapping from Model property names to API property names
        self.names = {
            "user_id" : "user_id",
            "modified_time" : "modified_time",
            "ip_address" : "ip_address",
            "session_token" : "session_token",
            "user_agent_string" : "user_agent_string",
            "metadata" : "metadata",
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
            user_id = dictionary.get("user_id")
            modified_time = dateutil.parser.parse(dictionary.get("modified_time")) if dictionary.get("modified_time") else None
            ip_address = dictionary.get("ip_address")
            session_token = dictionary.get("session_token")
            user_agent_string = dictionary.get("user_agent_string")
            metadata = dictionary.get("metadata")
            # Return an object of this model
            return cls(user_id,
                       modified_time,
                       ip_address,
                       session_token,
                       user_agent_string,
                       metadata)
