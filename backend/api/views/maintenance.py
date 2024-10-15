# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework import status

# Use-Cases
from interfaces.request_with_context import RequestWithContext
from use_cases.maintenance.handle_create_maintenance_ticket import handle_create_maintenance_ticket
from use_cases.maintenance.maintenance_use_cases import MaintenanceTicketUserCase
# Interfaces
from interfaces.api_response import APIResponse
from interfaces.error_response import ErrorResponse

# Serializer
from serializers.maintenance_serializer import get_serializer_class, serialize

# Decorators
from layer.handle import handle


@api_view(['POST', 'GET'])
@handle(only_authenticated=True)
def student_maintenance_ticket(request: RequestWithContext) -> APIResponse | ErrorResponse:
    try:
        if request.method == 'POST':
            serializer_class = get_serializer_class(request=request)
            serializer = serializer_class(data=request.data)

            if serializer.is_valid():
                result = handle_create_maintenance_ticket(
                    request, serializer)
                serialized_data = serialize(data=result)
                return APIResponse(status=status.HTTP_200_OK, data=serialized_data)
            else:
                return ErrorResponse(status=status.HTTP_400_BAD_REQUEST, error="BAD_REQUEST", message=str(serializer.errors))

        if request.method == 'GET':
            result = MaintenanceTicketUserCase.get_student_maintenance_tickets(
                request)
            serialized_data = serialize(data=result, many=True)
            return APIResponse(status=status.HTTP_200_OK, data=serialized_data)
    except Exception as e:
        return ErrorResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error="INTERNAL_SERVER_ERROR", message=str(e))

    return ErrorResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, error="METHOD_NOT_ALLOWED", message="Method not allowed")


@api_view(['GET', "POST"])
@handle(only_authenticated=True)
def student_maintenance_ticket_detail(request, pk) -> APIResponse | ErrorResponse:
    if request.method == 'GET':
        result = MaintenanceTicketUserCase.get_maintenance_ticket_by_id(
            request, pk)
        if result is not None:
            serialized_data = serialize(data=result)
            return APIResponse(status=status.HTTP_200_OK, data=serialized_data)
        else:
            return ErrorResponse(status=status.HTTP_404_NOT_FOUND, error="NOT_FOUND", message="Maintenance ticket not found")
    elif request.method == 'PUT':
        serializer_class = get_serializer_class(request=request)
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            result = MaintenanceTicketUserCase.update_maintenance_ticket(
                request, pk, serializer)
            serialized_data = serialize(data=result)
            return APIResponse(status=status.HTTP_200_OK, data=serialized_data)
        else:
            return ErrorResponse(status=status.HTTP_400_BAD_REQUEST, error="BAD_REQUEST", message=str(serializer.errors))

    return ErrorResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, error="METHOD_NOT_ALLOWED", message="Method not allowed")


@api_view(['POST', 'GET'])
@handle(only_authenticated=True)
def staff_maintenance_tickets(request) -> APIResponse | ErrorResponse:
    try:
        if request.method == 'GET':
            result = MaintenanceTicketUserCase.get_all_maintenance_tickets(
                request)
            serialized_data = serialize(data=result, many=True)
            return APIResponse(status=status.HTTP_200_OK, data=serialized_data)
    except Exception as e:
        return ErrorResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error="INTERNAL_SERVER_ERROR", message=str(e))

    return ErrorResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED, error="METHOD_NOT_ALLOWED", message="Method not allowed")
