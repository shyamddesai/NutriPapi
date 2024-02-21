from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json

User = get_user_model()

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
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
def logged_in_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(caloriesConsumed=data['caloriesConsumed'])
        if user is not None:
            #TODO not sure which function to call to send post request
            return JsonResponse({'caloriesConsumed': user.caloriesConsumed}, status=200)  # User entered num calories
        else:
            return JsonResponse({'error': 'Invalid input'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
