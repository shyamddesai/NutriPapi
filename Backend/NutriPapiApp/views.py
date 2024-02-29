from sqlite3 import IntegrityError
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Fridge, Ingredient

User = get_user_model()

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Request data:", data)

            if User.objects.filter(username=data['username']).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)

            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
            return JsonResponse({
                'message': 'User created successfully',
                # 'user': user, 'id': user.id, 'username': user.username}, status=201)  # User created
                'user': user_data}, status=201) # User created
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def signup_follow_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user
            return JsonResponse({'id': user.id, 'username': user.username}, status=201)  # User created
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
            if 'DiertaryRestriction ' in data:
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

@csrf_exempt
@login_required
def update_user_info_view(request):
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
            if 'dietary_restriction' in data:
                user.dietary_restriction = data['dietary_restriction']
            
            user.save()
            return JsonResponse({'message': 'User info updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)