# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework import status, serializers

# Exceptions
from rest_framework.exceptions import AuthenticationFailed

# Use-Cases
from use_cases.account.handle_create_account import handle_create_account
from use_cases.account.handle_get_account import handle_get_all_staff_accounts
from use_cases.account.handle_edit_staff_account import handle_edit_staff_account

# Interfaces
from interfaces.api_response import APIResponse
from interfaces.error_response import ErrorResponse

# Serializer
from serializers.account_serializer import get_serializer_class, serialize
from serializers.user_serializer import AuthUserSerializer

# Decorators
from core.middleware.decorators.authenticated_user_only import authenticated_user_only
from layer.handle import handle

from django.core.exceptions import ObjectDoesNotExist
from interfaces.request_with_context import RequestWithContext


@api_view(['GET', 'POST'])
@handle(only_authenticated=True, only_role=["STAFF"])
def staff_account(request: RequestWithContext) -> APIResponse | ErrorResponse:
    try:
        if request.method == 'GET':
            result = handle_get_all_staff_accounts(request)
            staff_accounts = serialize(data=result, many=True)
            return APIResponse(status=status.HTTP_200_OK, data=staff_accounts)
        elif request.method == 'POST':
            serializer_class = get_serializer_class(request)
            serializer = serializer_class(data=request.data)

            if serializer.is_valid():
                result = handle_create_account(request, serializer)
                account_data = serialize(data=result)
                return APIResponse(status=status.HTTP_201_CREATED, data=account_data)
            else:
                return ErrorResponse(status=status.HTTP_400_BAD_REQUEST, error="BAD_REQUEST", message=str(serializer.errors))
    except serializers.ValidationError as e:
        return ErrorResponse(status=status.HTTP_404_NOT_FOUND, error="CONFLICT", message=str(e))
    except AuthenticationFailed as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))
    except Exception as e:
        return ErrorResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error="INTERNAL_SERVER_ERROR", message=str(e))

    return ErrorResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, error="METHOD_NOT_ALLOWED", message="Method not allowed")


@api_view(['PUT'])
@handle(only_authenticated=True, only_role=["STAFF"])
def edit_staff_account(request: RequestWithContext, id: int):
    try:
        serializer_class = get_serializer_class(request)
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            result = handle_edit_staff_account(request, serializer, id)
            account_data = serialize(data=result)
            return APIResponse(status=status.HTTP_201_CREATED, data=account_data)
        else:
            return ErrorResponse(status=status.HTTP_400_BAD_REQUEST, error="BAD_REQUEST", message=str(serializer.errors))
    except ObjectDoesNotExist as e:
        return ErrorResponse(status=status.HTTP_404_NOT_FOUND, error="NOT_FOUND", message=str(e))
    except serializers.ValidationError as e:
        return ErrorResponse(status=status.HTTP_400_BAD_REQUEST, error="CONFLICT", message=str(e))
    except AuthenticationFailed as e:
        return ErrorResponse(status=status.HTTP_401_UNAUTHORIZED, error="UNAUTHORIZED", message=str(e))
    except Exception as e:
        return ErrorResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error="UNAUTHORIZED", message=str(e))
