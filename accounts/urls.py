from .views import RegistrationAPI, UserAPI
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path


urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')
]