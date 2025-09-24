from django.urls import path
# from .views import RegisterView, LoginView
from .controller.AuthController import LoginAPIView

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view()  , name='login'),
]