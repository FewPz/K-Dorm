from .get_usage_billings_student_id import (
    get_usage_billings_by_student_id as _get_usage_billings_by_student_id,
)
from .get_stats_by_student_id import get_stats_by_student_id as _get_stats_by_student_id
from .get_rent_billings import get_rent_billings as _get_rent_billings

get_rent_billings = _get_rent_billings
get_stats_by_student_id = _get_stats_by_student_id
get_usage_billings_by_student_id = _get_usage_billings_by_student_id
