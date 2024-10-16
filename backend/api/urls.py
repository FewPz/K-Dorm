import api.views.auth as auth_views
import api.views.maintenance as maintenance
import api.views.account as account
from django.urls import path

from api.views.building import building_detail_view, building_list_view
from api.views.room import room_detail_view, room_list_view

urlpatterns = [
    # Tasks API Route
    # path("/tasks", task_views.get_tasks, name="task"),
    # # Task Detail API
    # path("/tasks/<int:pk>", task_views.TaskDetail.as_view(), name="task_detail"),
]

# AUTHENTICATION URLS
urlpatterns += [
    path("auth/me", auth_views.get_current_user, name="getme"),
    # DEPRECATED
    path("auth/signin", auth_views.signin, name="signin"),
]

# MAINTENANCE URLS
urlpatterns += [
    path("student/maintenance", maintenance.student_maintenance_ticket),
    path("student/maintenance/<str:pk>",
         maintenance.student_maintenance_ticket_detail),
    path("staff/maintenance", maintenance.staff_maintenance_tickets),
]

# BUILDING URLS
urlpatterns += [
    path("staff/building", building_list_view.view),
    path("staff/building/<str:building_id>", building_detail_view.view),
]

urlpatterns += [
    path("staff/room", room_list_view.view),
    path("staff/room/<str:room_id>", room_detail_view.view),
]

# ACCOUNT URLS
urlpatterns += [
    path("staff/account", account.staff_account),
    path("staff/account/<int:id>", account.edit_staff_account),
]
