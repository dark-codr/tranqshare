from django.urls import path

from tranqshare.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    verify_view
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("~verify/", view=verify_view, name="verify"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
