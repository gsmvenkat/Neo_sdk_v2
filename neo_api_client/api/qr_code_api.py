import json
from pickletools import uint1

from requests import session


class QrCodeAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        # self.base64_token = api_client.configuration.base64_token
        self.rest_client = api_client.rest_client
        self.totp_session = None

    def qr_code_get_link(self, ucc=None):
        # TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIxbUtrVVhxbEh1NmU0TDQ0NHpGaW5HN2M2dHNhIiwibmJmIjoxNzI4NDgwMzgxLCJhenAiOiIxbUtrVVhxbEh1NmU0TDQ0NHpGaW5HN2M2dHNhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL25hcGkua290YWtzZWN1cml0aWVzLmNvbTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjI1OTI0ODAzODEsImlhdCI6MTcyODQ4MDM4MSwianRpIjoiYTk0ZmYxNjUtMzJlNy00ZDZlLWFhNTUtYzU2Y2FmYmQ4NzBlIn0.G4Lag7ZsYw-5ys_-RdMQiqHh7XXyGevFd4xNeLPwoAxOiU1I_1jt3khD_mFsYst3jKwEjRYB65itiVLm3T_IPpkGiuWa7LKlTTSCu5M4QqjZP1w6PLpED5-p7dg2ZgulvQpi_cW7Mm4QAgUWZUh8M1VXmzF4PzZ6DE3TfRXX6vqZfIUT96B6d-aW07hqte-xB_pwCnBWTLeZekA7__soqPrNsUZKRyFdQnsr9gpRcae_rg5sJardn_Yg97jylec9CoBSxpBs7j1ZeLCYWmMioRNnL5O3l4YCmLO8NK8hpxFRVyoiwchlCYdGOCDEIARF3VssTvf-i8E7xAfGTB--rA"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        URL = self.api_client.configuration.get_url_details("qr_code_get_link")
        # TODO Remove the below line
        URL = "https://gw-napi.kotaksecurities.com/login/1.0/algo-user/v5/login/authorization/dialog"

        query_params = {'id': ucc}
        qr_code_link = self.rest_client.request(
            url=URL, method='GET',
            headers=header_params,
            query_params=query_params
        )
        qr_code_link_data = qr_code_link.json()
        return qr_code_link_data

    def qr_code_generate_session(self, ott=None, ucc=None):
        # TODO Remove the below line
        self.api_client.configuration.bearer_token = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQxNjcxIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiIxbUtrVVhxbEh1NmU0TDQ0NHpGaW5HN2M2dHNhIiwibmJmIjoxNzI4NDgwMzgxLCJhenAiOiIxbUtrVVhxbEh1NmU0TDQ0NHpGaW5HN2M2dHNhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL25hcGkua290YWtzZWN1cml0aWVzLmNvbTo0NDNcL29hdXRoMlwvdG9rZW4iLCJleHAiOjI1OTI0ODAzODEsImlhdCI6MTcyODQ4MDM4MSwianRpIjoiYTk0ZmYxNjUtMzJlNy00ZDZlLWFhNTUtYzU2Y2FmYmQ4NzBlIn0.G4Lag7ZsYw-5ys_-RdMQiqHh7XXyGevFd4xNeLPwoAxOiU1I_1jt3khD_mFsYst3jKwEjRYB65itiVLm3T_IPpkGiuWa7LKlTTSCu5M4QqjZP1w6PLpED5-p7dg2ZgulvQpi_cW7Mm4QAgUWZUh8M1VXmzF4PzZ6DE3TfRXX6vqZfIUT96B6d-aW07hqte-xB_pwCnBWTLeZekA7__soqPrNsUZKRyFdQnsr9gpRcae_rg5sJardn_Yg97jylec9CoBSxpBs7j1ZeLCYWmMioRNnL5O3l4YCmLO8NK8hpxFRVyoiwchlCYdGOCDEIARF3VssTvf-i8E7xAfGTB--rA"
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token}
        URL = self.api_client.configuration.get_url_details("qr_code_generate_session")
        # TODO Remove the below line
        URL = "https://gw-napi.kotaksecurities.com/login/1.0/algo-user/v5/login/generate-session-token"
        body_params = {
            "ott": ott,
            "id": ucc
        }
        session = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        print(session)
        session_data = None
        if 200 <= session.status_code <= 299:
            session_data = session.json()
            self.api_client.configuration.edit_token = session_data.get("data").get("token")
            self.api_client.configuration.edit_sid = session_data.get("data").get("sid")
            self.api_client.configuration.edit_rid = session_data.get("data").get("rid")
            self.api_client.configuration.serverId = session_data.get("data").get("hsServerId")
        print(1111, self.api_client.configuration.__dict__)
        return session_data

