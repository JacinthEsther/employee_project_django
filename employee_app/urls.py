from . import views
from django.urls import path

urlpatterns = [
    path('department/', views.department_api),
    path('department/<int:id>', views.department_api),

    path('employee/', views.employee_api),
    path('employee/<int:id>', views.employee_api),

]
