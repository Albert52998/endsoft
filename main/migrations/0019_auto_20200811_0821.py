# Generated by Django 3.0.9 on 2020-08-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200811_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soft',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
