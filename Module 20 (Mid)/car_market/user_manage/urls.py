from django.urls import path
from user_manage import views


urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit-profile"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
