import logging
import requests
import time


class KeglandRaptAPIClient:

    api_endpoint = "https://api.rapt.io/api"
    api_username = None
    api_secret = None

    api_bearer_token = {
        "token": None,
        "expiration": None
    }


    def __init__(self, api_username, api_secret, verbose=False):
        self.api_username = api_username
        self.api_secret = api_secret

        level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=level
        )


    def query_api(self, api_method, api_url, api_payload=None):
        url = f"{self.api_endpoint}{api_url}"
        
        bearer_token = self.__get_bearer_token()
        
        logging.debug(f"Query: {api_method} {url}")

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {bearer_token}"
        }

        if api_method == "GET":
            r = requests.get(url, params=api_payload, headers=headers)
        else:
            r = requests.post(url, data=api_payload, headers=headers)

        r.raise_for_status()

        return r.json()
        

    def __get_bearer_token(self):
        if self.api_bearer_token["token"] and self.api_bearer_token["expiration"] > time.time():
            return self.api_bearer_token["token"]

        logging.debug("Current Bearer token is invalid, getting new one")

        self.api_bearer_token["expiration"] = time.time() + 3600
        self.api_bearer_token["token"] = KeglandRaptAPIClient.get_active_bearer_token(self.api_username, self.api_secret)

        return self.api_bearer_token["token"]

    
    @staticmethod
    def get_active_bearer_token(api_username, api_secret):

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        payload = {
            "client_id": "rapt-user",
            "grant_type": "password",
            "username": api_username,
            "password": api_secret
        }

        r = requests.post(
            "https://id.rapt.io/connect/token",
            data=payload,
            headers=headers
        )

        r.raise_for_status()

        response = r.json()

        return response["access_token"]
