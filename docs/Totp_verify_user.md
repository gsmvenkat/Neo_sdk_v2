# **Totp_verify_user**
User verification is the first step in TOTP login flow.
Scan the QR code with your authenticator app or copy key to manually import in authenticator app.
The QR code is valid only for 2 minutes. So make sure to scan it before it expires.

```python
user_verification.totp_verify_user(ucc="")
```

### Example


```python
from neo_api_client import UserVerification

user_verification = UserVerification(mobile_number="")
user_verification.send_otp(resend=False)
user_verification.verify_otp(code="")

try:
    
    user_verification.totp_verify_user(ucc="")
    
except Exception as e:
    print("Exception when calling TOTPLogin->totp_verify_user: %s\n" % e)
```
### Parameters

| Name           | Description                                       | Type   |
|----------------|---------------------------------------------------|--------|
| *mobilenumber* | Your registered mobile number Eg: "+919999996708" | Str    |
| *ucc*          | Your unique client code                           | Str    |

### Return type

**object**

### Sample response
```json
{
    "data": {
        "status": "success",
        "key": "",
        "qrCodeBase64": "",
        "uri": "",
        "issuer": "KOTAK-NEO",
        "message": "Scan the QR code with your authenticator app or copy key to manually import in authenticator app",
        "sessionID": ""
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                              |
|-------------|------------------------------------------|
| *200*       | User validated successfully       |
| *400*       | Invalid or missing input parameters      |
| *429*       | Too many requests to the API             |
| *500*       | Unexpected error                         |
| *503*       | Trade API service is unavailable         |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
