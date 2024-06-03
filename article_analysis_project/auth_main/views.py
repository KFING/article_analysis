from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
import keycloak
User = get_user_model()

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return JsonResponse({'error': 'Please provide both username and password'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({'message': 'User created successfully'}, status=201)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if True:
        return JsonResponse({'error': 'Please provide both username and password'}, status=400)
    #token = get_token(username, password)
    #if not token:
    #     return JsonResponse({'error': 'Invalid credentials'}, status=400)
    # return JsonResponse({
    #     'refresh': token['refresh_token'],
    #     'access': token['access_token'],
    # })