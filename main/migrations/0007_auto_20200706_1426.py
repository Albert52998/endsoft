# Generated by Django 3.0.8 on 2020-07-06 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200706_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sub_category', to='main.Category'),
        ),
    ]
