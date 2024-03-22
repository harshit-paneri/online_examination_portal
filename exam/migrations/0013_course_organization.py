# Generated by Django 3.0.5 on 2024-03-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_fees'),
        ('exam', '0012_auto_20240319_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
