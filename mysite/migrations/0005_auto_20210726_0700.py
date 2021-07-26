# Generated by Django 3.2.5 on 2021-07-26 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_profile_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.project'),
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
