import json

from neo_api_client import rest
from neo_api_client.exceptions import ApiException
from neo_api_client.urls import PROD_BASE_URL_GW_NAPI


class OrderHistoryAPI(object):
    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client

    def ordered_history(self, order_id):
        header_params = {'Authorization': "Bearer " + self.api_client.configuration.bearer_token,
                         "Sid": self.api_client.configuration.edit_sid,
                         "Auth": self.api_client.configuration.edit_token,
                         "neo-fin-key": self.api_client.configuration.get_neo_fin_key(),
                         "accept": "application/json",
                         "Content-Type": "application/x-www-form-urlencoded"}
        body_params = {"nOrdNo": order_id}
        query_params = {"sId": self.api_client.configuration.serverId}
        if self.api_client.configuration.base_url == PROD_BASE_URL_GW_NAPI:
            URL = self.api_client.configuration.get_url_details("order_history_napi")
        else:
            URL = self.api_client.configuration.get_url_details("order_history")

        try:
            history_report = self.rest_client.request(
                url=URL, method='POST',
                query_params=query_params,
                headers=header_params,
                body=body_params
            )
            return {"data": json.loads(history_report.text)}
        except ApiException as ex:
            return {"error": ex}
