from django.urls import path
from .views import home, post_create



app_name = 'post'
urlpatterns = [
    path('', home, name='home'),
    path('create/', post_create, name='create'),
]
