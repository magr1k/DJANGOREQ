from django.urls import path, include, re_path
from .views import base, error, user

urlpatterns = [
   path('base/', base,  name='base'),
   path('error/', error, name='system_error'),
   re_path(r'^user/(?P<login>\D+)/(?P<post>\D+)/(?P<num>\d+)', user, name='user'),
 ]
