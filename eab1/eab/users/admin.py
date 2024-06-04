from django.contrib import admin
from django import forms
from users.choices.choices import Choices

from .models import (
    User,
    UserType,
    Group,
    Department
)


class DepartmentAdminForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        supervisor = UserType.objects.get(name=Choices.SUPERVISOR).id
        self.fields['supervisor'].queryset = User.objects.filter(user_type_id=supervisor)


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        coordinator = UserType.objects.get(name=Choices.COORDINATOR).id
        self.fields['coordinator'].queryset = User.objects.filter(user_type_id=coordinator)


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        manager = UserType.objects.get(name=Choices.MANAGER).id
        self.fields['manager'].queryset = User.objects.filter(user_type_id=manager)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'user_type_id', 'department')
    form=UserAdminForm


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    list_display = ('name', 'description', 'coordinator')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = ('name', 'description', 'supervisor')