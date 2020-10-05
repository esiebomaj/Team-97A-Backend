# Generated by Django 3.1 on 2020-10-05 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200929_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='is confirmed'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='main.wallet'),
        ),
    ]
