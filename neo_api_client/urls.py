#############################################################################
#                               WebSocket URLs
#############################################################################
WEBSOCKET_URL = "wss://mlhsm.kotaksecurities.com"

#############################################################################
#                               UAT BASE URLs
#############################################################################
UAT_BASE_URL = "https://nsbxapi-gw.kotaksecurities.com/"
PROD_BASE_URL = "https://mnapi.kotaksecurities.com/"
PROD_BASE_URL_ADC = "https://cnapi.kotaksecurities.com/"

#############################################################################
#                               PROD BASE URLs
#############################################################################
SESSION_UAT_BASE_URL = "https://nsbxapi.kotaksecurities.com/"
SESSION_PROD_BASE_URL = "https://mnapi.kotaksecurities.com/"
SESSION_PROD_BASE_URL_ADC = "https://cnapi.kotaksecurities.com/"

#############################################################################
#                               ORDER_FEED  URL
#############################################################################
ORDER_FEED_URL = "wss://mlhsi.kotaksecurities.com/realtime?sId={server_id}"
ORDER_FEED_URL_GDC = "wss://mlhsi.kotaksecurities.com/realtime?sId={server_id}"
ORDER_FEED_URL_GDCD = "wss://mdlhsi.kotaksecurities.com/realtime?sId={server_id}"
ORDER_FEED_URL_ADC = "wss://clhsi.kotaksecurities.com/realtime?sId={server_id}"

#############################################################################
#                               BASE_URL  URL
#############################################################################
BASE_URL = "https://lapi.kotaksecurities.com/algo-user/v5/get-base-url"

#############################################################################
#                               USER VERIFICATION URL
#############################################################################
GENERATE_OTP_URL = "https://lapi.kotaksecurities.com/algo-user/v5/register/otp/send"
VALIDATE_OTP_URL = "https://lapi.kotaksecurities.com/algo-user/v5/register/otp/verify"
TOTP_VERIFY_USER_URL = "https://lapi.kotaksecurities.com/login/v6/totp/verify-user"
TOTP_REGISTER_URL = "https://lapi.kotaksecurities.com/login/v6/totp/register"
TOTP_DE_REGISTER_URL = "https://lapi.kotaksecurities.com/login/v6/totp/deregister"