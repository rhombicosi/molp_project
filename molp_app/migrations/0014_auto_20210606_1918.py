# Generated by Django 3.1 on 2021-06-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('molp_app', '0013_auto_20210522_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproblem',
            name='solver',
            field=models.CharField(choices=[('NEOS', 'NEOS'), ('CBC', 'CBC')], default='CBC', max_length=10),
        ),
    ]
