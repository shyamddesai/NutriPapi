from django.urls import path
from .views import view_meal_logs,get_recommendations, list_ingredients, list_recipes, import_recipes_and_ingredients, delete_meal_logs_for_today, caloric_intake_recommendation_view, sign_out_view, change_password, delete_account_view, meal_reminder_view, log_meal_view, get_user_info, remove_ingredients_from_fridge_view, signup_view, signup_follow_view, signin_view, user_info_view, add_ingredients_to_fridge_view, view_fridge_contents_view, search_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup_follow/', signup_follow_view, name='signup_follow'),
    path('signin/', signin_view, name='signin'),
    path('signout/', sign_out_view, name='signout'),
    path('user/get_info/', get_user_info, name='get_user_info'),
    path('user/update_info/', user_info_view, name='user_info'),
    path('user/change_password/', change_password, name='change_password'),
    path('user/delete/', delete_account_view, name='delete_account'),
    path('fridge/view_ingredients/', view_fridge_contents_view, name='view_fridge_contents'),
    path('fridge/add_ingredient/', add_ingredients_to_fridge_view, name='add_ingredients_to_fridge'),
    path('fridge/remove_ingredient/', remove_ingredients_from_fridge_view, name='remove_ingredients_from_fridge'),
    path('calorie_recommendation/', caloric_intake_recommendation_view, name='caloric_intake_recommendation'),
    path('meals/log/', log_meal_view, name='log_meal'),
    path('meals/view_log/', view_meal_logs, name='view_meal_logs'),
    path('meals/logs/delete/', delete_meal_logs_for_today, name='delete_meal_logs_for_today'),
    path('recipe/add/', import_recipes_and_ingredients, name='add_recipe'),
    path('recipe/view', list_recipes, name='view_recipes'),
    path('recipe/ingredients/view', list_ingredients, name='view_ingredients'),
    path('reminder/', meal_reminder_view, name='meal_reminder'),
    path('search/', search_view, name='search'),
    path('get-recommendations/', get_recommendations, name='get_recommendations')
]
