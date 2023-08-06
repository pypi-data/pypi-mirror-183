import os
import json
from pickle import FALSE, NONE
import boto3
import requests

from typing import Dict


class APIClient:
    r"""
    A wrapper of python reqeusts module
    It is to handle all GET,POST,PUT,DELETE requests
    """

    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "config.json"), "r") as f:
            self.config = json.load(f)
        self.backend_url =  self.config["backend_ip"]
        # self.headers = {"X-Alectio-Flavor": "PRO"}

    def POST_REQUEST(
        self, end_point: str, payload: dict = {}, auth: dict = {}, headers: dict = {}
    ):
        api_url = self.backend_url + end_point

        # print("#" * 100)
        # print(api_url)
        # print("#" * 100)

        response = requests.post(url=api_url, data=payload, headers=headers)
        if response.status_code not in [200, 201, 202, 203, 204, 2005, 206]:
            return True, None
        else:
            return False, response

    def AUTH_TOKEN_REQ(self, token):
        url = self.backend_url + f"/api/v2/python_client_auth/experiment_token/{token}"
        payload = {}
        headers = {"X-Alectio-Flavor": "PRO"}
        response = requests.request("GET", url, headers=headers, data=payload).json()

        # print("#" * 100)
        # print(response)
        # print("#" * 100)

        return response["data"]["access_token"]
