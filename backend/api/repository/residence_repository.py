from django.db.models import Q
from django.db.models.manager import BaseManager
from typing import List, NotRequired, TypedDict, Unpack
from domain.models import RentBilling, Residence
from datetime import datetime as DateTime


class ResidenceQuery(TypedDict):

    isEvicted: NotRequired[bool]
    """
    Only check if current time is between start and end date
    If the residence is evicted, it WILL still be considered active
    """
    isActive: NotRequired[bool]

    startDateFrom: NotRequired[DateTime]
    startDateTo: NotRequired[DateTime]
    endDateFrom: NotRequired[DateTime]
    endDateTo: NotRequired[DateTime]

    studentPk: NotRequired[int]
    roomId: NotRequired[str]

    recruitment_wave_id: NotRequired[str]


def get_list(**filter: Unpack[ResidenceQuery]) -> List[Residence]:
    query = Residence.objects

    if filter.get("student_id"):
        query = query.filter(student_id=filter.get("student_id"))
    if filter.get("roomId"):
        query = query.filter(room_id=filter.get("roomId"))
    if filter.get("recruitment_wave_id"):
        query = query.filter(recruitment_wave_id=filter.get("recruitment_wave_id"))

    if filter.get("startDateFrom"):
        query = query.filter(startDate__gte=filter.get("startDateFrom"))
    if filter.get("startDateTo"):
        query = query.filter(startDate__lte=filter.get("startDateTo"))

    if filter.get("endDateFrom"):
        query = query.filter(endDate__gte=filter.get("endDateFrom"))
    if filter.get("endDateTo"):
        query = query.filter(endDate__lte=filter.get("endDateTo"))

    if filter.get("isEvicted") is not None:
        query = query.filter(isEvicted=filter.get("isEvicted"))

    if filter.get("isActive") is not None:
        query = query.filter(startDate__lte=DateTime.now()).filter(
            endDate__gte=DateTime.now()
        )

    return list(query.all())


class ResidenceRepository:

    @staticmethod
    def get_by_id(
        residence_id: str,
    ) -> Residence:
        return Residence.objects.get(id=residence_id)

    @staticmethod
    def get_by_room_id(
        room_id: str,
    ) -> List[Residence]:
        residences = Residence.objects.filter(room_id=room_id).all()
        return list(residences)

    @staticmethod
    def get_by_student_id(
        student_id: str,
    ) -> List[Residence]:
        residences = Residence.objects.filter(student_id=student_id).all()
        return list(residences)

    @staticmethod
    def get_complete_overlap(
        start_date: DateTime,
        end_date: DateTime,
    ) -> List[Residence]:
        residences = Residence.objects.filter(
            Q(startDate__lte=start_date) & Q(endDate__gte=end_date)
        ).all()
        return list(residences)

    @staticmethod
    def get_partial_overlap(
        start_date: DateTime,
        end_date: DateTime,
    ) -> List[Residence]:
        residences = Residence.objects.filter(
            Q(startDate__lte=start_date) | Q(endDate__gte=end_date)
        ).all()
        return list(residences)
