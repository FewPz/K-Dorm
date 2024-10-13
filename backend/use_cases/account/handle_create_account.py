# Django
from django.db import transaction

# Repositories
from repositories.account_repository import create_new_account, create_new_maintenance_staff_account, create_new_security_staff_account, create_new_staff_account

# Utils
from utils.firebase_storage import get_bucket_location

import uuid


@transaction.atomic
def handle_create_account(request, serializer):
    uid = str(uuid.uuid4()).split("-")[0]
    validated_data = serializer.validated_data

    account = create_new_account(
        uid=uid,
        email=validated_data['email'],
        first_name=validated_data['firstName'],
        last_name=validated_data['lastName'],
    )

    if validated_data['type'] == "STAFF":
        create_new_staff_account(account=account)
    elif validated_data['type'] == "MAINTENANCE_STAFF":
        create_new_maintenance_staff_account(account=account)
    elif validated_data['type'] == "SECURITY_STAFF":
        create_new_security_staff_account(account=account)

    account.refresh_from_db()

    return account
