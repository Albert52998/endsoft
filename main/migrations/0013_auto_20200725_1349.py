# Generated by Django 3.0.8 on 2020-07-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200725_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soft',
            name='soft_file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл софта'),
        ),
    ]
