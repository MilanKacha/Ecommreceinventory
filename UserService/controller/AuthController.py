from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from UserService.serializers import LoginSerializer
from Ecommerceinventory.Helpers import renderResponse

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return renderResponse(
                data=serializer.errors,  # Pass errors here
                message="Validation failed",
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.validated_data['user']

        # Create JWT token
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'profile_pic': user.profile_pic,
                'role': user.role
            }
        }

        return renderResponse(
            data=data,
            message="Login successful",
            status=status.HTTP_200_OK
        )


class PublicAPIView(APIView):
    def get(self, request):
        return renderResponse(data='This is a publicly accessible API',message='This is a publicly accessible API',status=status.HTTP_400_BAD_REQUEST)

class ProtectedAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return renderResponse(data='This is a protected API. You can access this because you are authenticated.',message='This is a protected API. You can access this because you are authenticated.',status=status.HTTP_400_BAD_REQUEST)
