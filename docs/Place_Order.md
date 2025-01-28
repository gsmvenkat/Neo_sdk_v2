# Place_Order
Place a New order

```python
client.place_order(exchange_segment="", product="", price="", order_type="", quantity="", validity="", trading_symbol="",
                   transaction_type="", amo="", disclosed_quantity="", market_protection="", pf="", trigger_price="",
                   tag=)
```

### Example


```python
from neo_api_client import NeoAPI
from neo_api_client import BaseUrl

base_url = BaseUrl(ucc='').get_base_url()

#First initialize session and generate session token
client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)
client.totp_login(mobilenumber="", ucc="", totp='')
client.totp_validate(mpin="")
try:
    # Place a Order
    client.place_order(exchange_segment="", product="", price="", order_type="", quantity="", validity="", trading_symbol="",
                       transaction_type="", amo="NO", disclosed_quantity="0", market_protection="0", pf="N",
                       trigger_price="0", tag=None)
except Exception as e:
    print("Exception when calling OrderApi->place_order: %s\n" % e)
``` 

### Parameters

| Name                 | Description                                                                                                                                                                                                                                                                                                                                                       | Type           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| *exchange_segment*   | nse_cm - NSE<br/>bse_cm - BSE<br/>nse_fo - NFO<br/>bse_fo - BFO<br/>cde_fo - CDS  <br/>mcx_fo - MCX                                                                                                                                                                                                                                                               | Str            |
| *product*            | NRML - Normal<br/>CNC - Cash and Carry<br/>MIS - MIS<br/>CO - Cover Order<br/>BO - Bracket Order<br/>                                                                                                                                                                                                                                                             | Str            |
| *price*              | price of the order                                                                                                                                                                                                                                                                                                                                                | Str [optional] |
| *order_type*         | L - Limit<br/>MKT - Market<br/>SL - Stop loss limit<br/>SL-M - Stop loss market                                                                                                                                                                                                                                                                                   | Str            |
| *quantity*           | quantity of the order                                                                                                                                                                                                                                                                                                                                             | Str            |
| *validity*           | Validity of the order <br/> DAY - (Applicable for all orders across all segments)<br/> IOC - Immediate or Cancel (Not applicable for CO)<br/> GTC - Good Till Cancel (Applicable only for orders in MCX market)<br/> EOS - End of Session (Applicable only for orders in BSE and MCX market)<br/> GTD - Good Till Date (Applicable only for orders in MCX market) | Str            |
| *trading_symbol*     | pTrdSymbol in ScripMaster file                                                                                                                                                                                                                                                                                                                                    | Str            |
| *transaction_type*   | B(Buy), S(Sell)                                                                                                                                                                                                                                                                                                                                                   | Str            |
| *amo*                | YES/NO - (Default Value - NO)                                                                                                                                                                                                                                                                                                                                     | Str [optional] |
| *disclosed_quantity* | (Default Value - 0)                                                                                                                                                                                                                                                                                                                                               | Str [optional] |
| *market_protection*  | (Default Value - 0)                                                                                                                                                                                                                                                                                                                                               | Str [optional] |
| *pf*                 | Default Value - “N”                                                                                                                                                                                                                                                                                                                                               | Str [optional] |
| *trigger_price*      | Optional, required for stop loss and cover order                                                                                                                                                                                                                                                                                                                  | Str [optional] |
| *tag*                | Your own tag to track the order                                                                                                                                                                                                                                                                                                                                   | Str [optional] |


### Return type

**object**

### Sample response

```json
{
    "stat": "Ok",
    "nOrdNo": "",
    "stCode": 200
}

```
### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status Code | Description                                  |
|-------------|----------------------------------------------|
| *200*       | Order placed successfully                    |
| *400*       | Invalid or missing input parameters          |
| *403*       | Invalid session, please re-login to continue |
| *429*       | Too many requests to the API                 |
| *500*       | Unexpected error                             |
| *502*       | Not able to communicate with OMS             |
| *503*       | Trade API service is unavailable             |
| *504*       | Gateway timeout, trade API is unreachable    |


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)  [[Back to README]](../README.md)
