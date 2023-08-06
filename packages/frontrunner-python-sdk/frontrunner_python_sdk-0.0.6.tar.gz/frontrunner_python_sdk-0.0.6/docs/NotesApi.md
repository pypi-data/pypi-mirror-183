# frontrunner_python_sdk.NotesApi

All URIs are relative to *https://test.frontrunnerapp.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_create**](NotesApi.md#notes_create) | **POST** /notes/ | 
[**notes_destroy**](NotesApi.md#notes_destroy) | **DELETE** /notes/{id}/ | 
[**notes_list**](NotesApi.md#notes_list) | **GET** /notes/ | 
[**notes_partial_update**](NotesApi.md#notes_partial_update) | **PATCH** /notes/{id}/ | 
[**notes_retrieve**](NotesApi.md#notes_retrieve) | **GET** /notes/{id}/ | 
[**notes_update**](NotesApi.md#notes_update) | **PUT** /notes/{id}/ | 


# **notes_create**
> Note notes_create(note_create_update_request)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_create(note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_create(note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_create(note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_create(note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_create_update_request** | [**NoteCreateUpdateRequest**](NoteCreateUpdateRequest.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_destroy**
> notes_destroy(id)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_instance.notes_destroy(id)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_destroy: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_instance.notes_destroy(id)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_destroy: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_instance.notes_destroy(id)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_destroy: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_instance.notes_destroy(id)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_list**
> list[Note] notes_list(author__id=author__id, linked_contacts__id=linked_contacts__id, search=search)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    author__id = 56 # int |  (optional)
linked_contacts__id = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.notes_list(author__id=author__id, linked_contacts__id=linked_contacts__id, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    author__id = 56 # int |  (optional)
linked_contacts__id = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.notes_list(author__id=author__id, linked_contacts__id=linked_contacts__id, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    author__id = 56 # int |  (optional)
linked_contacts__id = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.notes_list(author__id=author__id, linked_contacts__id=linked_contacts__id, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    author__id = 56 # int |  (optional)
linked_contacts__id = 56 # int |  (optional)
search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.notes_list(author__id=author__id, linked_contacts__id=linked_contacts__id, search=search)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author__id** | **int**|  | [optional] 
 **linked_contacts__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**list[Note]**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_partial_update**
> Note notes_partial_update(id, note_create_update_request)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_partial_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_partial_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_partial_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_partial_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_partial_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_partial_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_partial_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note. | 
 **note_create_update_request** | [**NoteCreateUpdateRequest**](NoteCreateUpdateRequest.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_retrieve**
> Note notes_retrieve(id)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_response = api_instance.notes_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_response = api_instance.notes_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_response = api_instance.notes_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.

    try:
        api_response = api_instance.notes_retrieve(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note. | 

### Return type

[**Note**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_update**
> Note notes_update(id, note_create_update_request)



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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_update: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.NotesApi(api_client)
    id = 56 # int | A unique integer value identifying this note.
note_create_update_request = frontrunner_python_sdk.NoteCreateUpdateRequest() # NoteCreateUpdateRequest | 

    try:
        api_response = api_instance.notes_update(id, note_create_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotesApi->notes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this note. | 
 **note_create_update_request** | [**NoteCreateUpdateRequest**](NoteCreateUpdateRequest.md)|  | 

### Return type

[**Note**](Note.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [firebaseAuth](../README.md#firebaseAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

