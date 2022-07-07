from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

# NOTE: This is needed to control language switcher
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from config.sitemaps import StaticViewSitemap
from tranqshare.users.views import deposit, withdraw, suf_bal, get_error, get_currency, d_error, complete

from .views import faq_view, home, register, legals_view, plans_view, privacy_view, switch_language, home_view, about_view, affiliate_view, support_view, complete

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = i18n_patterns(
    path("", home_view, name="home"),
    path("referral/<ref>", home, name="referral"),
    path("about/", about_view, name="about"),
    path("complete/", complete, name="complete"),
    path("register/", register, name="register"),

    path("get_error/", get_error, name="get_error"),
    path("d_error/", d_error, name="d_error"),
    path("get_currency/", get_currency, name="get_currency"),
    path("suf_bal/", suf_bal, name="suf_bal"),

    path("plans/", plans_view, name="plans"),
    path("faq/", faq_view, name="faq"),
    path("legals/", legals_view, name="legals"),
    path("privacy/", privacy_view, name="privacy"),
    path("contact/", support_view, name="support"),
    path("complete/", complete, name="complete"),
    path("affilate-program/", affiliate_view, name="affiliate"),

    # Django Admin, use {% url 'admin:index' %}
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', include('admin_honeypot.urls', 'admin_honeypot')),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),

    # Transaction urls
    path("deposit/", deposit, name="deposit"),
    path("withdraw/", withdraw, name="withdraw"),


    # User management
    path("users/", include("tranqshare.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path("sitemap.xml/", sitemap, kwargs={"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = i18n_patterns(path("__debug__/", include(debug_toolbar.urls))) + urlpatterns

urlpatterns += i18n_patterns(
        path("<str:language>/<str:url>/", view=switch_language, name="language"),
)
