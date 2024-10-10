# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework import status

# Exceptions
from rest_framework.exceptions import AuthenticationFailed

# Use-Cases
from use_cases.auth.handle_get_current_user import handle_get_current_user
from use_cases.auth.handle_signin import handle_signin

# Interfaces
from interfaces.api_response import APIResponse
from interfaces.error_response import ErrorResponse

# Serializer
from serializers.user_serializer import AuthUserSerializer

# Utils
from utils import account_utils


@api_view(['POST'])
def signin(request):
    try:
        account = handle_signin(request)
        serializer = AuthUserSerializer(account)
        user_data = serializer.data
        role = account_utils.get_user_role(user_data)
        return APIResponse(status=status.HTTP_200_OK, data={"user": user_data, "role": role})
    except AuthenticationFailed as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))
    except Exception as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))


@api_view(['GET'])
def get_current_user(request):
    try:
        account = handle_get_current_user(request)
        serializer = AuthUserSerializer(account)
        user_data = serializer.data
        role = account_utils.get_user_role(user_data)
        return APIResponse(status=status.HTTP_200_OK, data={"user": user_data, "role": role})
    except AuthenticationFailed as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))
    except Exception as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))
