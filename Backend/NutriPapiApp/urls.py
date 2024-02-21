from django.urls import path
from .views import signup_view, signin_view, logged_in_view, user_info_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('loggedin/', logged_in_view, name='loggedin'), 
    path('user/info/', user_info_view, name='user_info')
]
