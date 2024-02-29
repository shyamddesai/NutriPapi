from django.urls import path
from .views import signup_view, signin_view, logged_in_view, user_info_view, add_ingredients_to_fridge_view, \
    signup_follow_view, update_user_info_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup_follow/', signup_follow_view, name='signup_follow'),
    path('signin/', signin_view, name='signin'),
    path('loggedin/', logged_in_view, name='loggedin'), 
    path('user/info/', user_info_view, name='user_info'),
    path('fridge/add_ingredients/', add_ingredients_to_fridge_view, name='add_ingredients_to_fridge'),
    path('user/update_info/', update_user_info_view, name='update_user_info'),
]
