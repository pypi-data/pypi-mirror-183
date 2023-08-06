# frontrunner_python_sdk.AbbreviatedPeopleApi

All URIs are relative to *https://test.frontrunnerapp.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abbreviated_people_list**](AbbreviatedPeopleApi.md#abbreviated_people_list) | **GET** /abbreviated_people/ | 
[**abbreviated_people_retrieve**](AbbreviatedPeopleApi.md#abbreviated_people_retrieve) | **GET** /abbreviated_people/{id}/ | 


# **abbreviated_people_list**
> list[PersonPart] abbreviated_people_list(search=search)



### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.abbreviated_people_list(search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.abbreviated_people_list(search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_list: %s\n" % e)
```

* Bearer (JWT) Authentication (firebaseAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.abbreviated_people_list(search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_list: %s\n" % e)
```

* Api Key Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.abbreviated_people_list(search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional] 

### Return type

[**list[PersonPart]**](PersonPart.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **abbreviated_people_retrieve**
> PersonPart abbreviated_people_retrieve(id)



### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    id = 56 # int | A unique integer value identifying this person.

    try:
        api_response = api_instance.abbreviated_people_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_retrieve: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    id = 56 # int | A unique integer value identifying this person.

    try:
        api_response = api_instance.abbreviated_people_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_retrieve: %s\n" % e)
```

* Bearer (JWT) Authentication (firebaseAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    id = 56 # int | A unique integer value identifying this person.

    try:
        api_response = api_instance.abbreviated_people_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_retrieve: %s\n" % e)
```

* Api Key Authentication (tokenAuth):
```python
from __future__ import print_function
import time
import frontrunner_python_sdk
from frontrunner_python_sdk.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://test.frontrunnerapp.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = frontrunner_python_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure Bearer authorization (JWT): firebaseAuth
configuration = frontrunner_python_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: tokenAuth
configuration = frontrunner_python_sdk.Configuration(
    host = "https://test.frontrunnerapp.dev",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with frontrunner_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = frontrunner_python_sdk.AbbreviatedPeopleApi(api_client)
    id = 56 # int | A unique integer value identifying this person.

    try:
        api_response = api_instance.abbreviated_people_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AbbreviatedPeopleApi->abbreviated_people_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this person. | 

### Return type

[**PersonPart**](PersonPart.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

