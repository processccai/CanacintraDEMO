# Generated by Django 3.2.4 on 2023-11-25 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_perfil_validacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('validacion', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
