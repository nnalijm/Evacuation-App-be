from django.db.models import TextChoices


class Choices(TextChoices):
    SUPERVISOR = 'supervisor', 'Supervisor'
    MANAGER = 'manager', 'Manager'
    COORDINATOR = 'coordinator', 'Coordinator'
    EMPLOYEE = 'employee', 'Employee'