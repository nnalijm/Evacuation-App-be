from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    UserViewSet,
    UserTypeViewSet,
    DepartmentViewSet,
    SupervisorViewSet,
    GroupViewSet,
    ManagerViewSet,
    CoordinatorViewSet
)


router = DefaultRouter()
router.register(r'user_types', UserTypeViewSet)
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'supervisors', SupervisorViewSet, basename='supervisor')
router.register(r'managers', ManagerViewSet, basename='manager')
router.register(r'coordinators', CoordinatorViewSet, basename='coordinator')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
