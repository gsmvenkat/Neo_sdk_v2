# **User_verification_send_otp**

```python
user_verification = UserVerification(mobile_number="")
user_verification.send_otp(resend=False)
```

### Example


```python
from neo_api_client import UserVerification

try:
    user_verification = UserVerification(mobile_number="+919876543210")
    user_verification.send_otp(resend=False)

except Exception as e:
    print("Exception when calling UserVerification->send_otp: %s\n" % e)
```
### Parameters

| Name           | Description                                                             | Type   |
|----------------|-------------------------------------------------------------------------|--------|
| *mobile_number* | Your registered mobile number Eg: "+919999996708"                       | Str    |
| *resend*          | Boolean value which determines whether the user is requesting a new otp | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "sessionId": ""
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | OTP sent successfully                     |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
