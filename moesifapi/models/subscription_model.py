
# -*- coding: utf-8 -*-

"""
    moesifapi.models.subscription_model


"""
import dateutil.parser
from .base_model import BaseModel

class SubscriptionModel(BaseModel):

    """Implementation of the 'models.SubscriptionModel' model.

    API Request

    Attributes:
        subscription_id (string): the id of the subscription.
        company_id (string): the id of the company.
        current_period_start (DateTime): Time when current subscription period started.
        mcurrent_period_end (DateTime): Time when current subscription period ends.
        status (string): the status of the subscription.
        metadata (object): any custom data for the subscription .

    """

    def __init__(self,
                 subscription_id=None,
                 company_id=None,
                 current_period_start=None,
                 current_period_end=None,
                 status=None,
                 metadata=None):
        """Constructor for the SubscriptionModel class"""

        # Initialize members of the class
        self.subscription_id = subscription_id
        self.company_id = company_id
        self.current_period_start = current_period_start
        self.current_period_end = current_period_end
        self.status = status
        self.metadata = metadata

        # Create a mapping from Model property names to API property names
        self.names = {
            "subscription_id": "subscription_id",
            "company_id": "company_id",
            "current_period_start": "current_period_start",
            "current_period_end": "current_period_end",
            "status": "status",
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
            subscription_id = dictionary.get("subscription_id")
            company_id = dictionary.get("company_id")
            current_period_start = dateutil.parser.parse(dictionary.get("current_period_start")) if dictionary.get("current_period_start") else None
            current_period_end = dateutil.parser.parse(dictionary.get("current_period_end")) if dictionary.get("current_period_end") else None
            status = dictionary.get("status")
            metadata = dictionary.get("metadata")

            # Return an object of this model
            return cls(subscription_id,
                       company_id,
                       current_period_start,
                       current_period_end,
                       status,
                       metadata)
