# -*- coding: utf-8 -*-

"""
    moesifapi.models.status_model


"""
from .base_model import BaseModel

class StatusModel(BaseModel):

    """Implementation of the 'models.Status' model.

    Generic status result

    Attributes:
        status (bool): Status of Call
        region (string): Location

    """

    def __init__(self,
                 status = None,
                 region = None):
        """Constructor for the StatusModel class"""

        # Initialize members of the class
        self.status = status
        self.region = region

        # Create a mapping from Model property names to API property names
        self.names = {
            "status" : "status",
            "region" : "region",
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
            status = dictionary.get("status")
            region = dictionary.get("region")
            # Return an object of this model
            return cls(status,
                       region)
