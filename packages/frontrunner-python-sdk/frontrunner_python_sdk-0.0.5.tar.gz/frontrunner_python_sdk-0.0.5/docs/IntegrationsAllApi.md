# frontrunner_python_sdk.IntegrationsAllApi

All URIs are relative to *https://test.frontrunnerapp.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_all_list**](IntegrationsAllApi.md#integrations_all_list) | **GET** /integrations_all/ | 
[**integrations_all_retrieve**](IntegrationsAllApi.md#integrations_all_retrieve) | **GET** /integrations_all/{id}/ | 


# **integrations_all_list**
> list[Integration] integrations_all_list(installed=installed, search=search)



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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    installed = True # bool | Installed (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.integrations_all_list(installed=installed, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    installed = True # bool | Installed (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.integrations_all_list(installed=installed, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    installed = True # bool | Installed (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.integrations_all_list(installed=installed, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    installed = True # bool | Installed (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.integrations_all_list(installed=installed, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installed** | **bool**| Installed | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**list[Integration]**](Integration.md)

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

# **integrations_all_retrieve**
> Integration integrations_all_retrieve(id)



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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    id = 56 # int | A unique integer value identifying this public integration.

    try:
        api_response = api_instance.integrations_all_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    id = 56 # int | A unique integer value identifying this public integration.

    try:
        api_response = api_instance.integrations_all_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    id = 56 # int | A unique integer value identifying this public integration.

    try:
        api_response = api_instance.integrations_all_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.IntegrationsAllApi(api_client)
    id = 56 # int | A unique integer value identifying this public integration.

    try:
        api_response = api_instance.integrations_all_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IntegrationsAllApi->integrations_all_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this public integration. | 

### Return type

[**Integration**](Integration.md)

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

