# **Totp_verify_user**
User verification is the first step in TOTP login flow.
Scan the QR code with your authenticator app or copy key to manually import in authenticator app.
The QR code is valid only for 2 minutes. So make sure to scan it before it expires.

```python
client.totp_verify_user(mobilenumber="", ucc="")
```

### Example


```python
from neo_api_client import NeoAPI

client = NeoAPI(consumer_key=" ",consumer_secret=" ",environment="uat")

try:
    client.totp_verify_user(mobilenumber="", ucc="")
    
except Exception as e:
    print("Exception when calling TOTPLogin->totp_verify_user: %s\n" % e)
```
### Parameters

| Name           | Description                                       | Type   |
|----------------|---------------------------------------------------|--------|
| *mobilenumber* | Your registered mobile number Eg: "+919999996708" | Str    |
| *ucc*          | Your unique client code                           | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "status": "success",
        "key": "RX6PKQ2LZUKNON2BGVTVABCDEF",
        "qrCodeBase64": "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAABmvDolAAAABlBMVEX ///8AAABVwtN+AAADcUlEQVR42uyZMY77vA7Ex3ChUjeILhJY13IRQAZc5Fo2chH5BixVGJoH0kn+2e4VX7wqVtU6+RXakBwOafydv/Nfn0hyCeLI7MlN3A5w6jeStRlgANxjE6SVGHuSU5clcRP76iQg8L7AO+p3105wG4IvcRPujQEXFAyQEZ2Uvgbg2p0OBEG/QEMqBZECNAZouKt3cw3k0tFRyaX7mQ/fBTTtH5sUDeL9448fdfHbgJ6+Ajccl9dKxRjzDxH5OuC5d+LmJfBOiptX+tJv1Pi2AgwBwMUXdPSkxp2Z90f15S0gZwCO2ZebZXsQ1Qkr0o9L/joAsMTqcRvA0tNkXyXfl9twGhDgds20lZwQ6OYF/v4gNQlbAYajPt2kShuzt6eiSjvXs4COsG6zRwJ99m7vMhIzOC/NAANU20lVWi1JE/n0yEA6DYgUt1x8SaSfrhfNtMCCQJO2RgAEIGbvppiPljSvtM/VcZ0ERLVVGW7qiKSO66ZhVbV/6kMLQJcF14tHzyxj3MRpgd5ZUdJpwGC55Utf1QxTtCN79ckfHubXgS5jvF7AmRljrFabCrA80+EEYAieqgZTJBIpnFeNrypGO4BNNNl6t5ocPv2Dilg9C4hZ+4uobKrrY0k1YOw3Ke+6aACgZZqWpKSlEzMSqrQflvXrgM6hFY6LhtWCGKw1f/wXvw50hApI6ddstBWpenj3r3d/H7Bjj6O2n3nRS2b/1ocGgOHZsqeY/RR1ou8O/ed0GmCxq9BhWXCFhjb4cg18F28LADD21SMtQZyWw95Rxp4sN5wFdFk9jK0XbMWhPVrGK/BOuQYA27pUbwur4yddibQHngjE45Ez6csVHn0N1ppf40MLwBBo5XDT3NuhEyt1jqb7V5vfBgBxT1slI4IcblRbz8sVNwGwHAIb1LqjqBt1zPgx0n4X0Klq6UTnLPNXuMXMydJ+aQeg2Aw4IcgxUkQbn+XVu08AIuEeh7Wz7cazSMlXx2kBOLZqtiNSk0Nb2H5OzScAtl18dpz02MjZNnubvFxxC8Cxp9VyoOYekap+kj8Hsa8DgSrylu33w888X0O83oA0Aujl+/UwOiWtR7W6aTgZsMndpoYb4O979x4fmgAAZzMygp/6DOiPeN8vbxE7ATjeqdE2n2m/AGmlpB0oqTYD/J2/8/+f/wUAAP//5R96G4r=",
        "uri": "otpauth: //totp/KOTAK-NEO:YOJE0?issuer=KOTAK-NEO&secret=RX6PKQ2LZUKNON2BGVTVABCDEF",
        "issuer": "KOTAK-NEO",
        "message": "Scan the QR code with your authenticator app or copy key to manually import in authenticator app",
        "sessionID": "c39688db-c1e0-416a-aa51-d10fe6996a91"
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
