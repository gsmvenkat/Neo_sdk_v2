# **Totp_register**
TOTP registration is the second step in TOTP login flow.

```python
client.totp_registration(totp='')
```

### Example


```python
from neo_api_client import NeoAPI

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment="uat")

try:
    client.totp_registration(totp='')
    
except Exception as e:
    print("Exception when calling TOTPLogin->totp_registration: %s\n" % e)
```
### Parameters

| Name           | Description                                            | Type   |
|----------------|--------------------------------------------------------|--------|
| *totp* | TOTP recieved on google authenticator app Eg: "123456" | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "status": "success",
        "message": "TOTP registered successfully"
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | TOTP registered successfully       |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
