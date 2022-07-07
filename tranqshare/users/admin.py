from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from tranqshare.users.forms import UserAdminChangeForm, UserAdminCreationForm

from .models import Wallet, SmartsUpp, Privacy, Currency, Legals, Addresses, FAQ, KYCVerify, TradeOpen, TransactionHistory, Withdraw, Deposit, Testimonials

User = get_user_model()

admin.site.register(Testimonials)
admin.site.register(SmartsUpp)
admin.site.register(Privacy)
admin.site.register(Currency)
admin.site.register(Addresses)
admin.site.register(FAQ)
admin.site.register(KYCVerify)
admin.site.register(TradeOpen)
admin.site.register(TransactionHistory)
admin.site.register(Withdraw)
admin.site.register(Deposit)
admin.site.register(Legals)
admin.site.register(Wallet)

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "name", "last_name", "email", "country", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "first_investment",
                    "has_invested",
                    "has_toped",
                    "can_withdraw",
                    "can_topup",
                    "can_withdraw_roi",
                    "confirm"
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "first_name", "name", "last_name", "ref", "phone", "country", "recommended_by", "first_investment", "has_invested", "has_toped", "can_withdraw", "can_topup", "can_withdraw_roi", "confirm", "is_superuser"]
    list_editable = ["first_name", "name", "last_name", "phone", "country", "first_investment", "has_invested", "has_toped", "can_withdraw", "can_topup", "can_withdraw_roi", "confirm", "is_superuser"]
    search_fields = ["name", "country"]
