from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name='home_page'), # основная страница
    path('login/', views.login_page, name='login_page'), # страница c кнопкой для инцилизации логина
    path('keycloak_login/', views.keycloak_login, name='keycloak_login'), # view которое делает редирект на страницу входа Keycloak
    path('keycloak_callback/', views.keycloak_callback, name='keycloak_callback'), # view обрабатывает ответ Keycloak, валидирует токен авторизует пользователя
]