from sqlite3 import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Fridge, Ingredient

from NutriPapiApp.models import Fridge, Ingredient

User = get_user_model()

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Check for mandatory fields and if they are not empty
            required_fields = ['username', 'email', 'password']
            if not all(field in data and data[field] for field in required_fields):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # Check for existing email or username
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'error': 'Email already in use'}, status=400)
            if User.objects.filter(username=data['username']).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            # Create user and log them in
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            login(request, user)
            return JsonResponse({'id': user.id, 'username': user.username}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



@csrf_exempt
def signup_follow_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user

            # Initialize user info based on the provided data
            if 'target_weight' in data:
                user.target_weight = data['target_weight']
            if 'current_weight' in data:
                user.current_weight = data['current_weight']
            if 'height' in data:
                user.height = data['height']
            if 'weekly_physical_activity' in data:
                user.weekly_physical_activity = data['weekly_physical_activity']
            if 'gender' in data:
                user.gender = data['gender']
            if 'Dietary_restriction' in data:
                user.dietary_restriction = data['dietary_restriction']
            user.save()
            return JsonResponse({'user': user, 'id': user.id, 'username': user.username}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({'id': user.id, 'username': user.username}, status=200)  # User logged in
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
@login_required
def logged_in_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            calories_consumed = data.get('caloriesConsumed')
            return JsonResponse({'caloriesConsumed': calories_consumed}, status=200)
        except KeyError:
            return JsonResponse({'error': 'Missing caloriesConsumed in request'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
@login_required
def user_info_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user
            
            # Update user info based on the provided data
            if 'target_weight' in data:
                user.target_weight = data['target_weight']
            if 'current_weight' in data:
                user.current_weight = data['current_weight']
            if 'height' in data:
                user.height = data['height']
            if 'weekly_physical_activity' in data:
                user.weekly_physical_activity = data['weekly_physical_activity']
            if 'gender' in data:
                user.gender = data['gender']
            if 'DietaryRestriction ' in data:
                user.dietary_restriction = data['dietary_restriction']
            
            user.save()
            return JsonResponse({'message': 'User info updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == 'GET':
        user = request.user
        user_info = {
            'target_weight': user.target_weight,
            'current_weight': user.current_weight,
            'height': user.height,
            'weekly_physical_activity': user.weekly_physical_activity,
            'gender': user.gender,
            'dietary_restriction': user.dietary_restriction.id if user.dietary_restriction else None
        }
        return JsonResponse(user_info, status=200)
    else:
        return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=405)
    
@csrf_exempt
@login_required
def add_ingredients_to_fridge_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ingredient_names = data.get('ingredients', '').split(',')

            fridge, created = Fridge.objects.get_or_create(user=request.user)
            for ingredient_name in ingredient_names:
                ingredient_name = ingredient_name.strip()  # Remove any leading/trailing whitespace
                if ingredient_name:  # Check if the ingredient name is not empty
                    ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                    fridge.ingredients.add(ingredient)
            fridge.save()

            return JsonResponse({'message': 'Ingredients added to fridge successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
def get_user_info(request):
    user = request.user
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'target_weight': user.target_weight,
        'dietary_restriction':user.dietary_restriction,
        'weekly_physical_activity':user.weekly_physical_activity
    })


@login_required
def caloric_intake_recommendation_view(request):
    if request.method == 'GET':
        user = request.user

        # Check if the user's health profile is complete
        if not all([user.current_weight, user.target_weight, user.height, user.weekly_physical_activity]):
            return JsonResponse({'error': 'Please complete your health profile'}, status=400)
        # This is a placeholder formula 
        recommended_calories = (10 * user.current_weight + 6.25 * user.height - 5 ) * user.weekly_physical_activity

        return JsonResponse({'recommended_calories': recommended_calories}, status=200)

    return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

