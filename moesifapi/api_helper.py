# -*- coding: utf-8 -*-

"""
   moesifapi.api_helper


"""

import re
import json
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

        if isinstance(obj, list):
            obj = [
                item.to_dictionary() if isinstance(item, BaseModel) else item
                for item in obj
            ]
        elif isinstance(obj, BaseModel):
            obj = obj.to_dictionary()

        return json.dumps(obj)

    @staticmethod
    def json_deserialize(json_str, unboxing_function= None):
        """JSON Deserialization of a given string.

        Args:
            json_str (str): The JSON serialized string to deserialize.
            unboxing_function (Callable, optional): A function to process the deserialized object.

        Returns:
            Any: A dictionary, list, or processed object.
        """
        if json_str is None:
            return None

        try:
            decoded = json.loads(json_str)
        except json.JSONDecodeError:
            return json_str

        if unboxing_function is None:
            return decoded
        if isinstance(decoded, list):
            return [unboxing_function(element) for element in decoded]
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
