from django.urls import path
from .views import user_login, user_registration
from django.contrib.auth.views import LogoutView




app_name = 'accounts'
urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
