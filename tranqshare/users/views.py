from datetime import date
from decimal import Decimal
from http.client import HTTPResponse
from multiprocessing import context
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView
from django.views.decorators.http import require_http_methods

from tranqshare.users.models import Addresses, Currency, Deposit, KYCVerify, TransactionHistory, Wallet, Withdraw

from tranqshare.utils.emails import support_email
from django.contrib.auth.decorators import login_required

from django.template.loader import get_template
from django.utils.safestring import mark_safe

from django_htmx.http import trigger_client_event

from tranqshare.utils.logger import LOGGER
from .forms import VerifyForm

User = get_user_model()
import datetime
# dt = datetime.datetime.now().strftime ("%Y%m%d%s")

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = self.request.user.transaction.all().order_by("-modified")[:50]
        return context

user_detail_view = UserDetailView.as_view()


class UserVerifyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = KYCVerify
    template_name="users/verify.html"
    fields = ['pass_front', 'pass_back']
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    # def get_object(self):
    #     return self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        # if 'cur' in self.request.session and self.request.user.is_authenticated and Addresses.objects.filter(currency=Currency.objects.get(name=self.request.session['cur'])).exists():
        #     LOGGER.info(self.request.session['cur'])
        #     currency = Currency.objects.get(name=self.request.session['cur'])
        #     addresses = Addresses.objects.get(currency=currency)
        # elif 'cur' in self.request.session and self.request.user.is_authenticated and Addresses.objects.filter(currency=Currency.objects.get(name=self.request.session['cur'])).exists():
        #     LOGGER.info(self.request.session['cur'])
        #     addresses = Addresses.objects.all().first()
        # else:
        #     addresses = None
        # context['wallet'] = addresses
        return context


verify_view = UserVerifyView.as_view()

