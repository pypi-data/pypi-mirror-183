# frontrunner_python_sdk.PaginatedPeopleApi

All URIs are relative to *https://test.frontrunnerapp.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paginated_people_list**](PaginatedPeopleApi.md#paginated_people_list) | **GET** /paginated_people/ | 


# **paginated_people_list**
> PaginatedPersonList paginated_people_list(age_group=age_group, bookmarked=bookmarked, box_query=box_query, email=email, near_location=near_location, page=page, page_size=page_size, phone=phone, primary_addr__city=primary_addr__city, primary_addr__county=primary_addr__county, primary_addr__state=primary_addr__state, primary_addr__zip=primary_addr__zip, search=search, search_location_only=search_location_only, sort=sort, tags=tags)



API endpoint that allows users to be viewed in a paginated list.

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
    api_instance = frontrunner_python_sdk.PaginatedPeopleApi(api_client)
    age_group = 'age_group_example' # str | Age group (optional)
bookmarked = True # bool | Bookmarked (optional)
box_query = 'box_query_example' # str | Box query (optional)
email = 'email_example' # str |  (optional)
near_location = 'near_location_example' # str | Near location (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
phone = 'phone_example' # str |  (optional)
primary_addr__city = 'primary_addr__city_example' # str |  (optional)
primary_addr__county = 'primary_addr__county_example' # str |  (optional)
primary_addr__state = 'primary_addr__state_example' # str |  (optional)
primary_addr__zip = 'primary_addr__zip_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
search_location_only = True # bool | Search location only (optional)
sort = ['sort_example'] # list[str] | Ordering (optional)
tags = 'tags_example' # str | Tags (optional)

    try:
        api_response = api_instance.paginated_people_list(age_group=age_group, bookmarked=bookmarked, box_query=box_query, email=email, near_location=near_location, page=page, page_size=page_size, phone=phone, primary_addr__city=primary_addr__city, primary_addr__county=primary_addr__county, primary_addr__state=primary_addr__state, primary_addr__zip=primary_addr__zip, search=search, search_location_only=search_location_only, sort=sort, tags=tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaginatedPeopleApi->paginated_people_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.PaginatedPeopleApi(api_client)
    age_group = 'age_group_example' # str | Age group (optional)
bookmarked = True # bool | Bookmarked (optional)
box_query = 'box_query_example' # str | Box query (optional)
email = 'email_example' # str |  (optional)
near_location = 'near_location_example' # str | Near location (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
phone = 'phone_example' # str |  (optional)
primary_addr__city = 'primary_addr__city_example' # str |  (optional)
primary_addr__county = 'primary_addr__county_example' # str |  (optional)
primary_addr__state = 'primary_addr__state_example' # str |  (optional)
primary_addr__zip = 'primary_addr__zip_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
search_location_only = True # bool | Search location only (optional)
sort = ['sort_example'] # list[str] | Ordering (optional)
tags = 'tags_example' # str | Tags (optional)

    try:
        api_response = api_instance.paginated_people_list(age_group=age_group, bookmarked=bookmarked, box_query=box_query, email=email, near_location=near_location, page=page, page_size=page_size, phone=phone, primary_addr__city=primary_addr__city, primary_addr__county=primary_addr__county, primary_addr__state=primary_addr__state, primary_addr__zip=primary_addr__zip, search=search, search_location_only=search_location_only, sort=sort, tags=tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaginatedPeopleApi->paginated_people_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.PaginatedPeopleApi(api_client)
    age_group = 'age_group_example' # str | Age group (optional)
bookmarked = True # bool | Bookmarked (optional)
box_query = 'box_query_example' # str | Box query (optional)
email = 'email_example' # str |  (optional)
near_location = 'near_location_example' # str | Near location (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
phone = 'phone_example' # str |  (optional)
primary_addr__city = 'primary_addr__city_example' # str |  (optional)
primary_addr__county = 'primary_addr__county_example' # str |  (optional)
primary_addr__state = 'primary_addr__state_example' # str |  (optional)
primary_addr__zip = 'primary_addr__zip_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
search_location_only = True # bool | Search location only (optional)
sort = ['sort_example'] # list[str] | Ordering (optional)
tags = 'tags_example' # str | Tags (optional)

    try:
        api_response = api_instance.paginated_people_list(age_group=age_group, bookmarked=bookmarked, box_query=box_query, email=email, near_location=near_location, page=page, page_size=page_size, phone=phone, primary_addr__city=primary_addr__city, primary_addr__county=primary_addr__county, primary_addr__state=primary_addr__state, primary_addr__zip=primary_addr__zip, search=search, search_location_only=search_location_only, sort=sort, tags=tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaginatedPeopleApi->paginated_people_list: %s\n" % e)
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
    api_instance = frontrunner_python_sdk.PaginatedPeopleApi(api_client)
    age_group = 'age_group_example' # str | Age group (optional)
bookmarked = True # bool | Bookmarked (optional)
box_query = 'box_query_example' # str | Box query (optional)
email = 'email_example' # str |  (optional)
near_location = 'near_location_example' # str | Near location (optional)
page = 56 # int | A page number within the paginated result set. (optional)
page_size = 56 # int | Number of results to return per page. (optional)
phone = 'phone_example' # str |  (optional)
primary_addr__city = 'primary_addr__city_example' # str |  (optional)
primary_addr__county = 'primary_addr__county_example' # str |  (optional)
primary_addr__state = 'primary_addr__state_example' # str |  (optional)
primary_addr__zip = 'primary_addr__zip_example' # str |  (optional)
search = 'search_example' # str | A search term. (optional)
search_location_only = True # bool | Search location only (optional)
sort = ['sort_example'] # list[str] | Ordering (optional)
tags = 'tags_example' # str | Tags (optional)

    try:
        api_response = api_instance.paginated_people_list(age_group=age_group, bookmarked=bookmarked, box_query=box_query, email=email, near_location=near_location, page=page, page_size=page_size, phone=phone, primary_addr__city=primary_addr__city, primary_addr__county=primary_addr__county, primary_addr__state=primary_addr__state, primary_addr__zip=primary_addr__zip, search=search, search_location_only=search_location_only, sort=sort, tags=tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaginatedPeopleApi->paginated_people_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age_group** | **str**| Age group | [optional] 
 **bookmarked** | **bool**| Bookmarked | [optional] 
 **box_query** | **str**| Box query | [optional] 
 **email** | **str**|  | [optional] 
 **near_location** | **str**| Near location | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **phone** | **str**|  | [optional] 
 **primary_addr__city** | **str**|  | [optional] 
 **primary_addr__county** | **str**|  | [optional] 
 **primary_addr__state** | **str**|  | [optional] 
 **primary_addr__zip** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **search_location_only** | **bool**| Search location only | [optional] 
 **sort** | [**list[str]**](str.md)| Ordering | [optional] 
 **tags** | **str**| Tags | [optional] 

### Return type

[**PaginatedPersonList**](PaginatedPersonList.md)

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

