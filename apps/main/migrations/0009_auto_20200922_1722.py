# Generated by Django 3.1 on 2020-09-22 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200922_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='dest_location',
            new_name='dest_address',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='pick_location',
            new_name='pick_address',
        ),
    ]
