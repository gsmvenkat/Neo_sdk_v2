# **Totp_deregister**
You can deregister a TOTP using totp_de_register method

```python
user_verification.totp_de_register(mpin='', ucc="")
```

### Example


```python
from neo_api_client import NeoAPI
from neo_api_client import UserVerification

base_url = BaseUrl(ucc='').get_base_url()

client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)
user_verification = UserVerification(mobile_number="")

try:
    user_verification.totp_de_register(mpin='', ucc="")
    
except Exception as e:
    print("Exception when calling TOTPLogin ->totp_de_register: %s\n" % e)
```
### Parameters

| Name   | Description                                             | Type   |
|--------|---------------------------------------------------------|--------|
| *mpin* | Your Mobile Personal Identification Number Eg: "123456" | Str    |

### Return type

object

### Sample response
```json
{
	"data": {
		"status": "success",
		"msg": "TOTP deregistered successfully"
	}
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | TOTP deregistered successfully       |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
