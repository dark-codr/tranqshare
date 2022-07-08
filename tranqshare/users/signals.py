import datetime

from decimal import Decimal
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.template.loader import get_template, render_to_string
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.templatetags.static import static

from django.dispatch import receiver

from allauth.account.signals import user_signed_up

from tranqshare.utils.logger import LOGGER
from tranqshare.utils.emails import plain_email


logo = static("vendors/images/logo.png")

from .models import Currency, Deposit, Withdraw, TransactionHistory, Wallet

User = get_user_model()

@receiver(post_save, sender=User)
def user_post_save_signal(created, instance, *args, **kwargs):
    if created:
        Wallet.objects.get_or_create(user=instance)
        # instance.ref = instance.email.split("@")[0]+str(instance.date_joined.year)
        LOGGER.info("Sent Registration Email to admin")

@receiver(pre_save, sender=User)
def user_pre_save_signal(instance, *args, **kwargs):
    if instance.ref == None or instance.ref == "":
        instance.ref = instance.email.split("@")[0][:5]+str(instance.date_joined.year)
        LOGGER.info("Referral Number Generated")


@receiver(post_save, sender=Withdraw)
def withdraw_approve_signal(created, instance, *args, **kwargs):
    if instance.status == Withdraw.FAILED:
        TransactionHistory.objects.filter(uuid=instance.uuid).update(
            status= TransactionHistory.FAILED,
        )
    elif instance.status == Withdraw.SUCCESS:
        TransactionHistory.objects.filter(uuid=instance.uuid).update(
            status= TransactionHistory.SUCCESS,
        )
        if instance.currency == Currency.objects.get(name="BTC"):
            amount = instance.user.wallet.btc - instance.amount
            Wallet.objects.filter(user=instance.user).update(btc = amount)
        elif instance.currency == Currency.objects.get(name="ETH"):
            amount = instance.user.wallet.eth - instance.amount
            Wallet.objects.filter(user=instance.user).update(eth = amount)
        elif instance.currency == Currency.objects.get(name="USDT"):
            amount = instance.user.wallet.usdt - instance.amount
            Wallet.objects.filter(user=instance.user).update(usdt = amount)
        # elif instance.currency.name == "DASH":
        #     amount = instance.user.wallet.dash - instance.amount
        #     Wallet.objects.filter(user=instance.user).update(dash = amount)

        body = f"""
        Hello Webmaster,
        <br>
        <br>
        You have confirmed a withdrawal request
        <br>
        User: {instance.user.username.title()} - {instance.user.email}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """
        body2 = f"""
        Hello {instance.user.username.title()},
        <br>
        <br>
        You withdrawal request has been confirmed
        <br>
        Date: {datetime.date.today()}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """

        admin_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Withdrawal Confirmed", "body": mark_safe(body)})
        user_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Withdrawal Confirmed", "body": mark_safe(body2)})
        plain_email(to_email=instance.user.email, subject="Withdrawal Confirmed", body=user_message)
        plain_email(to_email="admin@tranqshare.com", subject="Withdrawal Confirmed", body=admin_message)

