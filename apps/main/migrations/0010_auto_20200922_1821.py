# Generated by Django 3.1 on 2020-09-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200922_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_image',
            field=models.ImageField(default='package_images/default.png', upload_to='package_images/', verbose_name='Package image'),
        ),
        migrations.AlterField(
            model_name='package',
            name='dest_address',
            field=models.CharField(max_length=50, verbose_name='delivery address'),
        ),
        migrations.AlterField(
            model_name='package',
            name='pick_address',
            field=models.CharField(max_length=50, verbose_name='pick up address'),
        ),
    ]
