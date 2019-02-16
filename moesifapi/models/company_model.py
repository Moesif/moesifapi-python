# -*- coding: utf-8 -*-

"""
    moesifapi.models.company_model


"""
import dateutil.parser
from .base_model import BaseModel


class CompanyModel(BaseModel):

    """Implementation of the 'models.CompanyModel' model.

    API Request

    Attributes:
        company_id (string): the id of the company.
        company_domain (string): the domain of the company.
        modified_time (DateTime): Time when modification is made.
        ip_address (string): IP Address of the client if known.
        session_token (string): session token of the user if known.
        metadata (object): any custom data for the company.
    """

    def __init__(self,
                 company_id=None,
                 company_domain=None,
                 modified_time=None,
                 ip_address=None,
                 session_token=None,
                 metadata=None):
        """Constructor for the CompanyModel class"""

        # Initialize members of the class
        self.company_id = company_id
        self.company_domain = company_domain
        self.modified_time = modified_time
        self.ip_address = ip_address
        self.session_token = session_token
        self.metadata = metadata

        # Create a mapping from Model property names to API property names
        self.names = {
            "company_id": "company_id",
            "company_domain": "company_domain",
            "modified_time": "modified_time",
            "ip_address": "ip_address",
            "session_token": "session_token",
            "metadata": "metadata",
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
        if dictionary is None:
            return None
        else:
            # Extract variables from the dictionary
            company_id = dictionary.get("company_id")
            company_domain = dictionary.get("company_domain")
            modified_time = dateutil.parser.parse(dictionary.get("modified_time")) if dictionary.get("modified_time") else None
            ip_address = dictionary.get("ip_address")
            session_token = dictionary.get("session_token")
            metadata = dictionary.get("metadata")
            # Return an object of this model
            return cls(company_id,
                       company_domain,
                       modified_time,
                       ip_address,
                       session_token,
                       metadata)
