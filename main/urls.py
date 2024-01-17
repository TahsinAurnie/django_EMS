from django.urls import path
from .views import *

urlpatterns = [
    # admin
    path('', admin_dashboard, name='admin_home')
]
