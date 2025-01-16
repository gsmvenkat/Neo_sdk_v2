# Kotak Neo Python SDK Development

- API version: 1.0.1
- Package version: 1.2.0

## Requirements.

Python 3.10+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install "git+https://github.com/Kotak-Neo/kotak-neo-api.git#egg=neo_api_client"
```

If you are updating your package please use below command to install
```sh
pip install --force-reinstall "git+https://github.com/Kotak-Neo/kotak-neo-api"
```
(you may need to run `pip` with root permission: `sudo pip install -e "`)

Then import the package:
```python
import neo_api_client
```

### Setuptools

Install via [Setuptools]

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neo_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then refer to the sample code below for various API requests:

```python
from neo_api_client import NeoAPI
from neo_api_client import BaseUrl

# ucc: Unique Client Code which you will find in mobile application/website under profile section
base_url = BaseUrl(ucc='').get_base_url()

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print(message)
    
def on_open(message):
    print(message)
    
    
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
client = NeoAPI(consumer_key="", consumer_secret="", environment='prod', access_token=None, neo_fin_key=None, base_url=base_url)


# TOTP Login

from neo_api_client import UserVerification

# mobile_number: registered mobile number
user_verification = UserVerification(mobile_number="")

# resend: resend is an optional param. Default value is 'False'
# An otp will be sent to the registered mobile number
user_verification.send_otp(resend=False)

# code: OTP you recieved on the registered phone number
user_verification.verify_otp(code="")

# ucc: Unique Client Code which you will find in mobile application/website under profile section
# totp_verify_user returns a base64 encoded qrcode image. 
# Scan the qrcode with google authenticator application and you'll recieve the TOTP.
# qr code is valid only for 2 minutes
user_verification.totp_verify_user(ucc="")

# totp: Time-based One-Time Password recieved on google authenticator application
user_verification.totp_registration(totp="")

# mobile_number: registered mobile number
# ucc: Unique Client Code which you will find in mobile application/website under profile section
# totp: Time-based One-Time Password recieved on google authenticator application
# totp_login generates the view token and session id used to generate trade token
client.totp_login(mobile_number="", ucc="", totp='')

# mpin: 
# totp_validate generates the trade token
client.totp_validate(mpin="")


# TOTP de-register

# mobile_number: registered mobile number
user_verification = UserVerification(mobile_number="")

# resend: resend is an optional param. Default value is 'False'
# An otp will be sent to the registered mobile number
user_verification.send_otp(resend=False)

# mpin: 
# ucc: Unique Client Code which you will find in mobile application/website under profile section
# totp_de_register is used to de-register the current TOTP
user_verification.totp_de_register(mpin='210495', ucc="Y4HAU")



# QR Code Login

# ucc: Unique Client Code which you will find in mobile application/website under profile section
# qr_code_get_link returns a qrcode
client.qr_code_get_link(ucc='')

# ott: 
# ucc: Unique Client Code which you will find in mobile application/website under profile section
# trade token is generated on passing ott to qr_code_generate_session 
client.qr_code_generate_session(ott='', ucc='')


# Setup Callbacks for websocket events (Optional)
client.on_message = on_message  # called when message is received from websocket
client.on_error = on_error  # called when any error or exception occurs in code or websocket
client.on_close = on_close  # called when websocket connection is closed
client.on_open = on_open  # called when websocket successfully connects


# Once 2FA has you can place the order by using below function
# exchange_segment: Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, bcs_fo
# product: Expected values are NRML, CNC, MIS, INTRADAY, CO, BO
# price:
# order_type: Expected values are L, MKT, SL, SL-M, SP, 2L, 3L
# validity: Expected values are DAY
# trading_symbol: 
# transaction_type: Expected values are B, S
# amo: Expected values are either YES or NO
# disclosed_quantity:
# market_protection:
# pf:
# trigger_price:
# tag:
client.place_order(exchange_segment='', product='', price='', order_type='', quantity='', validity='', trading_symbol='', 
                   transaction_type='', amo='NO', disclosed_quantity='0', market_protection='0', pf='N', 
                   trigger_price='0', tag=None)

						
# Modify an order
# order_id: 
# price:
# quantity: 
# disclosed_quantity:
# trigger_price:
# validity: 
# order_type:
client.modify_order(order_id = "", price = "7.0", quantity = "2", disclosed_quantity = "0", trigger_price = "0", validity = "DAY", order_type='')

# Cancel an order
client.cancel_order(order_id = "")

# isVerify: isVerify is an optional param. Default value is 'False'
# This is delay type. if order id along with isVerify as True will be passed then check the status of the given order id and then proceed to further
client.cancel_order(order_id = "", isVerify=True)

# Cancel cover order
# amo: 
# isVerify: isVerify is an optional param. Default value is 'False'
client.cancel_cover_order(order_id = "", amo = "", isVerify=False)

# Cancel bracket order
# amo: 
# isVerify: isVerify is an optional param. Default value is 'False'
client.cancel_bracket_order(order_id = "", amo = "", isVerify=False)


# Get Order Book
client.order_report()

# Get Order History
client.order_history(order_id = "")

# Get Trade Book
client.trade_report()

# Get Detailed Trade Report for specific order id. 
client.trade_report(order_id = "")

# Get Positions
client.positions()

# Get Portfolio Holdings
client.holdings()

# Get Limits
client.limits(segment="", exchange="", product="")

# Get Margin required for Equity orders. 
client.margin_required(exchange_segment = "", price = "", order_type= "", product = "",   quantity = "", instrument_token = "",  transaction_type = "")

# Get Scrip Master CSV file
client.scrip_master()

# Get Scrip Master CSV file for specific Exchange Segment. 
# exchange_segment: Section of a stock exchange. Its a mandatory param. Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, bcs_fo
client.scrip_master(exchange_segment = "")

# Search for the Scrip details from Scrip master file
# exchange_segment: Section of a stock exchange. Its a mandatory param. Expected values are nse_cm, bse_cm, nse_fo, bse_fo, cde_fo, bcs_fo
client.search_scrip(exchange_segment="cde_fo", symbol="", expiry="", option_type="",
                    strike_price="")

# Get quote details
instrument_tokens = [
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""},
    {"instrument_token": "", "exchange_segment": ""}
]
# Get quotes details - `quote_type` can be `all`, `depth`, `ohlc`, `ltp`, `oi`, `52w`, `circuit_limits`, `scrip_details`
# By default, `quote_type` is set as `all`, which means you will get the complete data.
# Quotes API can be accessed without completing login by passing `session_token`, `sid`, and `server_id`.
client.quotes(instrument_tokens = instrument_tokens, quote_type = "")


# Subscribe method will get you the live feed details of the given tokens.
# By Default isIndex is set as False and you want to get the live feed to index scrips set the isIndex flag as True 
# By Default isDepth is set as False and you want to get the depth information set the isDepth flag as True
client.subscribe(instrument_tokens = instrument_tokens, isIndex=False, isDepth=False)

# Un_Subscribes the given tokens. First the tokens will be checked weather that is subscribed. If not Subscribed we will send you the error message else we will unsubscribe the give tokens
client.un_subscribe(instrument_tokens=instrument_tokens, isIndex=False, isDepth=False)

#Order Feed 
client.subscribe_to_orderfeed()

#Terminate user's Session
client.logout()
```


