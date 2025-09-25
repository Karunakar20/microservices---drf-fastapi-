from django.urls import path
from user.views.users_c_u_views import UsersViewCreatorUpdate,UsersViewGet
from user.views.user_login_logout import UserViewLogin,UserViewLogout

urlpatterns = [
    path("users/", UsersViewCreatorUpdate.as_view()),
    path("users/get/", UsersViewGet.as_view()),
    path("users/login/", UserViewLogin.as_view()),
    path("users/logout/", UserViewLogout.as_view()),
]