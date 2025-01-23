# **User_verification_verify_otp**

```python
from neo_api_client import UserVerification

user_verification = UserVerification(mobile_number="")
user_verification.verify_otp(code="")
```

### Example


```python
from neo_api_client import UserVerification

try:
    user_verification = UserVerification(mobile_number="+919876543210")
    user_verification.send_otp(resend=False)
    user_verification.verify_otp(code="")

except Exception as e:
    print("Exception when calling UserVerification->verify_otp: %s\n" % e)
```
### Parameters

| Name   | Description                                                 | Type   |
|--------|-------------------------------------------------------------|--------|
| *code* | One Time Password received on your mobile number Eg: "1234" | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "message": "Success",
        "uccInfo": [
            {
                "ucc": "",
                "clientType": "NEO"
            }
        ]
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | OTP verified successfully                 |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
