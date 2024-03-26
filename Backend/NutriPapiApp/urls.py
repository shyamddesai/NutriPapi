from django.urls import path
from .views import caloric_intake_recommendation_view, delete_account_view, meal_reminder_view, log_meal_view, get_user_info, remove_ingredients_from_fridge_view, signup_view, signup_follow_view, signin_view, logged_in_view, user_info_view, add_ingredients_to_fridge_view, view_fridge_contents_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup_follow/', signup_follow_view, name='signup_follow'),
    path('signin/', signin_view, name='signin'),
    path('loggedin/', logged_in_view, name='loggedin'), 
    path('user/info/', user_info_view, name='user_info'),
    path('fridge/add_ingredients/', add_ingredients_to_fridge_view, name='add_ingredients_to_fridge'),
    path('user/get_info/', get_user_info, name='get_user_info'),
    path('caloric_recommendation/', caloric_intake_recommendation_view, name='caloric_intake_recommendation'),
    path('fridge/view_contents/', view_fridge_contents_view, name='view_fridge_contents'),
    path('fridge/remove_ingredients/', remove_ingredients_from_fridge_view, name='remove_ingredients_from_fridge'),
    path('log_meal/', log_meal_view, name='log_meal'),
    path('reminder/', meal_reminder_view, name='meal_reminder'),
    path('delete/', delete_account_view, name='delete_account'),
]
