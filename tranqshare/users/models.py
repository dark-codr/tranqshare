from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    TextField,
    DecimalField,
    FileField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveSmallIntegerField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from stdimage import StdImageField
from model_utils.models import TimeStampedModel
from countries_plus.models import Country
from django.utils.timezone import now

class TradeOpen(TimeStampedModel):
    open = BooleanField(default=True)

    def __str__(self):
        return "Daily ROI Opened" if self.open else "Daily ROI Closed"

    class Meta:
        managed = True
        verbose_name = "Trade Week Open/Close"
        verbose_name_plural = "Trade Week Open/Close"

class Currency(TimeStampedModel):
    name = CharField(max_length=10, blank=False, unique=True)
    amount = DecimalField(decimal_places=7, max_digits=20, default=0.00, blank=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        verbose_name = "Crypto Currency"
        verbose_name_plural = "Crypto Currencies"
        ordering = ["-created"]

class User(AbstractUser):
    """
    Default custom user model for dan.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Middle Name"), blank=True, max_length=255, null=True)
    ref = CharField(_("Referral Link"), blank=True, max_length=25)
    bonus = DecimalField(decimal_places=2, max_digits=20, default=0.00, blank=False)
    roi = DecimalField(decimal_places=2, max_digits=20, default=0.00, blank=False)
    phone = CharField(unique=False, max_length=17, blank=True, help_text=_("eg: 018276475673"))
    country = ForeignKey(Country, on_delete=DO_NOTHING, default="US", blank=True, null=True)
    dp = StdImageField(upload_to="user/dp", blank=True)

    eth_address = CharField(max_length=250, blank=True)
    btc_address = CharField(max_length=250, blank=True)
    usdt_address = CharField(max_length=250, blank=True)

    recommended_by = ForeignKey("self", on_delete=CASCADE, blank=True, null=True, related_name='ref_by')

    first_investment = BooleanField(default=True)
    has_invested = BooleanField(default=False)
    has_toped = BooleanField(default=False)
    can_withdraw = BooleanField(default=False)
    can_topup = BooleanField(default=False)
    can_withdraw_roi = BooleanField(default=False)
    confirm = BooleanField(default=False)

    # @property
    # def ref(self):
    #     if self.first_name and self.last_name:
    #         return self.first_name[:3] + self.last_name[:3] + str(self.id)
    #     return self.email.split("@")[0]+str(self.date_joined.year)

    def get_recommended_profiles(self):
        qs = User.objects.all()
        # empty recommended lists
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self:
                my_recs.append(profile)
        return my_recs

    def get_recommended_count(self):
        qs = User.objects.all()
        # empty recommended lists
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self:
                my_recs.append(profile)
        return len(my_recs) or 0

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Wallet(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name=_("wallet"))
    btc = DecimalField(decimal_places=5, max_digits=20, default=0.00, blank=False)
    eth = DecimalField(decimal_places=5, max_digits=20, default=0.00, blank=False)
    usdt = DecimalField(decimal_places=5, max_digits=20, default=0.00, blank=False)
    invested_date = DateField(blank=True, null=True)

    @property
    def total_asset(self):
        currency = Currency.objects.all()

        # if currency[0].name == "BTC":
        btc = self.btc #/ currency[0].amount
        # if currency[1].name == "ETH":
        eth = self.eth #/ currency[1].amount
        # if currency[2].name == "USDT":
        usdt = self.usdt #/ currency[3].amount

        bonus = self.user.bonus

        total = float(btc + eth + usdt + bonus)
        return Decimal(total)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        managed = True
        verbose_name = "User Wallet"
        verbose_name_plural = "User Wallets"
        ordering = ["-created"]

class SmartsUpp(TimeStampedModel):
    script = TextField(blank=False)
    active = BooleanField(default=False)

    def __str__(self):
        return "Active Script" if self.active else "Inactive Script"

    class Meta:
        managed = True
        verbose_name = "Smartsupp Upload"
        verbose_name_plural = "Smartsupp Uploads"
        ordering = ["-created"]


class Testimonials(TimeStampedModel):
    name = CharField(max_length=250, blank=True)
    comment = TextField(blank=False)
    active = BooleanField(default=False)

    def __str__(self):
        return f"{self.name.title()} left a testimonial"

    class Meta:
        managed = True
        verbose_name = "Testimonial Upload"
        verbose_name_plural = "Testimonial Uploads"
        ordering = ["-created"]



class TransactionHistory(TimeStampedModel):
    # BTC = "BTC"
    # ETH = "ETH"
    # USDT = "USDT"
    # # AFFILIATE = "AFFILIATE"
    # CURRENCY = (
    #     (BTC, BTC),
    #     (ETH, ETH),
    #     (USDT, USDT),
    #     # (AFFILIATE, "AFFILIATE")
    # )

    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    AFFILIATE = "AFFILIATE"
    ROI = "ROI"
    TTYPE = (
        (AFFILIATE, AFFILIATE),
        (DEPOSIT, DEPOSIT),
        (WITHDRAW, WITHDRAW),
        (ROI, ROI),
    )

    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    STATUS = (
        (PENDING, PENDING),
        (FAILED, FAILED),
        (SUCCESS, SUCCESS),
    )

    user = ForeignKey(User, on_delete=CASCADE, related_name=_("transaction"))
    uuid = CharField(max_length=35, blank=True, unique=True)
    currency = ForeignKey(Currency, on_delete=CASCADE, related_name=_("transaction"))
    transaction_type = CharField(max_length=15, blank=False, choices=TTYPE, default=DEPOSIT)
    status = CharField(max_length=15, blank=False, choices=STATUS, default=PENDING)
    amount = DecimalField(decimal_places=7, max_digits=20, default=0.00, blank=False)

    def __str__(self):
        return str(self.user.username)


    class Meta:
        managed = True
        verbose_name = "Transaction History"
        verbose_name_plural = "Transaction Histories"
        ordering = ["-created"]

class FAQ(TimeStampedModel):
    question = CharField(max_length=700)
    answer = TextField('Answer')

    def __str__(self):
        return str(self.question)

    class Meta:
        managed = True
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["-created"]

class Privacy(TimeStampedModel):
    title = CharField(max_length=700)
    content = TextField('Content')

    def __str__(self):
        return str(self.title)

    class Meta:
        managed = True
        verbose_name = "Privacy"
        verbose_name_plural = "Privacies"
        ordering = ["-created"]

class Legals(TimeStampedModel):
    title = CharField(max_length=700)
    content = TextField('Content')

    def __str__(self):
        return str(self.title)

    class Meta:
        managed = True
        verbose_name = "Legal"
        verbose_name_plural = "Legals"
        ordering = ["-created"]

class KYCVerify(TimeStampedModel):
    user = OneToOneField(User, on_delete=CASCADE, related_name=_("kyc"))
    # id_type = CharField(
    #     choices=ID_TYPE, default=PASSPORT, max_length=15, null=True, blank=True
    # )
    pass_front = StdImageField(upload_to="passport/front", blank=True)
    pass_back = StdImageField(upload_to="passport/back", blank=True)
    # selfie = StdImageField(upload_to="passport/selfie", blank=True)
    # birth_cert = StdImageField(upload_to="passport/bcert", blank=True)

    approved = BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        managed = True
        verbose_name = "KYC Verification"
        verbose_name_plural = "KYC Verifications"
        ordering = ["-created"]


class Addresses(TimeStampedModel):
    # BTC = "BTC"
    # ETH = "ETH"
    # USDT = "USDT"
    # AFFILIATE = "AFFILIATE"
    # CURRENCY = (
    #     (BTC, BTC),
    #     (ETH, ETH),
    #     (USDT, USDT),
    #     (AFFILIATE, "AFFILIATE")
    # )
    currency = ForeignKey(Currency, on_delete=CASCADE, related_name=_("addresses"))
    wallet = CharField(max_length=250, blank=True)
    qr = StdImageField(upload_to="qr/", blank=True)
    active = BooleanField(default=True)

    def __str__(self):
        return f"{self.currency.name}"


    class Meta:
        managed = True
        verbose_name = "Wallet Address"
        verbose_name_plural = "Wallet Addresses"
        ordering = ["-modified"]

class Deposit(TimeStampedModel):
    # BTC = "BTC"
    # ETH = "ETH"
    # USDT = "USDT"
    # AFFILIATE = "AFFILIATE"
    # CURRENCY = (
    #     (BTC, BTC),
    #     (ETH, ETH),
    #     (USDT, USDT),
    #     (AFFILIATE, "AFFILIATE")
    # )

    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    STATUS = (
        (PENDING, PENDING),
        (FAILED, FAILED),
        (SUCCESS, SUCCESS),
    )
    user = ForeignKey(User, on_delete=CASCADE, related_name=_("depsit"))
    uuid = CharField(max_length=35, blank=True)
    currency = ForeignKey(Currency, on_delete=CASCADE, related_name=_("deposit"))
    status = CharField(max_length=15, blank=False, choices=STATUS, default=PENDING)
    amount = DecimalField(decimal_places=7, max_digits=20, default=0.00, blank=False)

    def __str__(self):
        return str(self.user.username)


    class Meta:
        managed = True
        verbose_name = "Deposit History"
        verbose_name_plural = "Deposit Histories"
        ordering = ["-created"]

class Withdraw(TimeStampedModel):
    # BTC = "BTC"
    # ETH = "ETH"
    # USDT = "USDT"
    # AFFILIATE = "AFFILIATE"
    # CURRENCY = (
    #     (BTC, BTC),
    #     (ETH, ETH),
    #     (USDT, USDT),
    #     (AFFILIATE, "AFFILIATE")
    # )

    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"
    STATUS = (
        (PENDING, PENDING),
        (FAILED, FAILED),
        (SUCCESS, SUCCESS),
    )
    user = ForeignKey(User, on_delete=CASCADE, related_name=_("withraw"))
    uuid = CharField(max_length=35, blank=True)
    currency = ForeignKey(Currency, on_delete=CASCADE, related_name=_("withdraw"))
    status = CharField(max_length=15, blank=False, choices=STATUS, default=PENDING)
    wallet = CharField(max_length=250, blank=True)
    amount = DecimalField(decimal_places=7, max_digits=20, default=0.00, blank=False)

    def __str__(self):
        return str(self.user.username)


    class Meta:
        managed = True
        verbose_name = "Withdraw History"
        verbose_name_plural = "Withdraw Histories"
        ordering = ["-created"]


































