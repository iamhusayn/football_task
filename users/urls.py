from django.urls import path, include
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login')
    # path('users/token/', UserRegistrationView.as_view(), name='token_obtain')
]

