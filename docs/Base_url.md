# **Base_url**
Initiate trading session for a User

```python
base_url = BaseUrl(ucc='').get_base_url()
```

### Example

```python
from neo_api_client import BaseUrl


base_url = BaseUrl(ucc='').get_base_url()

```
### Parameters

| Name              | Description     | Type |
|-------------------|-----------------|------|
| *ucc*             | Mandatory field | Str  |


### Return type

**object**

### Sample response

```json
{
    "data": {
        "baseURL": "https://mnapi.kotaksecurities.com"
    }
}

```

### HTTP request headers

 - **Accept**: application/json

### HTTP response details

| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Ok                                           |
| *401*       | Invalid or missing input parameters          |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
