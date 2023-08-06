from loguru import logger

from .pos import POS, POSAPI
from .bc_reader import BCReader
from .epp import EPP


class CCBPos(POS):

    def __init__(self, bcr: BCReader, epp: EPP, api: POSAPI, device: str, merchant: str) -> None:
        super().__init__(bcr, epp, device, merchant)
        self.api = api

    def sign_in(self) -> str:
        resp = self.api.exec({
            "tranCode": "0800",
            "device": self.device,
            "merchant": self.merchant
        })

        b62 = resp['b62']
        wkey = b62[:32]
        wkeysum = b62[32:40]
        mkey = b62[40:56]
        mkeysum = b62[56+16:80]
        logger.debug('pin key: {}, mac key: {}', wkey, mkey)

        with self.epp:
            r = self.epp.write_pin_key(wkey)
            logger.debug('write_pin_key {}, {}', r, wkeysum)

            if r.lower() != wkeysum:
                raise RuntimeError('Failed to write PIN key')

            r = self.epp.write_mac_key(mkey)
            logger.debug('write_mac_key {}, {}', r, mkeysum)
            if r.lower() != mkeysum:
                raise RuntimeError('Failed to write MAC key')

        return resp['batch']

    def sign_out(self) -> None:
        self.api.exec({
            "tranCode": "0820",
            "device": self.device
        })

    def pay(self, amount: int) -> dict:
        if amount < 1:
            raise RuntimeError('The amount must be greater than zero')

        bci = None
        with self.bcr:
            bci = self.bcr.read_info(amount)
            logger.debug("bci: {}", bci)

        if not bci:
            raise RuntimeError('Failed to read card information')

        pin = None
        with self.epp:
            pin = self.epp.read_pin(bci.pan)
            logger.debug('pin: {}', pin)

        if not pin:
            raise RuntimeError('Failed to read PIN')

        resp = self.api.exec({
            "tranCode": "02002",
            'amount': amount,
            "accountSN": bci.pan,
            "track2": bci.track2,
            "device": self.device,
            "password": pin,
            "ic55": bci.ic55
        })

        mac = None
        with self.epp:
            mac = self.epp.read_mac(resp['data'])
            logger.debug('mac: {}', mac)

        if not mac:
            raise RuntimeError('Failed to calculate MAC')

        result = self.api.exec({
            "tranCode": "0000",
            "id": resp['id'],
            "mac": mac[:16]
        })

        return result
