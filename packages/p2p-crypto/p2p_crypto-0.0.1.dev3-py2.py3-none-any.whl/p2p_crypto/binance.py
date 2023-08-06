import json
import requests
import random
import p2p_crypto.config as config


class Exchange:
    def __init__(self) -> None:
        self.prices = None
        self.nicknames = None
        self.merchant = None
        self.limits = None
        self.fiat = None
        self.token = None
        self.payments = None

    def getPrice(self, fiat, token, payments=[], merchant=False, rows=1, operation="BUY"):
        pass


class Binance(Exchange):
    def getPrice(self, fiat, token, payments=[], merchant=False, rows=1, operation="BUY"):
        '''
        Args:
        fiat (str) - Base currency
        token (str) - Cryptocurrency token
        payment (list) - Payment method. List of payment methods: p2p.config.paymentMethods
        merchant (bool) - List only adverts from merchants
        rows (int) - Amount of rows to output
        operation (str) - Operation type. Values: BUY/SELL
        
        Return: 
        List - JSON with adverts data
        '''

        userAgent = random.choice(config.USER_AGENT)
        payments = [config.paymentTypes[x] for x in payments]
        headers = {
            "Host": "p2p.binance.com",
            "User-Agent": userAgent,
            "Accept": "*/*",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": f"https://p2p.binance.com/en/trade/TinkoffNew/{token.upper()}?fiat={fiat.upper()}",
            "lang": "en",
            "content-type": "application/json",
            "Content-Length": "173",
            "Origin": "https://p2p.binance.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "trailers"
        }

        data = {
            "proMerchantAds": merchant,
            "page": 1,
            "rows": rows,
            "payTypes": payments,
            "countries": [],
            "publisherType": None,
            "fiat": fiat,
            "tradeType": operation,
            "asset": token,
            "merchantCheck": False
        }

        r = requests.post(
            'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)

        self.data = r.json()["data"]

        self.prices = [x["adv"]["price"] for x in self.data]
        self.nicknames = [x["advertiser"]["nickName"] for x in self.data]
        self.merchant = [x["advertiser"]["proMerchant"] for x in self.data]
        self.limits = [{"min": x["adv"]["minSingleTransQuantity"],
                        "max": x["adv"]["maxSingleTransQuantity"]} for x in self.data]
        self.fiat = fiat
        self.token = token
        self.payments = [y[0]["tradeMethodShortName"]
                         for y in [x["adv"]["tradeMethods"] for x in self.data]]

        return self.data

    def prettify(self, filename, mode="pdImage"):
        '''
        Args:
        mode (str) - [pdImage, PILImage, plain] default: pdImage
        pdImage - returns pandas DataFrame in png format
        PILImage - returns png image by a given template
        plain - returns output as a plain text
        
        filename (str) - for modes pdImage, PILImage specify filename for PNG file
        Return:
        Str: Filename or plain text
        '''

        from p2p_crypto.prettify import Binance
        return Binance(exchange=self).prettify(mode=mode, filename=filename)