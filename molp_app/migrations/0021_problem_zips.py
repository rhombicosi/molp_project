# Generated by Django 3.1.9 on 2021-07-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0020_remove_problem_chebyshev_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='zips',
            field=models.FileField(blank=True, upload_to='problems/zips/', verbose_name='zips'),
        ),
    ]
