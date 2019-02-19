# MoesifApi Lib for Python

[![Built For][ico-built-for]][link-built-for]
[![Latest Version][ico-version]][link-package]
[![Language Versions][ico-language]][link-language]
[![Software License][ico-license]][link-license]
[![Source Code][ico-source]][link-source]

[Source Code on GitHub](https://github.com/moesif/moesifapi-python)

This SDK uses the Requests library and will work for Python 2.7 — 3.5.

If you are using Django as your platform, we have [moesifapi-python](https://github.com/Moesif/moesifapi-python) middleware, you can use that middleware directly.

__Check out Moesif's [Developer Documentation](https://www.moesif.com/docs) and [Python API Reference](https://www.moesif.com/docs/api?python) to learn more__


## How to install:

```
pip install moesifapi
```

## How to use:

The code uses Python packages named requests, jsonpickle and dateutil.
After having resolved the dependencies, you can easily use the SDK following these steps.

```python
from __future__ import print_function
from moesifapi.moesif_api_client import *
from moesifapi.models import *

client = MoesifAPIClient(my_application_id)
api_client = client.api

# Note: we recommend sending all API Calls via MVC framework middleware.

req_headers = APIHelper.json_deserialize("""  {
  "Host": "api.acmeinc.com",
  "Accept": "*/*",
  "Connection": "Keep-Alive",
  "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.0.2; C6906 Build/14.5.A.0.242)",
  "Content-Type": "application/json",
  "Content-Length": "126",
  "Accept-Encoding": "gzip"
} """)

req_body = APIHelper.json_deserialize( """{
  "items": [
    {
      "type": 1,
      "id": "fwfrf"
    },
    {
      "type": 2,
      "id": "d43d3f"
    }
  ]
}""")

rsp_headers = APIHelper.json_deserialize("""  {
    "Date": "Tue, 23 Aug 2016 23:46:49 GMT",
    "Vary": "Accept-Encoding",
    "Pragma": "no-cache",
    "Expires": "-1",
    "Content-Type": "application/json; charset=utf-8"
    "Cache-Control": "no-cache"
  } """)

rsp_body = APIHelper.json_deserialize( """{
    "Error": "InvalidArgumentException",
    "Message": "Missing field field_a"
  }""")

metadata = APIHelper.json_deserialize("""{
    "field1": "foo",
    "field2": "bar"
  }""")



event_req = EventRequestModel(time = "2016-09-09T04:45:42.914",
    uri = "https://api.acmeinc.com/items/reviews/",
    verb = "PATCH",
    api_version = "1.1.0",
    ip_address = "61.48.220.123",
    headers = req_headers,
    body = req_body)

event_rsp = EventResponseModel(time = "2016-09-09T04:45:42.914",
    status = 500,
    headers = rsp_headers,
    body = rsp_body)

event_model = EventModel(request = event_req,
    response = event_rsp,
    user_id = "my_user_id",
    session_token = "23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f",
    metadata = metadata)


# Perform the API call through the SDK function
api_client.create_event(event_model)


api_client.create_event(my_api_event_model)
```

### update_user

The api also let you update a user profile with custom metadata.
The user_id is a required fields, all other fields are optional.

```python
metadata = APIHelper.json_deserialize("""  {
        "email": "pythonapiuser@email.com",
        "name": "pythonapiuser",
        "custom": "testdata"
    } """)


user_model = UserModel(
    user_id = 'pythonapiuser1',
    modified_time = datetime.utcnow(),
    metadata = metadata)

# Perform the API call through the SDK function
api_client.update_user(user_model)

```

### update_company

The api also let you update a company information with custom metadata.
The company_id is a required field, all other fields are optional.

```python
metadata = APIHelper.json_deserialize("""  {
        "email": "pythonapiuser@email.com",
        "name": "pythonapiuser",
        "location": "United States"
    } """)

company_model = CompanyModel(
            company_id='1',
            modified_time=datetime.utcnow(),
            metadata=metadata)

# Perform the API call through the SDK function
self.controller.update_company(company_model)
```

## How  to test:

You can test the SDK with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. Manually clone the git repo
  2. From terminal/cmd navigate to the root directory of the SDK.
  3. Invoke 'pip install -r requirements.txt'
  4. Add your own application id to 'test/controllers/controller_test_base'
  5. Invoke 'nosetests tests/controllers/test_api_controller.py'

  [ico-built-for]: https://img.shields.io/badge/built%20for-python-blue.svg
  [ico-version]: https://img.shields.io/pypi/v/moesifapi.svg
  [ico-language]: https://img.shields.io/pypi/pyversions/moesifapi.svg
  [ico-license]: https://img.shields.io/badge/License-Apache%202.0-green.svg
  [ico-source]: https://img.shields.io/github/last-commit/moesif/moesifapi-python.svg?style=social

  [link-built-for]: https://www.python.org/
  [link-package]: https://pypi.python.org/pypi/moesifapi
  [link-language]: https://pypi.python.org/pypi/moesifapi
  [link-license]: https://raw.githubusercontent.com/Moesif/moesifapi-python/master/LICENSE
  [link-source]: https://github.com/Moesif/moesifapi-python
