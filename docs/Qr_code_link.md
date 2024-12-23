# **Qr_code_link**
Generating qr code is the first step in QR code login flow

```python
client.qr_code_get_link(ucc='')
```

### Example


```python
from neo_api_client import NeoAPI

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment="uat")

try:
    client.qr_code_get_link(ucc='')
    
except Exception as e:
    print("Exception when calling QrCodeApi->qr_code_get_link: %s\n" % e)
```
### Parameters

| Name           | Description                                       | Type   |
|----------------|---------------------------------------------------|--------|
| *ucc*          | Your unique client code                           | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "baseDomain": "https://mnapi.kotaksecurities.com",
        "redirectUrl": ""
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | QR code generated successfully            |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
