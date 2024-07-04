from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authMy.backends import KeycloakConfidentialBackend

def login_page(request):
    return render(request, 'main/login_page.html')


def keycloak_login(request):


    redirect_url = f"{settings.KEYCLOAK_URL_BASE}realms/{settings.REALM_NAME}/protocol/openid-connect/auth" \
                  f"?client_id={settings.CLIENT_ID}&response_type=code"

    return redirect(redirect_url)

@login_required(redirect_field_name='next', login_url='/login')
def main_page(request):
    pass


def keycloak_callback(request):
    # Получаю токен и информацию о пользователе из запроса
    try:
        code = request.GET['code']
    except Exception:
        return redirect('/login')  # Замените на свой шаблон ошибки

    backend = KeycloakConfidentialBackend()
    data_token = backend.exchange_code_for_token(code)
    if not data_token:
        return redirect('/login')
    # Аутентифицируйте пользователя в Django
    user = backend.authenticate(request, token=data_token)
    if user is not None:
        login(request, user)
        # Пользователь успешно аутентифицирован, теперь вы можете перенаправить его на другую страницу
        return redirect('/home_page')  # Замените на путь, куда вы хотите перенаправить пользователя
    else:
        # Обработка случая, если аутентификация не удалась
        return redirect('/login')  # Замените на свой шаблон ошибки

def home_page(request):
    return render(request, 'main/home_page.html')