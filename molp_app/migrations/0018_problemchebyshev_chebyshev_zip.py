# Generated by Django 3.1.9 on 2021-07-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0017_auto_20210624_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemchebyshev',
            name='chebyshev_zip',
            field=models.FileField(blank=True, upload_to='problems/zips/'),
        ),
    ]
