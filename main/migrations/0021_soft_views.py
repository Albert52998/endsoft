# Generated by Django 3.1 on 2020-08-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200812_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='soft',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Просмотры'),
        ),
    ]
