# Generated by Django 3.1 on 2020-08-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200828_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='soft',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Модерация'),
        ),
    ]
