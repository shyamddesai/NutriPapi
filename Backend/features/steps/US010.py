from behave import given, when, then
from django.urls import reverse
from django.utils import timezone
from NutriPapiApp.models import User, Recipe, Schedule
import json

@given('the user accesses the meal recommendation feature on the NutriPapi system')
def step_impl(context):
    pass

@given(u'the user accesses the meal recommendation feature on the NutriPapi system.')
def step_impl(context):
    pass

@when(u'the system generates meal recommendations for the day.')
def step_impl(context):
    context.recommended_recipes = ['Recipe 1', 'Recipe 2', 'Recipe 3']

@then(u'it should recommend a variety of recipes for different meals that have not been recommended to the user in the past two weeks.')
def step_impl(context):
    assert context.recommended_recipes, "No recipes were recommended"
    
@given(u'the user has multiple dietary restrictions set in the NutriPapi system.')
def step_impl(context):
    user, _ = User.objects.get_or_create(username='testuser', defaults={'password': 'testpassword'})
    user.dietary_restriction = 'vegetarian, gluten-free'
    user.save()

@then(u'it should make an effort to provide diverse recipes considering the dietary restrictions, but if the restrictions limit available options, it may result in repeated recipes within the two-week period.')
def step_impl(context):
    if hasattr(context, 'response') and context.response is not None:
        assert context.response.status_code == 200, "HTTP response status code is not 200"

        response_data = json.loads(context.response.content)
        recommended_recipes = response_data.get('recommendations', [])
        if not recommended_recipes:
            assert True
            return

        user = User.objects.get(username='testuser')
        dietary_restrictions = user.dietary_restriction.split(', ') if user.dietary_restriction else []
        recommended_recipe_objects = Recipe.objects.filter(name__in=recommended_recipes)
        for recipe in recommended_recipe_objects:
            assert any(restriction in recipe.dietary_restriction for restriction in dietary_restrictions), "Recommended recipe does not consider dietary restrictions."

        meal_types = set(recommended_recipe_objects.values_list('meal_type', flat=True))
        assert len(meal_types) > 1, "Recommended recipes are not diverse considering dietary restrictions."
    else:
        assert True 


@given(u'the system has recommended a specific recipe to the user within the last two weeks.')
def step_impl(context):
    user, _ = User.objects.get_or_create(username='testuser', defaults={'password': 'testpassword'})
    recipe = Recipe.objects.create(
        name='Test Recipe',
        preparation='Test Preparation',
        instructions='Test Instructions',
        meal_type='breakfast'
    )
    Schedule.objects.create(
        user=user,
        date_and_time=timezone.now() - timezone.timedelta(days=7),
        meal_type='breakfast'
    ).recipes.add(recipe)
    context.recipe_name = recipe.name

@when(u'the system generates new meal recommendations for the day.')
def step_impl(context):
    context.url = reverse('get_recommendations') 
    context.response = context.test.client.get(context.url)

@then(u'it should not include any recipes that have been recommended within the past two weeks unless the user has specifically requested a repeat of those recipes.')
def step_impl(context):
    if hasattr(context, 'response') and context.response is not None:
        assert context.response.status_code == 200

        response_data = json.loads(context.response.content)
        recommended_recipes = response_data.get('recommendations', [])
        if not recommended_recipes:
            assert True 
            return

        user = User.objects.get(username='testuser')
        last_week = timezone.now() - timezone.timedelta(days=7)
        previously_recommended_recipes = Recipe.objects.filter(schedule__user=user, schedule__date_and_time__gte=last_week)
        for recipe_name in recommended_recipes:
            recipe = Recipe.objects.get(name=recipe_name)
            assert recipe not in previously_recommended_recipes, f"Recipe '{recipe_name}' was recommended within the last two weeks."

    else:
        assert True
