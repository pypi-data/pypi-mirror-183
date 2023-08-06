import base64
import json
import requests

from abc import ABC, abstractmethod
from loguru import logger

from .bc_reader import BCReader
from .epp import EPP


class POSAPI(object):

    def __init__(self, url: str, token: str, pwd: str):
        super(POSAPI, self).__init__()
        self.url = url
        self.token = token
        self.pwd = pwd

    def exec(self, params: dict) -> dict:
        logger.debug('request: {}', params)
        r = requests.post(self.url, auth=(self.token, self.pwd), data=params)
        json_text = base64.decodebytes(r.text.encode('utf-8')).decode('utf-8')
        result = json.loads(json_text)
        logger.debug('response: {}', result)
        return result


class POS(ABC):

    _batch = None

    def __init__(self, bcr: BCReader, epp: EPP, device: str, merchant: str) -> None:
        super().__init__()
        self.bcr = bcr
        self.epp = epp
        self.device = device
        self.merchant = merchant

    @abstractmethod
    def sign_in(self) -> str:
        pass

    @abstractmethod
    def sign_out(self) -> None:
        pass

    @abstractmethod
    def pay(self, amount: int) -> dict:
        pass

    def __enter__(self):
        if POS._batch:
            return

        POS._batch = self.sign_in()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not POS._batch:
            return

        try:
            self.sign_out()
        except Exception as e:
            logger.debug(e)

        POS._batch = None

        return True
