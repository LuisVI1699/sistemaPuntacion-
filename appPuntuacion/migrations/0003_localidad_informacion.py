# Generated by Django 3.2.2 on 2021-07-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPuntuacion', '0002_localidad_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='localidad',
            name='informacion',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
    ]