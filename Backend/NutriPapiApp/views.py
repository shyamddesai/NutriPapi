from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Fridge, Ingredient, Schedule
from NutriPapiApp.models import Fridge, Ingredient, Schedule
import json
import datetime

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
@login_required
def signup_follow_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user

            if not request.user.is_authenticated:
                return JsonResponse({'error': 'The user is not logged in'}, status=401)
            
            # Initialize user info based on the provided data
            if 'target_weight' in data:
                user.target_weight = float(data['target_weight'])
            if 'current_weight' in data:
                user.current_weight = float(data['current_weight'])
            if 'height' in data:
                user.height = float(data['height'])
            if 'weekly_physical_activity' in data:
                user.weekly_physical_activity = int(data['weekly_physical_activity'])
            if 'gender' in data:
                user.gender = data['gender']
            if 'dietary_restriction' in data:
                user.dietary_restriction = data['dietary_restriction']
            if 'first_name' in data:
                user.first_name = data['first_name']
            user.save()

            # Return a dictionary of user attributes
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'target_weight': user.target_weight,
                'current_weight': user.current_weight,
                'height': user.height,
                'weekly_physical_activity': user.weekly_physical_activity,
                'gender': user.gender,
                'dietary_restriction': user.dietary_restriction,
            }, status=200)
        except Exception as e:
            print(e)
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
    
@require_http_methods(["DELETE"])
@login_required
def delete_account_view(request):
    if request.method == 'DELETE':
        user = request.user

        try:
            data = json.loads(request.body)
            password = data.get('password')
            
            if not authenticate(username=user.username, password=password):
                return JsonResponse({'error': 'The password entered is incorrect. Please retry to proceed with account deletion.'}, status=400)

            Fridge.objects.filter(user=user).delete()
            Schedule.objects.filter(user=user).delete()
            user.delete()
            return JsonResponse({'message': 'Account deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)

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
            print(data)
            user = request.user
            
            # Update user info based on the provided data
            if 'target_weight' in data:
                if float(data['target_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
                user.target_weight = data['target_weight']
            if 'current_weight' in data:
                if float(data['current_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
                user.current_weight = data['current_weight']
            if 'height' in data:
                if float(data['height']) < 0:
                    return JsonResponse({'error': 'Height cannot be negative'}, status=400)
                user.height = data['height']
            if 'weekly_physical_activity' in data:
                if float(data['weekly_physical_activity']) < 0:
                    return JsonResponse({'error': 'Weekly Physical Activity cannot be negative'}, status=400)
                user.weekly_physical_activity = data['weekly_physical_activity']
            if 'gender' in data:
                user.gender = data['gender']
            if 'dietary_restriction' in data:
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
            'dietary_restriction': user.dietary_restriction if user.dietary_restriction else None
        }
        return JsonResponse(user_info, status=200)
    else:
        return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=405)
    
def get_user_info(request):
    user = request.user
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'gender': user.gender,
        'current_weight': user.current_weight,
        'target_weight': user.target_weight,
        'height': user.height,
        'dietary_restriction':user.dietary_restriction,
        'weekly_physical_activity':user.weekly_physical_activity
    })

@csrf_exempt
@login_required
def add_ingredients_to_fridge_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ingredient_names = data.get('ingredients', '').split(',')

            # Strip whitespace and filter out empty strings
            ingredient_names = [name.strip() for name in ingredient_names if name.strip()]

            # Check if the list is empty after stripping whitespace
            if not ingredient_names:
                return JsonResponse({'error': 'No ingredients were added'}, status=400)

            fridge, created = Fridge.objects.get_or_create(user=request.user)
            for ingredient_name in ingredient_names:
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                fridge.ingredients.add(ingredient)
            fridge.save()

            return JsonResponse({'message': 'Ingredients added to fridge successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    
@login_required
def view_fridge_contents_view(request):
    if request.method == 'GET':
        fridge = Fridge.objects.filter(user=request.user).first()
        if fridge:
            ingredients = [ingredient.name for ingredient in fridge.ingredients.all()]
            return JsonResponse({'ingredients': ingredients}, status=200)
        return JsonResponse({'error': 'Fridge is empty'}, status=404)
    
@csrf_exempt
@login_required
def remove_ingredients_from_fridge_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ingredient_names = data.get('ingredients', [])

        fridge = Fridge.objects.filter(user=request.user).first()
        if not fridge:
            return JsonResponse({'error': 'Fridge not found'}, status=404)

        for name in ingredient_names:
            ingredient = Ingredient.objects.filter(name=name).first()
            if ingredient:
                fridge.ingredients.remove(ingredient)

        return JsonResponse({'message': 'Ingredients removed successfully'}, status=200)

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

@csrf_exempt
@login_required
def log_meal_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user
            
           # Extracting meal and exercise details from the request
            breakfast = data.get('breakfast')
            lunch = data.get('lunch')
            dinner = data.get('dinner')

            if not all([breakfast, lunch, dinner]):
                return JsonResponse({'error': 'Meal details are required'}, status=400)

            # We'll just return the meal log data as confirmation for now
            return JsonResponse({
                'message': 'Meal and exercise details logged successfully',
                'details': {
                    'breakfast': breakfast,
                    'lunch': lunch,
                    'dinner': dinner
                }
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
MEAL_TIMES = {
    'breakfast': datetime.time(8, 0),  # Reminder at 7:00 AM for breakfast at 8:00 AM
    'lunch': datetime.time(12, 0),     # Reminder at 11:00 AM for lunch at 12:00 PM
    'dinner': datetime.time(18, 0)     # Reminder at 5:00 PM for dinner at 6:00 PM
}

def get_current_time():
    return datetime.datetime.now()

@csrf_exempt
@login_required
def meal_reminder_view(request):
    if request.method == 'GET':
        user = request.user
        current_time = get_current_time().time()

        # Iterate through meal times to check if it's within one hour of the meal time
        for meal, meal_time in MEAL_TIMES.items():
            meal_datetime = datetime.datetime.combine(datetime.date.today(), meal_time)
            current_datetime = datetime.datetime.combine(datetime.date.today(), current_time)
            time_difference = (meal_datetime - current_datetime).total_seconds()

            print("Current time: ", current_time)
            print("Meal time: ", meal_time)
            print("Time difference: ", time_difference)

            if 0 <= time_difference <= 3600:  # Time difference within an hour
                if Schedule.objects.filter(user=user, meal_type=meal, date_and_time__date=datetime.date.today()).exists():
                    return JsonResponse({'reminder': f"Reminder, get your ingredients ready for {meal}!"}, status=200)
            return JsonResponse({'message': 'No meal suggestions available, so no reminders can be provided.'}, status=204)  # 204 No Content
        else:
            return JsonResponse({'error': 'Only GET requests are allowed'}, status=405) # 405 Method Not Allowed