class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["first_name", "name", "last_name", "country", "phone"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    # def get_context_data(self, **kwargs):
    #     if 'cur' in self.request.session and self.request.user.is_authenticated and Addresses.objects.filter(currency=Currency.objects.get(name=self.request.session['cur'])).exists():
    #         LOGGER.info(self.request.session['cur'])
    #         currency = Currency.objects.get(name=self.request.session['cur'])
    #         addresses = Addresses.objects.get(currency=currency)
    #     elif 'cur' in self.request.session and self.request.user.is_authenticated and Addresses.objects.filter(currency=Currency.objects.get(name=self.request.session['cur'])).exists():
    #         LOGGER.info(self.request.session['cur'])
    #         addresses = Addresses.objects.all().first()
    #     else:
    #         addresses = None
    #     context = super().get_context_data(**kwargs)
    #     context['wallet'] = addresses
    #     return context


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

# @require_http_methods(['GET', 'POST'])
# def wallets(request):
#     wallets = Addresses.objects.get(currency__name=request.session["cur"]) if request.session['cur'] else None
#     # amount = request.POST.get("amount")
#     # deposit = Deposit.objects.create(user=request.user, currency=Currency.objects.get(id=int(currency)), amount=Decimal(amount), status=Deposit.PENDING)
#     # TransactionHistory.objects.create(id=deposit.id, transaction_type=TransactionHistory.DEPOSIT, user=request.user, currency=Currency.objects.get(id=int(currency)), amount=Decimal(amount), status=Withdraw.PENDING)
#     return render(request, "snippets/wallets.html", context={"wallets":wallets})


@require_http_methods(['GET', 'POST'])
def deposit(request):
    currency = request.POST.get("currency")
    curre = Currency.objects.get(name=currency)
    dt = datetime.datetime.now().strftime("%Y%m%d%s")
    amount = request.POST.get("amount")
    if int(amount) > 0:
        deposit = Deposit.objects.create(user=request.user, uuid=f"DEPOSIT-{dt}", currency=Currency.objects.get(name=currency), amount=Decimal(amount), status=Deposit.PENDING)
        TransactionHistory.objects.create(uuid=deposit.uuid, transaction_type=TransactionHistory.DEPOSIT, user=request.user, currency=Currency.objects.get(name=currency), amount=Decimal(amount), status=Withdraw.PENDING)
        return render(request, "snippets/wallets.html", context={"wallet":Addresses.objects.get(currency=curre)})
    return render(request, "snippets/wallets.html", context={"wallet":Addresses.objects.get(currency=curre)})
    # trigger_client_event(response, 'currency', {})
    # return response

def suf_bal(request):
    amount = request.POST.get("amount")
    curr = int(request.session["cur"])

    LOGGER.info(amount)
    LOGGER.info(curr)

    if curr == "BTC" and Decimal(amount) < Decimal(request.user.wallet.btc):
        rate = Currency.objects.get(name="BTC")
        LOGGER.info(rate.amount)
        price = Decimal(amount) / Decimal(rate.amount)
        context = {
            'price': price,
        }
        return render(request, "snippets/button.html", context)
    elif curr == "ETH" and Decimal(amount) < Decimal(request.user.wallet.eth):
        rate = Currency.objects.get(name="ETH")
        LOGGER.info(rate.amount)
        price = Decimal(amount) / Decimal(rate.amount)
        context = {
            'price': price,
        }
        return render(request, "snippets/button.html", context)
    elif curr == "USDT" and Decimal(amount) < Decimal(request.user.wallet.usdt):
        rate = Currency.objects.get(name="USDT")
        price = Decimal(amount) / Decimal(rate.amount)
        context = {
            'price': price,
        }
        return render(request, "snippets/button.html", context)
    else:
        return HTTPResponse("Insufficient Balance")

    # return render(request, "snippets/button.html", context)

@require_http_methods(['GET', 'POST'])
def withdraw(request):
    dt = datetime.datetime.now().strftime("%Y%m%d%s")
    wallet = request.POST.get("wallet")
    currency = request.POST.get("currency")
    amount = request.POST.get("amount")
    curr =  Currency.objects.filter(name=currency).first()
    if int(amount) > 0 and Decimal(amount) <= request.user.wallet.btc and currency == "BTC":        # 'wallet' : addresses,
        wit = Withdraw.objects.create(user=request.user, wallet=str(wallet), uuid=f"WITDRAW-{dt}", currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        TransactionHistory.objects.create(uuid=wit.uuid, transaction_type=TransactionHistory.WITHDRAW, user=request.user, currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        return render(request, "snippets/complete.html")
    elif int(amount) > 0 and Decimal(amount) <= request.user.wallet.eth and currency == "ETH":        # 'wallet' : addresses,
        wit = Withdraw.objects.create(user=request.user, wallet=str(wallet), uuid=f"WITDRAW-{dt}", currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        TransactionHistory.objects.create(uuid=wit.uuid, transaction_type=TransactionHistory.WITHDRAW, user=request.user, currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        return render(request, "snippets/complete.html")
    elif int(amount) > 0 and Decimal(amount) <= request.user.wallet.usdt and currency == "USDT":        # 'wallet' : addresses,
        wit = Withdraw.objects.create(user=request.user, wallet=str(wallet), uuid=f"WITDRAW-{dt}", currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        TransactionHistory.objects.create(uuid=wit.uuid, transaction_type=TransactionHistory.WITHDRAW, user=request.user, currency=Currency.objects.get(name=currency), amount=amount, status=Withdraw.PENDING)
        return render(request, "snippets/complete.html")
    else:        # 'wallet' : addresses,
        return render(request, "snippets/complete.html")

# @require_http_methods(['GET'])
# def get_error(request):
#     currency = request.POST.get("currency")
#     amount = request.POST.get("amount")
#     wallet = Wallet.objects.get(user=request.user)
#     if currency == "1":
#         rate = Currency.objects.get(id=1)
#         currency = wallet.btc
#     elif currency == "2":
#         rate = Currency.objects.get(id=2)
#         currency = wallet.eth
#     elif currency == "3":
#         rate = Currency.objects.get(id=3)
#         currency = wallet.usdt

#     if Decimal(amount) > Decimal(currency):
#         status = "Error"
#         message = "Insufficient Balance"
#     else:
#         status = "Success"
#         message = Decimal(rate.amount) / Decimal(amount)


#     context = {
#         "currency": currency,
#         'message': message,
#         "status": status
#     }
#     return render(request, "snippets/error.html", context)


def get_currency(request):
    currency = request.GET.get("currency")
    # request.session["cur"] = currency
    request.session['cur'] = Currency.objects.filter(name=currency).first().name
    LOGGER.info(currency)

    if currency == "BTC":
        rate = Currency.objects.get(name="BTC")
    elif currency == "ETH":
        rate = Currency.objects.get(name="ETH")
    elif currency == "USDT":
        rate = Currency.objects.get(name="USDT")
    return render(request, "snippets/currency.html", context={"name":rate.name})


@require_http_methods(['GET'])
def get_error(request):
    amount = request.GET.get("amount")

    curr = int(request.session["cur"])

    LOGGER.info(amount)
    LOGGER.info(curr)

    if curr == "BTC" and Decimal(amount) < Decimal(request.user.wallet.btc):
        rate = Currency.objects.get(name="BTC")
        LOGGER.info(rate.amount)
        status = "Success"
        price = Decimal(amount) / Decimal(rate.amount)
        message = f"{price:.6f}"
    elif curr == "ETH" and Decimal(amount) < Decimal(request.user.wallet.eth):
        rate = Currency.objects.get(name="ETH")
        LOGGER.info(rate.amount)
        status = "Success"
        price = Decimal(amount) / Decimal(rate.amount)
        message = f"{price:.6f}"
    elif curr == "USDT" and Decimal(amount) < Decimal(request.user.wallet.usdt):
        rate = Currency.objects.get(name="USDT")
        LOGGER.info(rate.amount)
        status = "Success"
        price = Decimal(amount) / Decimal(rate.amount)
        message = f"{price:.6f}"
    else:
        status = "Error"
        message = f"Insufficient Balance in your wallet"


    context = {
        'message': message,
        "status": status
    }
    return render(request, "snippets/error.html", context)


@require_http_methods(['GET'])
def d_error(request):
    amount = request.GET.get("amount")

    if Decimal(amount) <= Decimal(999):
        message = "STARTER PLAN"
    elif Decimal(amount) >= 999.00 or Decimal(amount) <= Decimal(9999):
        message = "INTERMEDIATE PLAN"
    elif Decimal(amount) >= 10000.00 or Decimal(amount) <= Decimal(25000):
        message = "DIAMOND PLAN"
    elif Decimal(amount) >= 25001.00 or Decimal(amount) <= Decimal(1000000000000000):
        message = "PLATINIUM PLAN"


    context = {
        'message': message,
    }
    return render(request, "snippets/error.html", context)

def complete(request):
    return render(request, "snippets/complete.html")
