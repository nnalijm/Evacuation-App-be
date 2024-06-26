# Generated by Django 5.0.4 on 2024-06-04 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='coordinator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coordinated_groups', to='users.user'),
        ),
    ]
