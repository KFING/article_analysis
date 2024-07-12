from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_page, name='main_page'), # основная страница
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='login_page'),# страница c кнопкой для инцилизации логина
    path('keycloak_login/', views.keycloak_login, name='keycloak_login'),# view которое делает редирект на страницу входа Keycloak
    path('keycloak_registration/', views.keycloak_login, name='keycloak_login'),
    path('keycloak_callback/', views.keycloak_callback, name='keycloak_callback'), # view обрабатывает ответ Keycloak, валидирует токен авторизует пользователя
    path('home_page/', views.home_page, name='home_page'),  # home страница

]