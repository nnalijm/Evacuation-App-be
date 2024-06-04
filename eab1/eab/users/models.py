from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    supervisor = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True, related_name='supervised_departments')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    coordinator = models.ForeignKey('User', null=True, blank=True, on_delete=models.CASCADE, related_name='coordinated_groups')

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_present = models.BooleanField(default=False)
    image_path = models.URLField(null=True, blank=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, related_name='managed_users', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"