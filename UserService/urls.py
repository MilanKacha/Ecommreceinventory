from django.urls import path
# from .views import RegisterView, LoginView
from .controller.AuthController import LoginAPIView, SignUpView

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view()  , name='login'),
    path('signup/', SignUpView.as_view()  , name='signup'),
]