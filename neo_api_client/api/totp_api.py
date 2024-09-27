import json

from requests import session


class TotpAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        # self.base64_token = api_client.configuration.base64_token
        self.rest_client = api_client.rest_client
        self.totp_session = None

    def totp_verify_user(self, mobile_number=None, ucc=None):
        #TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJuZW9hZG1pbiIsImF1dCI6IkFQUExJQ0FUSU9OX1VTRVIiLCJhdWQiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwibmJmIjoxNzI3MDczOTc5LCJhenAiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjc3NjYyODEzNTg1MjYyMjAsImlhdCI6MTcyNzA3Mzk3OSwianRpIjoiM2Y2NDg4ZDktOGYzMi00N2YwLTg4OGQtYjAzYTg0MzRlNTU5In0.Hyr30dvmcyArD1HphxEiPRwBW2Kk_xHSIJjK_6chH4Jf49rNKYHVRNfFtt5aPMfY6tiNiSwwCuxeGCdEVfuSE3XcoeIDi9H5o0PKhlOAkFZJmPaze6GQMQm8NvDL-32CmpwGk92cUTMupcYQiLQT0NuB7kepxM4mSkaH-ec489K2nqd3Yyj4BanjKOsb15mrq9tdeWwy7qbWG-9qyND1ERArv957kJotkdIzs2RGCE4SARsfcY737fAVQ7vBcXzbE-17d49AZ2K4ChU2r0MIeue4SdZW9Nuioebwit7Mmu3c5nBK_yDUQ0YDG1ic9In2qiCTgJAGn8q0qWRkTghaDg"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        URL = self.api_client.configuration.get_url_details("totp_verify_user")
        body_params = {
            "mobileNumber": mobile_number,
            "ucc": ucc
        }
        verify_user = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        verify_user_data = verify_user.json()
        if 200 <= verify_user.status_code <= 299:
            self.api_client.configuration.totp_session_id = verify_user_data.get("data").get("sessionID")
        return verify_user_data

    def totp_registration(self, totp=None):
        #TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJuZW9hZG1pbiIsImF1dCI6IkFQUExJQ0FUSU9OX1VTRVIiLCJhdWQiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwibmJmIjoxNzI3MDczOTc5LCJhenAiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjc3NjYyODEzNTg1MjYyMjAsImlhdCI6MTcyNzA3Mzk3OSwianRpIjoiM2Y2NDg4ZDktOGYzMi00N2YwLTg4OGQtYjAzYTg0MzRlNTU5In0.Hyr30dvmcyArD1HphxEiPRwBW2Kk_xHSIJjK_6chH4Jf49rNKYHVRNfFtt5aPMfY6tiNiSwwCuxeGCdEVfuSE3XcoeIDi9H5o0PKhlOAkFZJmPaze6GQMQm8NvDL-32CmpwGk92cUTMupcYQiLQT0NuB7kepxM4mSkaH-ec489K2nqd3Yyj4BanjKOsb15mrq9tdeWwy7qbWG-9qyND1ERArv957kJotkdIzs2RGCE4SARsfcY737fAVQ7vBcXzbE-17d49AZ2K4ChU2r0MIeue4SdZW9Nuioebwit7Mmu3c5nBK_yDUQ0YDG1ic9In2qiCTgJAGn8q0qWRkTghaDg"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        URL = self.api_client.configuration.get_url_details("totp_registration")
        body_params = {
            "sessionID": self.api_client.configuration.totp_session_id,
            "totp": totp
        }
        totp_register = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        totp_register = totp_register.json()
        return totp_register

    def totp_login(self, mobile_number=None, ucc=None, totp=None):
        #TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJuZW9hZG1pbiIsImF1dCI6IkFQUExJQ0FUSU9OX1VTRVIiLCJhdWQiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwibmJmIjoxNzI3MDczOTc5LCJhenAiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjc3NjYyODEzNTg1MjYyMjAsImlhdCI6MTcyNzA3Mzk3OSwianRpIjoiM2Y2NDg4ZDktOGYzMi00N2YwLTg4OGQtYjAzYTg0MzRlNTU5In0.Hyr30dvmcyArD1HphxEiPRwBW2Kk_xHSIJjK_6chH4Jf49rNKYHVRNfFtt5aPMfY6tiNiSwwCuxeGCdEVfuSE3XcoeIDi9H5o0PKhlOAkFZJmPaze6GQMQm8NvDL-32CmpwGk92cUTMupcYQiLQT0NuB7kepxM4mSkaH-ec489K2nqd3Yyj4BanjKOsb15mrq9tdeWwy7qbWG-9qyND1ERArv957kJotkdIzs2RGCE4SARsfcY737fAVQ7vBcXzbE-17d49AZ2K4ChU2r0MIeue4SdZW9Nuioebwit7Mmu3c5nBK_yDUQ0YDG1ic9In2qiCTgJAGn8q0qWRkTghaDg"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        URL = self.api_client.configuration.get_url_details("totp_login")
        body_params = {
             "mobileNumber": mobile_number,
            "ucc": ucc,
            "totp": totp
        }
        totp_login = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        totp_login_data = totp_login.json()
        if 200 <= totp_login.status_code <= 299:
            self.api_client.configuration.view_token = totp_login_data.get("data").get("token")
            self.api_client.configuration.sid = totp_login_data.get("data").get("sid")
        return totp_login_data

    def totp_validate(self, mpin=None):
        #TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJuZW9hZG1pbiIsImF1dCI6IkFQUExJQ0FUSU9OX1VTRVIiLCJhdWQiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwibmJmIjoxNzI3MDczOTc5LCJhenAiOiJudDlJSmxkYjc1X3dXQWhXNVlabU5CVU51RU1hIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2FwaW0ua290YWtzZWN1cml0aWVzLm9ubGluZTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjc3NjYyODEzNTg1MjYyMjAsImlhdCI6MTcyNzA3Mzk3OSwianRpIjoiM2Y2NDg4ZDktOGYzMi00N2YwLTg4OGQtYjAzYTg0MzRlNTU5In0.Hyr30dvmcyArD1HphxEiPRwBW2Kk_xHSIJjK_6chH4Jf49rNKYHVRNfFtt5aPMfY6tiNiSwwCuxeGCdEVfuSE3XcoeIDi9H5o0PKhlOAkFZJmPaze6GQMQm8NvDL-32CmpwGk92cUTMupcYQiLQT0NuB7kepxM4mSkaH-ec489K2nqd3Yyj4BanjKOsb15mrq9tdeWwy7qbWG-9qyND1ERArv957kJotkdIzs2RGCE4SARsfcY737fAVQ7vBcXzbE-17d49AZ2K4ChU2r0MIeue4SdZW9Nuioebwit7Mmu3c5nBK_yDUQ0YDG1ic9In2qiCTgJAGn8q0qWRkTghaDg"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "sid": self.api_client.configuration.sid,
                         "Auth": self.api_client.configuration.view_token
                         }
        URL = self.api_client.configuration.get_url_details("totp_validate")
        body_params = {
            "mpin": mpin
        }
        totp_validate = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        print(totp_validate, totp_validate.json())
        totp_validate_data = totp_validate.json()
        if 200 <= totp_validate.status_code <= 299:
            self.api_client.configuration.edit_token = totp_validate_data.get("data").get("token")
            self.api_client.configuration.edit_sid = totp_validate_data.get("data").get("sid")
            self.api_client.configuration.edit_rid = totp_validate_data.get("data").get("rid")
            self.api_client.configuration.serverId = totp_validate_data.get("data").get("hsServerId")
        return totp_validate_data