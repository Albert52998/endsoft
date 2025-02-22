# Generated by Django 3.1 on 2020-08-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_soft_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soft',
            name='downloads',
        ),
        migrations.RemoveField(
            model_name='soft',
            name='views',
        ),
        migrations.AddField(
            model_name='soft',
            name='counter',
            field=models.PositiveIntegerField(default=0, verbose_name='Кол-во загрузок'),
        ),
        migrations.AlterField(
            model_name='soft',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Файл'),
        ),
    ]
