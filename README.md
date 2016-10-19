MoesifApi Lib for Python
========================

[Source Code on GitHub](https://github.com/moesif/moesifapi-python)

This SDK uses the Requests library and will work for Python 2.7 — 3.5.

__Check out Moesif's
[Python developer documentation](https://www.moesif.com/developer-documentation) to learn more__

(Documentation access requires an active account)

How to install:
===============

```
pip install moesifapi
```

How to use:
===========
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
    session_token = "23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f")


# Perform the API call through the SDK function
api_client.create_event(event_model)


controller.create_event(my_api_event_model)
```

How  to test:
=============
You can test the SDK with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. Manually clone the git repo
  2. From terminal/cmd navigate to the root directory of the SDK.
  3. Invoke 'pip install -r requirements.txt'
  4. Invoke 'nosetests tests/controllers/test_api_controller.py'
