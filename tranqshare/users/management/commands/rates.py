from decimal import Decimal

import requests
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.core.management.base import BaseCommand
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _

# from requests_html import HTMLSession
from tranqshare.utils.logger import LOGGER
from tranqshare.users.models import Currency

User = get_user_model()
class Command(BaseCommand):
    """
    This just retrieves a set of crypto currency current prices
    """
    help = _("Collect current bank rates")
    """
    BTC=189
    ETH=195
    USDT=191
    """

    def handle(self, *args, **kwargs):
        url = "https://investing-cryptocurrency-markets.p.rapidapi.com/currencies/get-rate"

        headers = {
            'x-rapidapi-host': "investing-cryptocurrency-markets.p.rapidapi.com",
            'x-rapidapi-key': str(settings.API)
        }

        btc = {"fromCurrency":"189","toCurrency":"12","lang_ID":"1","time_utc_offset":"28800"}
        eth = {"fromCurrency":"195","toCurrency":"12","lang_ID":"1","time_utc_offset":"28800"}
        ltc = {"fromCurrency":"191","toCurrency":"12","lang_ID":"1","time_utc_offset":"28800"}
        usdt = {"fromCurrency":"205","toCurrency":"12","lang_ID":"1","time_utc_offset":"28800"}
        btc_res = requests.request("GET", url, params=btc, headers=headers)
        eth_res = requests.request("GET", url, params=eth, headers=headers)
        ltc_res = requests.request("GET", url, params=ltc, headers=headers)
        usdt_res = requests.request("GET", url, params=usdt, headers=headers)
        if btc_res.status_code != 200:
            return LOGGER.info(f"BTC {btc_res.status_code} - {btc_res.reason}")
        if eth_res.status_code != 200:
            return LOGGER.info(f"ETH {eth_res.status_code} - {eth_res.reason}")
        if ltc_res.status_code != 200:
            return LOGGER.info(f"LTC {ltc_res.status_code} - {ltc_res.reason}")
        if usdt_res.status_code != 200:
            return LOGGER.info(f"USDT {usdt_res.status_code} - {usdt_res.reason}")

        resb = btc_res.json()
        rese = eth_res.json()
        resl = ltc_res.json()
        resd = usdt_res.json()

        btcusd = Decimal(resb["data"][0][0]["basic"])
        ethusd = Decimal(rese["data"][0][0]["basic"])
        ltcusd = Decimal(resl["data"][0][0]["basic"])
        usdtusd = Decimal(resd["data"][0][0]["basic"])

        try:
            Currency.objects.get_or_create(name="BTC", amount=btcusd)
            LOGGER.info("BTC Created")
        except Currency.DoesNotExist:
            Currency.objects.filter(name="BTC").update(amount=btcusd)
            LOGGER.info("BTC Updated")

        try:
            Currency.objects.get_or_create(name="ETH", amount=ethusd)
            LOGGER.info("ETH Created")
        except Currency.DoesNotExist:
            Currency.objects.filter(name="ETH").update(amount=ethusd)
            LOGGER.info("ETH Updated")

        try:
            Currency.objects.get_or_create(name="LTC", amount=ltcusd)
            LOGGER.info("LTC Created")
        except Currency.DoesNotExist:
            Currency.objects.filter(name="LTC").update(amount=ltcusd)
            LOGGER.info("LTC Updated")

        try:
            Currency.objects.get_or_create(name="USDT", amount=usdtusd)
            LOGGER.info("USDT Created")
        except Currency.DoesNotExist:
            Currency.objects.filter(name="USDT").update(amount=usdtusd)
            LOGGER.info("USDT Updated")

        self.stdout.write("Exchange Rate Retrieved Successfully.")
