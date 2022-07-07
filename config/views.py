from django.utils import translation
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.templatetags.static import static
from tranqshare.utils.emails import support_email
from countries_plus.models import Country

from django.template.loader import get_template
from django.utils.safestring import mark_safe

from tranqshare.utils.logger import LOGGER

from tranqshare.users.models import FAQ, Legals, Privacy

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def home_view(request):
    title = "Online Trading, Investment and Asset Management"
    can_link = reverse("home")
    template = "pages/home.html"
    htmx_template = "htmx/pages/home.html"
    context = {
        'title': title,
        'can_link': can_link,
        'home': True
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)


@require_http_methods(['GET'])
def home(request, *args, **kwargs):
    ref = str(kwargs.get('ref'))
    LOGGER.info(ref)
    try:
        user = User.objects.get(ref=ref)
        request.session['ref_profile'] = user.id
        LOGGER.info(f"ID: {user.id} for {user.name.title()}")
    except:
        LOGGER.info("No User ID")

    if request.htmx:
        return render(request, "htmx/pages/home.html")
    return render(request, "pages/home.html")

@require_http_methods(['GET'])
def about_view(request):
    title = "About Us"
    can_link = reverse("about")
    template = "pages/about.html"
    htmx_template = "htmx/pages/about.html"
    context = {
        'title': title,
        'can_link': can_link,
        'about': True
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)

@require_http_methods(['GET'])
def affiliate_view(request):
    title = "Affiliate Program"
    can_link = reverse("affiliate")
    template = "pages/affiliate.html"
    htmx_template = "htmx/pages/affiliate.html"
    context = {
        'title': title,
        'can_link': can_link,
        'affiliate': True
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)


@require_http_methods(['GET'])
def faq_view(request):
    title = "FAQ"
    can_link = reverse("faq")
    faqs = FAQ.objects.all()
    template = "pages/faqs.html"
    htmx_template = "htmx/pages/faqs.html"
    context = {
        'title': title,
        'can_link': can_link,
        'faqs': faqs,
        'faq': True
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)

@require_http_methods(['GET'])
def privacy_view(request):
    title = "Privacy"
    can_link = reverse("privacy")
    template = "pages/privacy.html"
    htmx_template = "htmx/pages/privacy.html"
    object = Privacy.objects.first()
    context = {
        'title': title,
        'can_link': can_link,
        'faq': True,
        "object": object
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)


@require_http_methods(['GET'])
def legals_view(request):
    title = "Legal"
    can_link = reverse("legals")
    template = "pages/legals.html"
    htmx_template = "htmx/pages/legals.html"
    object = Legals.objects.first()
    context = {
        'title': title,
        'can_link': can_link,
        'affiliate': True,
        "object": object
    }
    if request.htmx:
        return render(request, htmx_template, context)
    return render(request, template, context)

@require_http_methods(['GET'])
def plans_view(request):
    template = "pages/plans.html"
    htmx_template = "htmx/pages/plans.html"
    # object = Legals.objects.first()
    # context = {
    #     "object": object
    # }
    if request.htmx:
        return render(request, htmx_template)#, context)
    return render(request, template)#, context)


@require_http_methods(['GET', 'POST'])
def support_view(request):
    title = "Contact Us"
    can_link = reverse("support")
    template = "pages/support.html"
    htmx_template = "htmx/pages/support.html"
    context = {
        'title': title,
        'can_link': can_link,
        'affiliate': True
    }
    if request.htmx:
        if request.POST and request.htmx:
            image = static("vendors/images/logo.png")
            message = request.POST.get('message')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            name = request.POST.get('name')
            message = get_template('mail/simple_mail.html').render(context={"subject": f"New Mail From {name.title()} - {subject.title()}", "body": mark_safe(message), "image":image})
            support_email(to_email="support@pamlicotrade.org", from_email=str(email), subject=str(subject), body=message)
            return redirect(reverse("complete"))
        return render(request, htmx_template, context)
    return render(request, template, context)

@require_http_methods(['GET'])
def complete(request):
    if request.htmx:
        title = "Complete"
        complete = "snippets/complete.html"
        context = {
            'title': title,
        }
        return render(request, complete, context)

@require_http_methods(['GET', 'POST'])
def register(request):
    username = request.POST.get('username')
    first = request.POST.get('first_name')
    middle = request.POST.get('middle_name')
    last = request.POST.get('last_name')
    country = request.POST.get('country')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    if request.htmx and request.POST:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first
        user.last_name = last
        user.name = middle
        user.phone = phone
        user.country = Country.objects.get(iso=country.upper())
        user.save()
    return render(request, "snippets/complete.html")

@require_http_methods(['GET'])
def switch_language(request, **kwargs):
    language = kwargs.get('language')
    redirect_url_name = request.GET.get('url') # e.g. '/about/'

    # make sure language is available
    valid = False
    for l in settings.LANGUAGES:
        if l[0] == language:
            valid = True
    if not valid:
        raise Http404(_('The selected language is unavailable!'))

    # Make language the setting for the session
    translation.activate(language)
    # response = redirect(reverse(redirect_url_name)) # Changing this to use reverse works

    # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    # return response
    return redirect(reverse(language, kwargs={'url':redirect_url_name})) # Changing this to use reverse works



