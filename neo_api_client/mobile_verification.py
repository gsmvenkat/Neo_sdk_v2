import requests

from neo_api_client.urls import GENERATE_OTP_URL, VALIDATE_OTP_URL, TOTP_VERIFY_USER_URL, TOTP_DE_REGISTER_URL, \
    TOTP_REGISTER_URL


class UserVerification:
    def __init__(self, mobile_number):
        self.mobile_number = mobile_number
        self.origin = "cug-cms.kotaksecurities.com"
        self.session_id = None
        self.ucc = None

    def send_otp(self, resend=False):
        URL = GENERATE_OTP_URL
        headers = {
            "Origin": self.origin
        }
        request_body = {
            "mobile": self.mobile_number,
            "resend": resend
        }
        generate_otp = requests.post(url=URL, json=request_body, headers=headers)
        if generate_otp.status_code == 201:
            generate_otp = generate_otp.json()
            self.session_id = generate_otp.get("data").get("sessionId")
        else:
            generate_otp = generate_otp.json()
        return generate_otp

    def verify_otp(self, code=None):
        URL = VALIDATE_OTP_URL
        headers = {
            "Origin": self.origin
        }
        request_body = {
            "mobile": self.mobile_number,
            "code": code,
            "sessionId": self.session_id
        }
        verify_otp = requests.post(url=URL, json=request_body, headers=headers)
        generate_otp = verify_otp.json()
        return generate_otp

    def totp_verify_user(self, ucc=None):
        URL = TOTP_VERIFY_USER_URL
        request_body = {
            "mobileNumber": self.mobile_number,
            "ucc": ucc,
            "sessionId": self.session_id
        }
        verify_user = requests.post(url=URL, json=request_body)
        # verify_user = verify_user.json()
        if verify_user.status_code == 200:
            verify_user = verify_user.json()
            self.session_id = verify_user.get("data").get("sessionID")
        else:
            verify_user = verify_user.json()
        return verify_user

    def totp_registration(self, totp=None):
        URL = TOTP_REGISTER_URL
        request_body = {
            "sessionID": self.session_id,
            "totp": totp
        }
        verify_user = requests.post(url=URL, json=request_body)
        verify_user = verify_user.json()
        return verify_user

    def totp_de_register(self, mpin=None, ucc=None):
        URL = TOTP_DE_REGISTER_URL
        request_body = {
            "mpin": mpin,
            "ucc": ucc,
            "sessionId": self.session_id
        }
        verify_user = requests.post(url=URL, json=request_body)
        verify_user = verify_user.json()
        return verify_user