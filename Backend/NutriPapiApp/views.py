import random
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Fridge, Ingredient, Recipe, Schedule, MealLog
from NutriPapiApp.models import Fridge, Ingredient, Schedule
from NutriPapiApp.encryption_utils import encrypt_data, decrypt_data
from django.utils import timezone
import datetime, json

User = get_user_model()

MEAL_TIMES = {
    'breakfast': datetime.time(8, 0),  # Reminder at 7:00 AM for breakfast at 8:00 AM
    'lunch': datetime.time(12, 0),     # Reminder at 11:00 AM for lunch at 12:00 PM
    'dinner': datetime.time(18, 0)     # Reminder at 5:00 PM for dinner at 6:00 PM
}

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

            # Set the account creation date
            if not user.created_at:
                user.created_at = datetime.timezone.now()

            # Encrypt sensitive fields
            user.encrypted_email = encrypt_data(data['email'])

            user.save()
            
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
            # print(data)
            user = request.user

            if not request.user.is_authenticated:
                return JsonResponse({'error': 'The user is not logged in'}, status=401)
            
            # Initialize user info based on the provided data
            if 'target_weight' in data:
                if float(data['target_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
                user.target_weight = float(data['target_weight'])
            if 'current_weight' in data:
                if float(data['current_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
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
            if 'birthday' in data:
                user.birthday = data['birthday']

            # Set goals based on weight comparison
            if user.current_weight < user.target_weight:
                user.goals = 'gain'
            elif user.current_weight > user.target_weight:
                user.goals = 'lose'
            else:
                user.goals = 'maintain'

            # Encrypt sensitive fields
            user.encrypted_weight = encrypt_data(str(user.current_weight))
            user.encrypted_height = encrypt_data(str(user.height))
            user.encrypted_birthday = encrypt_data(str(user.birthday))

            user.save()

            # Return a dictionary of user attributes
            return JsonResponse({
                'id': user.id,
                'created_at': user.created_at,
                'username': user.username,
                'target_weight': user.target_weight,
                'current_weight': user.current_weight,
                'height': user.height,
                'weekly_physical_activity': user.weekly_physical_activity,
                'gender': user.gender,
                'dietary_restriction': user.dietary_restriction,
                'birthday': user.birthday,
                'goals': user.goals,
            }, status=200)
        except Exception as e:
            # print(e)
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)

            if user.is_locked():
                lockout_duration = (user.lockout_until - timezone.now()).total_seconds()//60
                return JsonResponse({'error': 'Your account is temporarily locked. Please try again in ' + str(int(lockout_duration)) + ' minutes.'}, status=403)

            user_auth = authenticate(username=username, password=password)

            if user_auth is not None:
                user.reset_failed_attempts()
                login(request, user)
                return JsonResponse({'id': user.id, 'username': user.username}, status=200)
            else:
                user.failed_login_attempts += 1
                if user.failed_login_attempts >= 5:
                    user.lock_account()
                    return JsonResponse({'error': 'Too many failed login attempts. Your account has been locked for 5 minutes.'}, status=403)
                else:
                    user.save()
                    return JsonResponse({'error': 'Invalid password. You have ' + str(5 - user.failed_login_attempts) + ' attempts remaining.'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
@csrf_exempt
@login_required
def sign_out_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Successfully logged out'}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_account_view(request):
    if request.method == 'DELETE':
        user = request.user
        try:
            data = json.loads(request.body)
            password = data.get('password')
            # print(data)
            
            if not authenticate(username=user.username, password=password):
                return JsonResponse({'error': 'The password entered is incorrect. Please retry to proceed with account deletion.'}, status=400)

            Fridge.objects.filter(user=user).delete()
            Schedule.objects.filter(user=user).delete()
            logout(request)
            user.delete()
            return JsonResponse({'message': 'Account deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)

@csrf_exempt
@login_required
def user_info_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # print(data)
            user = request.user

            # Decrypt sensitive fields before returning user info
            user.birthday = decrypt_data(user.encrypted_birthday) if user.encrypted_birthday else None
            user.current_weight = decrypt_data(user.encrypted_weight) if user.encrypted_weight else None
            user.height = decrypt_data(user.encrypted_height) if user.encrypted_height else None
            
            # Update user info based on the provided data
            if 'target_weight' in data:
                if float(data['target_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
                user.target_weight = float(data['target_weight'])
            if 'current_weight' in data:
                if float(data['current_weight']) < 0:
                    return JsonResponse({'error': 'Weight cannot be negative'}, status=400)
                user.current_weight = float(data['current_weight'])
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
            if 'birthday' in data:
                user.birthday = data['birthday']    
            if 'first_name' in data:
                user.first_name = data['first_name']

            # Set goals based on weight comparison
            if user.current_weight < user.target_weight:
                user.goals = 'gain'
            elif user.current_weight > user.target_weight:
                user.goals = 'lose'
            else:
                user.goals = 'maintain'

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
        'created_at': user.created_at,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'gender': user.gender,
        'birthday': decrypt_data(user.encrypted_birthday) if user.encrypted_birthday else None,
        'current_weight': decrypt_data(user.encrypted_weight) if user.encrypted_weight else None,
        'target_weight': user.target_weight,
        'height': decrypt_data(user.encrypted_height) if user.encrypted_height else None,
        'dietary_restriction': user.dietary_restriction,
        'goals': user.goals,
        'weekly_physical_activity': user.weekly_physical_activity,
        'password': user.password,
        'failed_login_attempts': user.failed_login_attempts,
        'lockout_until': user.lockout_until
    })

@csrf_exempt
@login_required
def change_password(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # print(data)

            new_password = data.get('new_password')
            if not new_password:
                return JsonResponse({'error': 'New password is required.'}, status=400)

            user = request.user
            # print(user)
            user.set_password(new_password)
            user.save()
            login(request, user)

            return JsonResponse({'success': 'Password changed successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
@login_required
def add_ingredients_to_fridge_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # print(data)
            ingredient_names = data.get('ingredients', [])
            
            # Strip whitespace and filter out empty strings
            ingredient_names = [name.strip() for name in ingredient_names if name.strip()]

            # Check if the list is empty after stripping whitespace
            if not ingredient_names:
                return JsonResponse({'error': 'No ingredients were added'}, status=400)

            fridge, created = Fridge.objects.get_or_create(user=request.user)
            for ingredient_name in ingredient_names:
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                fridge.ingredients.add(ingredient)
                # print(f"Added ingredient '{ingredient_name}' to fridge.")
            fridge.save()
            # print(fridge.ingredients.all())
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
        else:
            return JsonResponse({'error': 'Fridge not found'}, status=404)
    
@csrf_exempt
@login_required
def remove_ingredients_from_fridge_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data)

        fridge = Fridge.objects.filter(user=request.user).first()
        if not fridge:
            return JsonResponse({'error': 'Fridge not found'}, status=404)
        
        if 'ingredient' in data:
            ingredient_names = [data['ingredient']]
        else:
            if 'ingredients' in data and not data['ingredients']:
                fridge.ingredients.clear()
                # print("All ingredients removed from the fridge.")
                # print("Ingredients in Fridge: ", fridge.ingredients.all())
                return JsonResponse({'message': 'All ingredients removed successfully'}, status=200)
            else:
                ingredient_names = data.get('ingredients', [])
                if 'ingredient' in data:
                    ingredient_names = [data['ingredient']]
                # print("Ingredients to remove:", ingredient_names)

        for name in ingredient_names:
            ingredient = Ingredient.objects.filter(name=name).first()
            if ingredient:
                fridge.ingredients.remove(ingredient)
                # print(f"Removed '{name}' from fridge.")  # Log each removed ingredient

        # print("Ingredients in Fridge: ", fridge.ingredients.all())
        return JsonResponse({'message': 'Ingredients removed successfully'}, status=200)

# Daily required calorie calculator: https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873
def calculate_recommended_calories(user, logged_calories=None):
    # print(user.current_weight, user.target_weight, user.height, user.weekly_physical_activity, user.goals, user.birthday)
    # Check if the user's health profile is complete
    if not all([user.current_weight, user.target_weight, user.height, user.weekly_physical_activity, user.goals, user.birthday]):
        return None
    
    # Decrypt encrypted fields
    current_weight = decrypt_data(user.encrypted_weight) if user.encrypted_weight else None
    height = decrypt_data(user.encrypted_height) if user.encrypted_height else None
    birthday = decrypt_data(user.encrypted_birthday) if user.encrypted_birthday else None

    # Convert decrypted fields to appropriate types
    current_weight = float(current_weight) if current_weight else None
    height = float(height) if height else None
    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date() if birthday else None

    # Calculate user's age
    if birthday:
        today = datetime.date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    else:
        age = None

    # Calculate BMR
    if user.gender == 'male':
        bmr = 66.47 + (13.75 * current_weight) + (5.003 * height) - (6.755 * age)
    else: 
        if user.gender == 'female':
            bmr = 655.1 + (9.563 * current_weight) + (1.850 * height) - (4.676 * age)
        else:
            return JsonResponse({'error': 'Gender not stored correctly'}, status=400)
        
    # Adjust BMR based on activity level to get AMR
    activity_multiplier = {
        1: 1.2,  # Sedentary
        2: 1.375,  # Lightly active
        3: 1.55,  # Moderately active
        4: 1.725,  # Active
        5: 1.9  # Very active
    }
    amr = bmr * activity_multiplier.get(user.weekly_physical_activity)
    daily_calorie_requirement = amr

    # Adjust _requirement based on user's goal
    goal_multiplier = {
        'lose': 0.8,  # 20% calorie deficit for weight loss
        'maintain': 1.0,  # No adjustment needed
        'gain': 1.2   # 20% calorie surplus for weight gain
    }

    recommended_calories = amr * goal_multiplier.get(user.goals)

    # Vary the recommended calories based on the user's daily calorie intake logged
    if logged_calories is not None and logged_calories > 0:
        calorie_difference = logged_calories - recommended_calories
        calorie_difference = abs(calorie_difference)

        if calorie_difference >= 100:
            # User is exceeding their calorie goal
            recommended_calories += 0.05 * calorie_difference # Increase recommended calories by 5% of logged calories
        else:
            # User is not meeting their calorie goal
            recommended_calories -= 0.05 * calorie_difference # Decrease recommended calories by 5% of logged calories

    return recommended_calories

@login_required
def caloric_intake_recommendation_view(request):
    if request.method == 'GET':
        user = request.user

        # Retrieve the user's logs for today
        today = datetime.date.today()
        user_logs = MealLog.objects.filter(user=user, date_and_time__date=today)
        
        # Extract the total logged calories for today
        logged_calories = sum([log.calories for log in user_logs])

        recommended_calories = calculate_recommended_calories(user, logged_calories)
        if recommended_calories is None:
            return JsonResponse({'error': 'Please complete your health profile'}, status=400)
        
        return JsonResponse({  
            'logged_calories': logged_calories,
            'recommended_calories': recommended_calories
        }, status=200)
    return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
@login_required
def log_meal_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user

            # Validate meal details
            required_fields = ['breakfast', 'lunch', 'dinner', 'snacks']
            if not all(field in data for field in required_fields):
                return JsonResponse({'error': 'All meal fields are required'}, status=400)
            if any(data[field] < 0 for field in required_fields if field in data):
                return JsonResponse({'error': 'Meal calories cannot be negative'}, status=400)
                        
            # Extracting meal and exercise details from the request
            breakfast = data.get('breakfast', 0)  # Default to 0 if not provided
            lunch = data.get('lunch', 0)
            dinner = data.get('dinner', 0)
            snacks = data.get('snacks', 0)
            
            calories_today = sum([breakfast, lunch, dinner, snacks])
            
            recommended_calories = calculate_recommended_calories(user)

            # Define the lower and upper bounds of recommended calories with leeway
            calories_lower_bound = recommended_calories - 100
            calories_upper_bound = recommended_calories + 100

            # Compare with recommended calories
            calorie_status = ''
            if calories_lower_bound <= calories_today <= calories_upper_bound:
                calorie_status = 'You have met your daily calorie goal.'
            elif calories_today < calories_lower_bound:
                calorie_status = 'You have not met your daily calorie goal. You should consider eating more.'
            else:
                calorie_status = 'You have exceeded your daily calorie goal. You may want to reduce your intake.'

            # Store the current date
            log_date = datetime.date.today().isoformat()

            # Check if a MealLog entry for today already exists for the user
            existing_entry = MealLog.objects.filter(user=user, date_and_time__date=log_date).first()

            if existing_entry:
                # Update the existing entry
                existing_entry.breakfast_calories = breakfast
                existing_entry.lunch_calories = lunch
                existing_entry.dinner_calories = dinner
                existing_entry.snacks_calories = snacks
                existing_entry.calories = calories_today
                existing_entry.date_and_time = log_date
                existing_entry.save()
            else:
                # Create a new MealLog instance and save it to the database
                meal_log = MealLog(
                    user=user,
                    date_and_time=log_date,
                    calories=calories_today,
                    breakfast_calories=breakfast,
                    lunch_calories=lunch,
                    dinner_calories=dinner,
                    snacks_calories=snacks
                )
                meal_log.save()

            return JsonResponse({
                'calorie_status': calorie_status,
                'log_date': log_date,
                'details': {
                    'breakfast': breakfast,
                    'lunch': lunch,
                    'dinner': dinner,
                    'snacks': snacks,
                    'recommended_calories': recommended_calories,
                }
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
@csrf_exempt
@login_required
def view_meal_logs(request):
    if request.method == 'GET':
        user = request.user
        today = datetime.date.today()
        meal_logs = MealLog.objects.filter(user=user, date_and_time__date=today)
        logs_data = [{
            'id': log.id,
            'date_and_time': log.date_and_time,
            'calories': log.calories,
            'breakfast': log.breakfast_calories,
            'lunch': log.lunch_calories,
            'dinner': log.dinner_calories,
            'snacks': log.snacks_calories
        } for log in meal_logs]
        return JsonResponse({'meal_logs': logs_data}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
@login_required
def delete_meal_logs_for_today(request):
    if request.method == 'GET': # This method is intended to delete all logs (as an admin from the browser) for testing purposes
        user = request.user
        today = datetime.date.today()
        deleted_count, _ = MealLog.objects.filter(user=user, date_and_time__date=today).delete()
        return JsonResponse({'message': f'{deleted_count} meal logs deleted for today'}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

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

            # print("Current time: ", current_time)
            # print("Meal time: ", meal_time)
            # print("Time difference: ", time_difference)

            if 0 <= time_difference <= 3600:  # Time difference within an hour
                if Schedule.objects.filter(user=user, meal_type=meal, date_and_time__date=datetime.date.today()).exists():
                    return JsonResponse({'reminder': f"Reminder, get your ingredients ready for {meal}!"}, status=200)
            return JsonResponse({'message': 'No meal suggestions available, so no reminders can be provided.'}, status=204)  # 204 No Content
        else:
            return JsonResponse({'error': 'Only GET requests are allowed'}, status=405) # 405 Method Not Allowed

@csrf_exempt
@login_required
def search_view(request):
    if request.method == 'GET':
        keyword=request.GET.get('keyword')
        if keyword == '':
            return JsonResponse({'results': []})
        results = Ingredient.objects.filter(name__icontains=keyword)
        results_data = [{'name': result.name, 'nutritional_information': result.nutritional_information, 'calories': result.calories} for result in results]
        return JsonResponse({'results': results_data})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405) # 405 Method Not Allowed
    
@csrf_exempt
@login_required
def import_recipes_and_ingredients(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
    # We don't have staff users, so just comment the following line when adding recipes...
    # if not request.user.is_staff:
    #     return JsonResponse({'error': 'Unauthorized access'}, status=403)

    try:
        # Access the raw string from 'data' key
        raw_data = json.loads(request.body.decode('utf-8')).get('data')
        
        # Now load this raw string as JSON to get the actual list
        recipes_data = json.loads(raw_data)
        # print(recipes_data)

        existing_items_info = []  # To keep track of existing items
        new_items_info = []  # To keep track of new items

        for recipe_data in recipes_data:
            # Check if a recipe with the same name already exists
            if Recipe.objects.filter(name=recipe_data['name']).exists():
                existing_items_info.append(f"Skipped existing recipe: {recipe_data['name']}")
                continue

            nutritional_info = "Fat: {}g, Protein: {}g, Sodium: {}mg".format(
                recipe_data.get('fat', 0),
                recipe_data.get('protein', 0),
                recipe_data.get('sodium', 0)
            )

            recipe, recipe_created = Recipe.objects.get_or_create(
                name=recipe_data['name'],
                defaults={
                    'preparation': "\n".join(recipe_data.get('preparation', [])),
                    'instructions': "\n".join(recipe_data.get('instructions', [])),
                    'meal_type': recipe_data.get('meal_type', 'General'),
                    'calories': recipe_data.get('calories', 0),
                    'nutritional_information': nutritional_info,
                }
            )

            if recipe_created:
                new_items_info.append(f"New recipe added: {recipe.name}")
            else:
                existing_items_info.append(f"Existing recipe used: {recipe.name}")

            # Process ingredients
            for ingredient_name in recipe_data.get('ingredients', []):
                ingredient, ingredient_created = Ingredient.objects.get_or_create(name=ingredient_name)
                recipe.ingredients.add(ingredient)
                
                if ingredient_created:
                    new_items_info.append(f"New ingredient added: {ingredient.name}")
                else:
                    existing_items_info.append(f"Existing ingredient used: {ingredient.name}")

            messages = {
            'existing_items': existing_items_info,
            'new_items': new_items_info,
            'message': 'All recipes and ingredients imported successfully.'
        }

        return JsonResponse(messages, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'Missing key in data: {str(e)}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
@login_required
def list_recipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipes_data = [{
            'id': recipe.id,
            'name': recipe.name,
            'preparation': recipe.preparation,
            'meal_type': recipe.meal_type,
            'instructions': recipe.instructions,
            'calories': recipe.calories,
            'nutritional_information': recipe.nutritional_information,
            'ingredients': list(recipe.ingredients.values_list('name', flat=True))
        } for recipe in recipes]
        return JsonResponse({'recipes': recipes_data}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
@login_required
def list_ingredients(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        ingredients_data = [{
            'id': ingredient.id,
            'name': ingredient.name,
            'recipes': list(ingredient.recipes.values_list('name', flat=True))
        } for ingredient in ingredients]
        return JsonResponse({'ingredients': ingredients_data}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    
@csrf_exempt
@login_required
def delete_recipes_and_ingredients(request):
    if request.method == 'GET': # This method is intended to delete all recipes and ingredients (as an admin from the browser) for testing purposes
        deleted_count, _ = Recipe.objects.all().delete()
        deleted_count_ingredients, _ = Ingredient.objects.all().delete()
        return JsonResponse({'message': f'{deleted_count} deleted recipes, and {deleted_count_ingredients} deleted ingredients'}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
