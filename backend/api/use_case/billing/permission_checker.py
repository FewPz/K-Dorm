from backend.exception.application_logic.client.not_found import NotFoundException
from backend.exception.permission.unauthorized_action import UnauthorizedAction
from backend.interfaces.context import Context
from backend.interfaces.request_with_context import RequestWithContext
from backend.repositories.staff import StaffRepository
from backend.repositories.student import StudentRepository


def get_billing(ctx: Context, studentId: str) -> bool:
    user = ctx.user
    if user is None:
        raise UnauthorizedAction("Not logged in")

    isStaff = bool(StaffRepository.get_staff_by_account_id(user.uid))
    if isStaff:
        return True

    student = StudentRepository.get_student_by_account_id(user.uid)
    if not student:
        raise NotFoundException("Student is not found")
    return student.studentId == studentId