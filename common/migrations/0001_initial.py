# Generated by Django 3.2.10 on 2022-04-24 16:30

import TM470_backend.storage_backends
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beats', '0001_initial'),
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('beat', models.ForeignKey(blank=True, help_text='Kudos given to Beat', null=True, on_delete=django.db.models.deletion.CASCADE, to='beats.beat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(max_length=500, storage=TM470_backend.storage_backends.PrivateMediaStorage, upload_to='images/routes/')),
                ('description', models.TextField(blank=True, null=True)),
                ('beat', models.ForeignKey(blank=True, help_text='Kudos given to Beat', null=True, on_delete=django.db.models.deletion.CASCADE, to='beats.beat')),
                ('problem', models.ForeignKey(blank=True, help_text='Kudos given to Beat', null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('post', models.TextField()),
                ('beat', models.ForeignKey(help_text='Comment on Beat', on_delete=django.db.models.deletion.CASCADE, to='beats.beat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
