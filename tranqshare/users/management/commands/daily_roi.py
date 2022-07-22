from decimal import Decimal
import datetime


from django.core.management.base import BaseCommand
from django.utils.translation import gettext_lazy as _

# from requests_html import HTMLSession
from tranqshare.utils.logger import LOGGER
from tranqshare.users.models import TradeOpen, TransactionHistory, User, Currency

class Command(BaseCommand):
    """This command updates a users Daily ROI depending
     if the user has invested and his/her
    investment is running within three months before it stops.

    If the trade week is weekend, the ROI wont work.

    Args:
        BaseCommand (_type_): _description_
    """
    help = _("Get daily roi")

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        trade_open = True #TradeOpen.objects.filter(id=1,open=True).exists()
        for u in users:
            if u.invested:
                if u.wallet.total_asset >= 999 and u.wallet.total_asset < 9999:
                    duration = u.wallet.invested_date + datetime.timedelta(weeks=4)
                    if trade_open and u.wallet.invested_date and u.wallet.invested_date <= duration :
                        # td = u.wallet.invested_date + datetime.timedelta(days=90)
                        asset = u.wallet.total_asset #Deposit.objects.filter(user=u, status=Deposit.SUCCESS).aggregate(Sum('amount'))
                        roi =  Decimal(asset)  * Decimal(0.15)
                        TransactionHistory.objects.create(
                            user=u,
                            currency=Currency.objects.get(name="USDT"),
                            transaction_type= TransactionHistory.ROI,
                            status= TransactionHistory.SUCCESS,
                            amount= roi,
                        )
                        u_roi = u.roi + roi
                        User.objects.filter(username=u.username).update(roi=u_roi)

                        LOGGER.success(f"{u.username.title()} Asset:{asset} ROI:{Decimal(roi)}")
                    else:
                        LOGGER.error(f"{u.username.title()} Trade week is closed")
                elif u.wallet.total_asset >= 10000 and u.wallet.total_asset <= 25000:
                    duration = u.wallet.invested_date + datetime.timedelta(weeks=14)
                    if trade_open and u.wallet.invested_date and u.wallet.invested_date <= duration :
                        # td = u.wallet.invested_date + datetime.timedelta(days=90)
                        asset = u.wallet.total_asset #Deposit.objects.filter(user=u, status=Deposit.SUCCESS).aggregate(Sum('amount'))
                        roi =  Decimal(asset)  * Decimal(0.20)
                        TransactionHistory.objects.create(
                            user=u,
                            currency=Currency.objects.get(name="USDT"),
                            transaction_type= TransactionHistory.ROI,
                            status= TransactionHistory.SUCCESS,
                            amount= roi,
                        )
                        u_roi = u.roi + roi
                        User.objects.filter(username=u.username).update(roi=u_roi)

                        LOGGER.success(f"{u.username.title()} Asset:{asset} ROI:{Decimal(roi)}")
                    else:
                        LOGGER.error(f"{u.username.title()} Trade week is closed")
                elif u.wallet.total_asset > 25000 and u.wallet.total_asset <= 1000000000000:
                    duration = u.wallet.invested_date + datetime.timedelta(months=12)
                    if trade_open and u.wallet.invested_date and u.wallet.invested_date <= duration :
                        # td = u.wallet.invested_date + datetime.timedelta(days=90)
                        asset = u.wallet.total_asset #Deposit.objects.filter(user=u, status=Deposit.SUCCESS).aggregate(Sum('amount'))
                        roi =  Decimal(asset)  * Decimal(0.25)
                        TransactionHistory.objects.create(
                            user=u,
                            currency=Currency.objects.get(name="USDT"),
                            transaction_type= TransactionHistory.ROI,
                            status= TransactionHistory.SUCCESS,
                            amount= roi,
                        )
                        u_roi = u.roi + roi
                        User.objects.filter(username=u.username).update(roi=u_roi)

                        LOGGER.success(f"{u.username.title()} Asset:{asset} ROI:{Decimal(roi)}")
                    else:
                        LOGGER.error(f"{u.username.title()} Trade week is closed")
                else:
                    duration = u.wallet.invested_date + datetime.timedelta(months=2)
                    if trade_open and u.wallet.invested_date and u.wallet.invested_date <= duration :
                        # td = u.wallet.invested_date + datetime.timedelta(days=90)
                        asset = u.wallet.total_asset #Deposit.objects.filter(user=u, status=Deposit.SUCCESS).aggregate(Sum('amount'))
                        roi =  Decimal(asset)  * Decimal(0.10)
                        TransactionHistory.objects.create(
                            user=u,
                            currency=Currency.objects.get(name="USDT"),
                            transaction_type= TransactionHistory.ROI,
                            status= TransactionHistory.SUCCESS,
                            amount= roi,
                        )
                        u_roi = u.roi + roi
                        User.objects.filter(username=u.username).update(roi=u_roi)

                        LOGGER.success(f"{u.username.title()} Asset:{asset} ROI:{Decimal(roi)}")
                    else:
                        LOGGER.error(f"{u.username.title()} Trade week is closed")


        self.stdout.write("Daily ROI Retrieved Successfully.")
