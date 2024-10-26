from api.repository.staff_repository import StaffRepository
from interfaces.context import Context
from layer.use_case import usecase


@usecase()
def is_security_staff(ctx: Context, accountId: str):
    staff = StaffRepository.get_staff_by_account_id(accountId)
    return bool(staff)
