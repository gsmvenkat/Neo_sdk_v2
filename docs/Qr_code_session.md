# **Qr_code_session**
This is the final step in QR code login flow.

```python
client.qr_code_generate_session(ott='', ucc='')
```

### Example


```python
from neo_api_client import NeoAPI
from neo_api_client import BaseUrl

base_url = BaseUrl(ucc='').get_base_url()

client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)

try:
    client.qr_code_generate_session(ott='', ucc='')
    
except Exception as e:
    print("Exception when calling QrCodeApi->qr_code_generate_session: %s\n" % e)
```
### Parameters

| Name           | Description                                 | Type   |
|----------------|---------------------------------------------|--------|
| *ucc*          | Your unique client code                     | Str    |
| *ott*          | The token recieved from the link in QR CODE | Str    |

### Return type

object

### Sample response
```json
{
    "data": {
        "token": "",
        "sid": "",
        "rid": "",
        "hsServerId": "server4",
        "isUserPwdExpired": false,
        "caches": {
            "baskets": "",
            "lastUpdatedTS": "",
            "multiplewatchlists": ""
        },
        "ucc": "",
        "greetingName": "",
        "isTrialAccount": false,
        "dataCenter": "gdc",
        "searchAPIKey": "",
        "derivativesRiskDisclosure": "",
        "mfAccess": 1,
        "dataCenterMap": null,
        "dormancyStatus": "A",
        "asbaStatus": "",
        "clientType": "RI",
        "isNRI": false
    }
}
```

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                               |
|-------------|-------------------------------------------|
| *200*       | Trade token generated                     |
| *400*       | Invalid or missing input parameters       |
| *429*       | Too many requests to the API              |
| *500*       | Unexpected error                          |
| *503*       | Trade API service is unavailable          |
| *504*       | Gateway timeout, trade API is unreachable |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
