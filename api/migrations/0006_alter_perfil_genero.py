# Generated by Django 3.2.4 on 2023-11-22 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_perfil_fecha_realizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.TextField(blank=True, null=True),
        ),
    ]
