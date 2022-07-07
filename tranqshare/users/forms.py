from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, ResetPasswordKeyForm, ChangePasswordForm, AddEmailForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from countries_plus.models import Country
from tranqshare.users.models import KYCVerify

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['password'].label = ""
        self.fields['login'].widget = forms.TextInput(
            attrs={'type': 'email', 'class': 'textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-t-md focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-b-md focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})


class VerifyForm(forms.ModelForm):
     class Meta:
         model = KYCVerify
         fields = ['pass_front', 'pass_back']


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label='Country', empty_label="Select Country", widget=forms.Select(attrs={'placeholder': 'Your First Name',
                           "class": "textinput textInput form-control  relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl"}))
    first_name = forms.CharField(max_length=255, label='First Name', widget=forms.TextInput(attrs={'title': 'Your First Name', 'placeholder': 'Your First Name',
                           "class": "textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl"}))
    name = forms.CharField(max_length=255, required=False, label='Middle Name', widget=forms.TextInput(attrs={'title': 'Your Middle Name', 'placeholder': 'Your Middle Name', 'required': "false",
                           "class": "textinput relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'title': 'Your Last Name', 'placeholder': 'Your Last Name',
                           "class": "textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl"}))
    phone = forms.CharField(max_length=14,  widget=forms.TextInput(attrs={'title': 'Your Phone Number', 'placeholder': 'Your Phone Number',
                           "class": "textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={'placeholder': 'Your Email', "hx-post":"/accounts/signup/check-email/", "hx-target":"#email-err", "hx-trigger":"keyup", 'class': 'textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-t-md focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password', 'class': 'textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-b-md focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': 'Your Username', 'class': 'form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl', "hx-post":"/accounts/signup/check-username/", "hx-target":"#username-err", "hx-trigger":"keyup"})
        self.fields['first_name'].widget = forms.TextInput(
            attrs={'placeholder': 'Your First Name', 'class': 'form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['last_name'].widget = forms.TextInput(
            attrs={'placeholder': 'Your Surname', 'class': 'form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})
        self.fields['name'].required = False
        self.fields['phone'].widget = forms.TextInput(
            attrs={'placeholder': 'Phone Number', 'class': 'form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark focus:outline-none focus:ring-variant-2 focus:border-variant-2 focus:z-10 sm:text-xl'})

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']
        user.country = self.cleaned_data['country']
        user.save()
        return user

class ResetUserPassword(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ResetUserPassword, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['email'].widget = forms.EmailInput(
            attrs={'placeholder':'Email Address', 'class': 'textinput textInput form-control fbc-has-badge fbc-UID_1 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-dark rounded-md focus:outline-none focus:ring-primary focus:border-primary focus:z-10 sm:text-xl'})

class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
