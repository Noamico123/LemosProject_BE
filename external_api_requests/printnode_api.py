import json
import os
from typing import List, Any

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from consts import *
from models.models import Printer


class PrintNodeAPI:

    def __init__(self):
        load_dotenv()

        self.req = requests.Session()
        self.headers = {'Accept': 'application/json'}
        self.api_key = os.getenv(API_KEY)
        self.auth = HTTPBasicAuth('apikey', self.api_key)

    def get_user_data_from_printnode_api(self):
        response = self.req.get(BASE_URL + WHOAMI, headers=self.headers, auth=self.auth)

        return response.text

    def get_printers_data_from_printnode_api(self):
        res = self.req.get(BASE_URL + PRINTERS, headers=self.headers, auth=self.auth)

        return json.loads(res.text)

    def get_user_data_from_printnode_api_by_key(self, api_key: str):
        self.api_key = api_key
        self.auth = HTTPBasicAuth('apikey', self.api_key)
        response = self.req.get(BASE_URL + PRINTERS, headers=self.headers, auth=self.auth)
        print(response.text)
        return json.loads(response.text)

    def post_jobs_for_print(self):
        self.headers = {'Accept': 'application/json', "Content-Type": "application/json"}
        self.api_key = os.getenv(API_KEY)
        self.auth = HTTPBasicAuth('apikey', self.api_key)
        data = {
            "printerId": 34,
            "title": "My Test PrintJob",
            "contentType": "pdf_uri",
            "content": "http:\/\/sometest.com\/pdfhere",
            "source": "api documentation!"
        }

        response = self.req.post('https://api.printnode.com/printjobs', headers=self.headers, auth=self.auth, data=data)
        print(response.status_code)

    @staticmethod
    def get_printers_list(response_json: List[Any]) -> List[Printer]:
        printers = []

        for printer in response_json:
            capabilities = printer.get('capabilities')

            printers.append(
                Printer(
                    id=str(printer.get('id')),
                    name=printer.get('name'),
                    description=printer.get('description'),
                    nickname="",
                    paper_types=str(len(capabilities.get('papers'))),
                    state=printer.get('state')
                )
            )

        return printers