## Documentation for API Endpoints

| Class               | Method                                                                                | Description              |
|---------------------|---------------------------------------------------------------------------------------|--------------------------|
| *Base Url*          | [**neo_api_client.BaseUrl**](docs/Base_url.md#base_url)                               | Base Url                 |
| *LoginAPI*          | [**neo_api_client.SessionINIT**](docs/Session_init.md#session_init)                   | Initialise Session       |
| *User Verification* | [**neo_api_client.SendOTP**](docs/SendOTP.md#user_verification_send_otp)              | Send OTP                 |
| *User Verification* | [**neo_api_client.VerifyOTP**](docs/VerifyOTP.md#user_verification_verify_otp)        | Send OTP                 |
| *TOTP LoginAPI*     | [**neo_api_client.Totp_verify_user**](docs/Totp_verify_user.md#totp_verify_user)      | Verify User              |
| *TOTP LoginAPI*     | [**neo_api_client.Totp_registration**](docs/Totp_register.md#totp_register)           | TOTP Registration        |
| *TOTP LoginAPI*     | [**neo_api_client.Totp_login**](docs/Totp_login.md#totp_login)                        | TOTP Login               |
| *TOTP LoginAPI*     | [**neo_api_client.Totp_validation**](docs/Totp_validate.md#totp_validate)             | TOTP Validation          |
| *TOTP LoginAPI*     | [**neo_api_client.Totp_deregister**](docs/Totp_deregister.md#totp_deregister)         | TOTP De-Register         |
| *QR Code LoginAPI*  | [**neo_api_client.Qr_code_link**](docs/Qr_code_link.md#qr_code_link)                  | QR Code Get Link         |
| *QR Code LoginAPI*  | [**neo_api_client.Qr_code_session**](docs/Qr_code_session.md#qr_code_session)         | QR Code Generate Session |
| *Place Order*       | [**neo_api_client.placeorder**](docs/Place_Order.md#place_order)                      | Place Order              |
| *Modify Order*      | [**neo_api_client.modifyorder**](docs/Modify_Order.md#modify_order)                   | Modify Order             |
| *Cancel Order*      | [**neo_api_client.cancelorder**](docs/Cancel_Order.md#cancel_order)                   | Cancel Order             |
| *Order Report*      | [**neo_api_client.orderreport**](docs/Order_report.md#order_report_and_order_history) | Order Report             |
| *Trade Report*      | [**neo_api_client.tradereport**](docs/Trade_report.md#trade_report)                   | Trade Report             |
| *Positions*         | [**neo_api_client.positions**](docs/Positions.md#positions)                           | Positions                |
| *Holdings*          | [**neo_api_client.holdings**](docs/Holdings.md#holdings)                              | Holdings                 |
| *Limits*            | [**neo_api_client.limits**](docs/Limits.md#limits)                                    | Limits                   |
| *Margin Required*   | [**neo_api_client.margin_required**](docs/Margin_Required.md#margin_required)         | Margin Required          |
| *Scrip Master*      | [**neo_api_client.scrip_master**](docs/Scrip_Master.md#scrip_master)                  | Scrip Master             |
| *Search Scrip*      | [**neo_api_client.scrip_search**](docs/Scrip_Search.md#scrip_search)                  | Scrip Search             |
| *Quotes*            | [**neo_api_client.quotes**](docs/Quotes#quotes)                           | Quotes                   |
| *Subscribe*         | [**neo_api_client.subscribe**](docs/webSocket.md#websocket)                           | Subscribe                |

