from .base_model import BaseModel

class CampaignModel(BaseModel):

    """Implementation of the 'models.CampaignModel' model.

    API Request

    Attributes:
        utm_source (string): the utm source.
        utm_medium (string): the utm medium.
        utm_campaign (string): the utm campaign.
        utm_term (string): the utm term.
        utm_content (string): the utm content.
        referrer (string): the referrer.
        referring_domain (string): the referring domain.
        gclid (string): the gclid.
    """

    def __init__(self,
                 utm_source=None,
                 utm_medium=None,
                 utm_campaign=None,
                 utm_term=None,
                 utm_content=None,
                 referrer=None,
                 referring_domain=None,
                 gclid=None):
        """Constructor for the CampaignModel class"""

        # Initialize members of the class
        self.utm_source = utm_source
        self.utm_medium = utm_medium
        self.utm_campaign = utm_campaign
        self.utm_term = utm_term
        self.utm_content = utm_content
        self.referrer = referrer
        self.referring_domain = referring_domain
        self.gclid = gclid

        # Create a mapping from Model property names to API property names
        self.names = {
            "utm_source": "utm_source",
            "utm_medium": "utm_medium",
            "utm_campaign": "utm_campaign",
            "utm_term": "utm_term",
            "utm_content": "utm_content",
            "referrer": "referrer",
            "referring_domain": "referring_domain",
            "gclid": "gclid",
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
            utm_source = dictionary.get("utm_source")
            utm_medium = dictionary.get("utm_medium")
            utm_campaign = dictionary.get("utm_campaign")
            utm_term = dictionary.get("utm_term")
            utm_content = dictionary.get("utm_content")
            referrer = dictionary.get("referrer")
            referring_domain = dictionary.get("referring_domain")
            gclid = dictionary.get("gclid")
            # Return an object of this model
            return cls(utm_source,
                       utm_medium,
                       utm_campaign,
                       utm_term,
                       utm_content,
                       referrer,
                       referring_domain,
                       gclid)
