# Generated by Django 3.1.9 on 2021-07-06 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0019_auto_20210707_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='chebyshev_zip',
        ),
    ]