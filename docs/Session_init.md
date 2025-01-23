# **Session_Init**
Initiate trading session for a User

```python
client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)

```

### Example

```python
from neo_api_client import NeoAPI
from neo_api_client import BaseUrl

base_url = BaseUrl(ucc='').get_base_url()

#the session initializes when the following constructor is called
# Either you pass consumer_key and consumer_secret or you pass acsess_token 
client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)
```
### Parameters

| Name                   | Description                                                   | Type           |
|------------------------|---------------------------------------------------------------|----------------|
| *consumer_key*         | Mandatory if not passing access token                         | Str [optional] |
| *consumer_secret*      | Mandatory if not passing access token                         | Str [optional] |
| *access_token*         | Mandatory if not passing consumer key and secret              | Str [optional] |
| *environment*          | UAT/PROD, Default Value = "UAT"                               | Str [optional] |
| *neo_fin_key*          | Default Value = "neotradeapi"                                 | Str [optional] |
| *base_url*             | Mandatory field. Its fetched from base url api by passing ucc | Str [optional] |


## Return type

**object**

### Sample response

```json
{
    "access_token": "",
    "scope": "default",
    "token_type": "Bearer",
    "expires_in": 8760000
}

### HTTP request headers

 - **Accept**: application/json

### HTTP response details

| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Ok                                           |
| *401*       | Invalid or missing input parameters          |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)