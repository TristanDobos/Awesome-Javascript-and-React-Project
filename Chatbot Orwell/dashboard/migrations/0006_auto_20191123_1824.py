# Generated by Django 2.2 on 2019-11-24 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_reporte_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
