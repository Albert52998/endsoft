# Generated by Django 3.0.8 on 2020-07-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200706_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='soft',
            name='soft_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл софта'),
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Фото категории'),
        ),
    ]
