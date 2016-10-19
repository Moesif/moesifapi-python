# -*- coding: utf-8 -*-

"""
   moesifapi.api_helper


"""

import re
import jsonpickle
import isodatetimehandler
from requests.utils import quote
from .models.base_model import BaseModel


class APIHelper(object):

    """A Helper Class for various functions associated with API Calls.

    This class contains static methods for operations that need to be
    performed during API requests. All of the methods inside this class are
    static methods, there is no need to ever initialise an instance of this
    class.

    """

    @staticmethod
    def json_serialize(obj):
        """JSON Serialization of a given object.

        Args:
            obj (object): The object to serialise.

        Returns:
            str: The JSON serialized string of the object.

        """
        if obj is None:
            return None

        # Resolve any Names if it's one of our objects that needs to have this called on
        if isinstance(obj, list):
            value = list()
            for item in obj:
                if isinstance(item, BaseModel):
                    value.append(item.to_dictionary())
                else:
                    value.append(item)
            obj = value
        else:
            if isinstance(obj, BaseModel):
                obj = obj.to_dictionary()

        return jsonpickle.encode(obj, False)

    @staticmethod
    def json_deserialize(json, unboxing_function=None):
        """JSON Deerialization of a given string.

        Args:
            json (str): The JSON serialized string to deserialize.

        Returns:
            dict: A dictionary representing the data contained in the
                JSON serialized string.

        """
        if json is None:
            return None

        try:
            decoded = jsonpickle.decode(json)
        except:
            return json

        if unboxing_function == None:
            return decoded
        elif type(decoded) == list:
            return [unboxing_function(element) for element in decoded]
        else:
            return unboxing_function(decoded)

    @staticmethod
    def append_url_with_template_parameters(url,
                                            parameters):
        """Replaces template parameters in the given url.

        Args:
            url (str): The query url string to replace the template parameters.
            parameters (dict): The parameters to replace in the url.

        Returns:
            str: Url with replaced parameters.

        """
        # Parameter validation
        if url is None:
            raise ValueError("URL is None.")
        if parameters is None:
            return url

        # Iterate and replace parameters
        for key in parameters:
            element = parameters[key]
            replace_value = ""

            # Load parameter value
            if element is None:
                replace_value = ""
            elif isinstance(element, list):
                replace_value = "/".join(quote(str(x), safe='') for x in element)
            else:
                replace_value = quote(str(element), safe='')

            url = url.replace('{{{0}}}'.format(key),str(replace_value))

        return url

    @staticmethod
    def clean_url(url):
        """Validates and processes the given query Url to clean empty slashes.

        Args:
            url (str): The given query Url to process.

        Returns:
            str: Clean Url as string.

        """
        # Ensure that the urls are absolute
        regex = "^https?://[^/]+"
        match = re.match(regex, url)
        if match is None:
            raise ValueError('Invalid Url format.')

        protocol = match.group(0)
        index = url.find('?')
        query_url = url[len(protocol): index if index != -1 else None]
        query_url = re.sub("//+", "/", query_url)
        parameters = url[index:] if index != -1 else ""

        return protocol + query_url + parameters

    @staticmethod
    def form_encode_parameters(form_parameters):
        """Form encodes a dictionary of form parameters

        Args:
            form_parameters (dictionary): The given dictionary which has
            atleast one model to form encode.

        Returns:
            dict: A dictionary of form encoded properties of the model.

        """
        encoded = dict()
        for key, value in form_parameters.items():
            encoded.update(APIHelper.form_encode(value, key))

        return encoded

    @staticmethod
    def form_encode(obj,
                    instanceName):
        """Encodes a model in a form-encoded manner such as person[Name]

        Args:
            obj (object): The given Object to form encode.
            instanceName (string): The base name to appear before each entry
                for this object.

        Returns:
            dict: A dictionary of form encoded properties of the model.

        """
        retval = dict()

        # If we received an object, resolve it's field names.
        if isinstance(obj, BaseModel):
            obj = obj.to_dictionary()

        if obj is None:
            return None
        elif isinstance(obj, list):
            for index, entry in enumerate(obj):
                retval.update(APIHelper.form_encode(entry, instanceName + "[" + str(index) + "]"))
        elif isinstance(obj, dict):
            for item in obj:
                retval.update(APIHelper.form_encode(obj[item], instanceName + "[" + item + "]"))
        else:
            retval[instanceName] = obj

        return retval
