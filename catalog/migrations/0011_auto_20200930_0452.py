# Generated by Django 3.0.7 on 2020-09-30 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200930_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addition_info',
            old_name='image',
            new_name='images',
        ),
    ]
