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

Your Moesif Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps. 

You can always find your Moesif Application Id at any time by logging 
into the [_Moesif Portal_](https://www.moesif.com/), click on the top right menu,
 and then clicking _Installation_.

### Create Event

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
    "Date": "Tue, 23 Aug 2019 23:46:49 GMT",
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



event_req = EventRequestModel(time = "2019-09-09T04:45:42.914",
    uri = "https://api.acmeinc.com/items/reviews/",
    verb = "PATCH",
    api_version = "1.1.0",
    ip_address = "61.48.220.123",
    headers = req_headers,
    body = req_body)

event_rsp = EventResponseModel(time = "2019-09-09T04:45:42.914",
    status = 500,
    headers = rsp_headers,
    body = rsp_body)

event_model = EventModel(request = event_req,
    response = event_rsp,
    user_id = "12345",
    company_id = "67890",
    session_token = "23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f",
    metadata = metadata)


# Perform the API call through the SDK function
api_client.create_event(event_model)


api_client.create_event(my_api_event_model)
```

## Update a Single User

Create or update a user profile in Moesif.
The metadata field can be any customer demographic or other info you want to store.
Only the `userId` field is required.
For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-a-user).

```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

# Only user_id is required.
# Campaign object is optional, but useful if you want to track ROI of acquisition channels
# See https://www.moesif.com/docs/api#users for campaign schema
# metadata can be any custom object
user = {
  'user_id': '12345',
  'company_id': '67890', # If set, associate user with a company object
  'campaign': {
    'utm_source': 'google',
    'utm_medium': 'cpc', 
    'utm_campaign': 'adwords',
    'utm_term': 'api+tooling',
    'utm_content': 'landing'
  },
  'metadata': {
    'email': 'john@acmeinc.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'title': 'Software Engineer',
    'sales_info': {
        'stage': 'Customer',
        'lifetime_value': 24000,
        'account_owner': 'mary@contoso.com'
    },
  }
}

update_user = api_client.update_user(user)
```

## Update Users in Batch

Similar to UpdateUser, but used to update a list of users in one batch. 
Only the `userId` field is required.
For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-users-in-batch).

```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

userA = {
  'user_id': '12345',
  'company_id': '67890', # If set, associate user with a company object
  'metadata': {
    'email': 'john@acmeinc.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'title': 'Software Engineer',
    'sales_info': {
        'stage': 'Customer',
        'lifetime_value': 24000,
        'account_owner': 'mary@contoso.com'
    },
  }
}

userB = {
  'user_id': '54321',
  'company_id': '67890', # If set, associate user with a company object
  'metadata': {
    'email': 'mary@acmeinc.com',
    'first_name': 'Mary',
    'last_name': 'Jane',
    'title': 'Software Engineer',
    'sales_info': {
        'stage': 'Customer',
        'lifetime_value': 48000,
        'account_owner': 'mary@contoso.com'
    },
  }
}
update_users = api_client.update_users_batch([userA, userB])
```

## Update a Single Company

Create or update a company profile in Moesif.
The metadata field can be any company demographic or other info you want to store.
Only the `companyId` field is required.
For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-a-company).

```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

# Only company_id is required.
# Campaign object is optional, but useful if you want to track ROI of acquisition channels
# See https://www.moesif.com/docs/api#update-a-company for campaign schema
# metadata can be any custom object
company = {
  'company_id': '12345',
  'company_domain': 'acmeinc.com', # If domain is set, Moesif will enrich your profiles with publicly available info 
  'campaign': {
    'utm_source': 'google',
    'utm_medium': 'cpc', 
    'utm_campaign': 'adwords',
    'utm_term': 'api+tooling',
    'utm_content': 'landing'
  },
  'metadata': {
    'org_name': 'Acme, Inc',
    'plan_name': 'Free',
    'deal_stage': 'Lead',
    'mrr': 24000,
    'demographics': {
        'alexa_ranking': 500000,
        'employee_count': 47
    },
  }
}

update_company = api_client.update_company(company)
```

## Update Companies in Batch

Similar to updateCompany, but used to update a list of companies in one batch. 
Only the `companyId` field is required.
For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-companies-in-batch).


```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

# Only company_id is required.
# Campaign object is optional, but useful if you want to track ROI of acquisition channels
# See https://www.moesif.com/docs/api#update-a-company for campaign schema
# metadata can be any custom object
companies = [{
  'company_id': '67890',
  'company_domain': 'acmeinc.com', # If domain is set, Moesif will enrich your profiles with publicly available info 
  'campaign': {
    'utm_source': 'google',
    'utm_medium': 'cpc', 
    'utm_campaign': 'adwords',
    'utm_term': 'api+tooling',
    'utm_content': 'landing'
  },
  'metadata': {
    'org_name': 'Acme, Inc',
    'plan_name': 'Free',
    'deal_stage': 'Lead',
    'mrr': 24000,
    'demographics': {
        'alexa_ranking': 500000,
        'employee_count': 47
    },
  }
},
{
  'company_id': '09876',
  'company_domain': 'contoso.com', # If domain is set, Moesif will enrich your profiles with publicly available info 
  'campaign': {
    'utm_source': 'facebook',
    'utm_medium': 'cpc', 
    'utm_campaign': 'retargeting'
  },
  'metadata': {
    'org_name': 'Contoso, Inc',
    'plan_name': 'Paid',
    'deal_stage': 'Lead',
    'mrr': 48000,
    'demographics': {
        'alexa_ranking': 500000,
        'employee_count': 53
    },
  }
}]

update_company = api_client.update_companies(companies)
```

## Update a Single Subscription

Create or update a subscription profile in Moesif. The metadata field can store any subscription-related information you wish to keep. The `subscription_id`, `company_id`, and `status` fields are all required. This method is a convenient helper that calls the Moesif API library. For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-a-subscription).

```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *
from datetime import datetime, timedelta

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

# Required fields for a subscription update
subscription = {
  'subscription_id': 'sub_3456',
  'company_id': '67890',
  'current_period_start': datetime.utcnow(),
  'current_period_end': datetime.utcnow() + timedelta(days=30),
  'status': 'active',
  # Optional metadata can be any custom object
  'metadata': {
    'string_field': 'value_1',
    'number_field': 0,
    'object_field': {
      'field_1': 'value_1',
      'field_2': 'value_2'
    }
  }
}

update_subscription = api_client.update_subscription(subscription)
```

## Update Subscriptions in Batch

Similar to `updateSubscription`, but used to update a list of subscriptions in one batch. The `subscription_id`, `company_id`, and `status` fields are required for each subscription in the list. This method is a convenient helper that calls the Moesif API library. For details, visit the [Python API Reference](https://www.moesif.com/docs/api?python#update-subscriptions-in-batch).

```python
from moesifapi.moesif_api_client import *
from moesifapi.models import *
from datetime import datetime, timedelta

api_client = MoesifAPIClient("YOUR_COLLECTOR_APPLICATION_ID").api

# Required fields for subscription updates in a batch
subscriptions = [{
  'subscription_id': 'sub_3456',
  'company_id': '67890',
  'current_period_start': datetime.utcnow(),
  'current_period_end': datetime.utcnow() + timedelta(days=30),
  'status': 'active',
  # Optional metadata can be any custom object
  'metadata': {
    'string_field': 'value_1',
    'number_field': 0,
    'object_field': {
      'field_1': 'value_1',
      'field_2': 'value_2'
    }
  }
}, {
  'subscription_id': 'sub_34567',
  'company_id': '6789',
  'current_period_start': datetime.utcnow(),
  'current_period_end': datetime.utcnow() + timedelta(days=30),
  'status': 'active',
  'metadata': {
    'string_field': 'value_1',
    'number_field': 0,
    'object_field': {
      'field_1': 'value_1',
      'field_2': 'value_2'
    }
  }
}]

update_subscriptions = api_client.update_subscriptions_batch(subscriptions)
```

## How to test:

You can test the SDK with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. Manually clone the git repo
  2. From terminal/cmd navigate to the root directory of the SDK.
  3. Invoke 'pip install -r requirements.txt'
  4. Add your own application id to 'test/controllers/controller_test_base'
  5. Invoke 'pytest tests/controllers/test_api_controller.py'

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