@receiver(post_save, sender=Deposit)
def deposit_approve_signal(created, instance, *args, **kwargs):
    LOGGER.info("Deposit Getting Approved")
    User.objects.filter(username=instance.user.username, can_withdraw=True).update(can_withdraw=False)
    if instance.status == Deposit.FAILED:
        LOGGER.error("Deposit Failing")
        User.objects.filter(username=instance.user.username, first_investment=True).update(has_invested = False, can_withdraw=False, first_investment=False)
        TransactionHistory.objects.filter(uuid=instance.uuid).update(
            status= TransactionHistory.FAILED,
        )
        if instance.currency == Currency.objects.get(name="BTC") and not instance.user.wallet.btc > 0:
            amount = instance.user.wallet.btc - instance.amount
            Wallet.objects.filter(user=instance.user).update(btc = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="ETH") and not instance.user.wallet.eth > 0:
            amount = instance.user.wallet.eth - instance.amount
            Wallet.objects.filter(user=instance.user).update(eth = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="USDT") and not instance.user.wallet.usdt > 0:
            amount = instance.user.wallet.usdt - instance.amount
            Wallet.objects.filter(user=instance.user).update(usdt = amount, invested_date=instance.created)
        body = f"""
        Hello Webmaster,
        <br>
        <br>
        You have unconfirmed a Deposit request
        <br>
        User: {instance.user.username.title()} - {instance.user.email}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """
        body2 = f"""
        Hello {instance.user.username.title()},
        <br>
        <br>
        Your Deposit request has been denied
        <br>
        Date: {datetime.date.today()}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """

        admin_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body)})
        user_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body2)})
        plain_email(to_email=instance.user.email, subject="Deposit Failed", body=user_message)
        plain_email(to_email="admin@tranqshare.com", subject="Deposit Failed", body=admin_message)

    elif instance.status == Deposit.SUCCESS and not instance.user.first_investment:
        LOGGER.error("Deposit Succeeding")
        User.objects.filter(username=instance.user.username).update(has_invested = True, can_withdraw=False, first_investment=False)
        TransactionHistory.objects.filter(uuid=instance.uuid).update(
            status= TransactionHistory.SUCCESS,
        )

        if instance.currency == Currency.objects.get(name="BTC"):
            amount = instance.user.wallet.btc + instance.amount
            Wallet.objects.filter(user=instance.user).update(btc = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="ETH"):
            amount = instance.user.wallet.eth + instance.amount
            Wallet.objects.filter(user=instance.user).update(eth = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="USDT"):
            amount = instance.user.wallet.usdt + instance.amount
            Wallet.objects.filter(user=instance.user).update(usdt = amount, invested_date=instance.created)

        body = f"""
        Hello Webmaster,
        <br>
        <br>
        You have confirmed a Deposit request
        <br>
        User: {instance.user.username.title()} - {instance.user.email}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """
        body2 = f"""
        Hello {instance.user.username.title()},
        <br>
        <br>
        You Deposit request has been confirmed
        <br>
        Date: {datetime.date.today()}
        <br>
        Amount: {instance.amount}
        <br>
        <br>
        """

        admin_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body)})
        user_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body2)})
        plain_email(to_email=instance.user.email, subject="Deposit Confirmed", body=user_message)
        plain_email(to_email="admin@tranqshare.com", subject="Deposit Confirmed", body=admin_message)

    elif instance.status == Deposit.SUCCESS and instance.user.first_investment:
        LOGGER.error("First Investment Deposit Succeeding")
        User.objects.filter(username=instance.user.username).update(has_invested=True, can_withdraw=False, first_investment=False)

        TransactionHistory.objects.filter(uuid=instance.uuid).update(
            status= TransactionHistory.SUCCESS,
        )

        if instance.currency == Currency.objects.get(name="BTC"):
            amount = instance.user.wallet.btc + instance.amount
            Wallet.objects.filter(user=instance.user).update(btc = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="ETH"):
            amount = instance.user.wallet.eth + instance.amount
            Wallet.objects.filter(user=instance.user).update(eth = amount, invested_date=instance.created)
        elif instance.currency == Currency.objects.get(name="USDT"):
            amount = instance.user.wallet.usdt + instance.amount
            Wallet.objects.filter(user=instance.user).update(usdt = amount, invested_date=instance.created)

        two_percent = instance.amount * Decimal(0.1)
        referrer = User.objects.filter(username=instance.user.recommended_by).exists()
        LOGGER.info(referrer)
        if referrer:
            user = User.objects.get(username=instance.user.recommended_by)
            if user.bonus < 1.00:
                profit = Decimal(0.00) + two_percent
            else:
                profit = user.bonus + two_percent
            User.objects.filter(username=instance.user.recommended_by).update(bonus=profit)
            TransactionHistory.objects.objects.get(uuid=instance.uuid).update(
                status= TransactionHistory.SUCCESS,
            )
            body = f"""
            Hello {referrer},
            <br>
            <br>
            You have just been awarded a bonus of {profit} by referring:
            <br>
            User: {instance.user.username.title()} - {instance.user.email}
            <br>
            Deposit Amount: {instance.amount}
            <br>
            <br>
            """
            admin_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body)})
            plain_email(to_email=instance.user.email, subject="Referral Bonus", body=user_message)


            body2 = f"""
            Hello {instance.user.username.title()},
            <br>
            <br>
            Your referrer master {referrer} has just been awarded a bonus of {profit}
            <br>
            Date: {datetime.date.today()}
            <br>
            Deposited Amount: {instance.amount}
            <br>
            <br>
            """

            user_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Deposit Confirmed", "body": mark_safe(body2)})
            plain_email(to_email=referrer.email, subject="Referral Bonus", body=admin_message)



@receiver(user_signed_up)
def referral_signals(request, user, **kwargs):
    LOGGER.info("Creating Referral")
    referrer_id = request.session.get("ref_profile")

    admin_body = f"""
    Hello Webmaster,
    <br>
    <br>
    {user.username.title()} Has just successfully signed up.
    <br>
    <br>
    """

    admin_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "New Referral", "body": mark_safe(admin_body)})
    plain_email(to_email="admin@tranqshare.com", subject="New Referral", body=admin_message)

    LOGGER.info("Sent new registration email to admin")

    if referrer_id is not None:
        recommended_by_user = User.objects.get(id=referrer_id)
        recommender_email = recommended_by_user.email
        new_user = user
        new_user.recommended_by = recommended_by_user
        new_user.save()

        body = f"""
        Hello {recommended_by_user.username.title()},
        <br>
        <br>
        Your referral code: {recommended_by_user.ref.upper()} was used to refer
        <br>
        <br>
        <strong>NEW USER: {new_user.username.title()}</strong>
        <br>
        <br>
        Be informed that upon their initial investment capital, you will earn <strong>2%</strong> from that investment, which shall be added to your referral bonus.
        <br>
        <br>
        """

        body2 = f"""
        Hello {new_user.username.title()},
        <br>
        <br>
        Your have successfully signed up with the referral code: {recommended_by_user.ref.upper()}
        <br>
        <br>
        Be informed that upon your initial investment capital, your referrer will earn <strong>2%</strong> from your investment.
        <br>
        <br>
        """

        referrer_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "New Referral", "body": mark_safe(body)})
        user_message = get_template('mail/simple_mail.html').render(context={"image":logo, "subject": "Successfully Referrer Registration", "body": mark_safe(body2)})
        plain_email(to_email=user.email, subject="Successfully Referrer Registration", body=user_message)
        plain_email(to_email=recommender_email, subject="New Referral", body=referrer_message)
        LOGGER.info(f"Sent new referrer registration email to {recommended_by_user.username.title()}")


