from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserType, User, Department, Group
from .serializers import (
    UserTypeSerializer,
    UserSerializer,
    DepartmentSerializer,
    GroupSerializer,
    UserEmployeeSerializer
)


class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=['get'])
    def managers(self, request, pk=None):
        department = self.get_object()
        managers = User.objects.filter(department=department, user_type__name='manager')
        serializer = UserSerializer(managers, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        group = self.get_object()
        employee = User.objects.filter(group=group, user_type__name='employee')
        serializer = UserEmployeeSerializer(employee, many=True)
        return Response(serializer.data)


class SupervisorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.filter(user_type__name='supervisor')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def departments(self, request, pk=None):
        supervisor = self.get_object()
        departments = Department.objects.filter(supervisor=supervisor)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


class ManagerViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.filter(user_type__name='manager')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def coordinators(self, request, pk=None):
        manager = self.get_object()
        coordinators = User.objects.filter(manager=manager)
        serializer = UserSerializer(coordinators, many=True)
        return Response(serializer.data)


class CoordinatorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.filter(user_type__name='coordinator')
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def groups(self, request, pk=None):
        coordinator = self.get_object()
        groups = Group.objects.filter(coordinator=coordinator)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
