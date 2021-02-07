# Generated by Django 3.1.4 on 2021-01-10 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210110_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appmodule',
            name='user',
        ),
        migrations.CreateModel(
            name='AppModuleUserMapping',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('apmodule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.appmodule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appmodule',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='app_modules', through='core.AppModuleUserMapping', to=settings.AUTH_USER_MODEL),
        ),
    ]
