# Generated by Django 3.2.5 on 2021-07-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20210722_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
