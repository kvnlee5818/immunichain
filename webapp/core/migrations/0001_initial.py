# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Required. 150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.', max_length=150, unique=True)),
                ('full_name', models.CharField(help_text="Please enter your child's full name.", max_length=60)),
                ('address', models.CharField(help_text="Please enter your child's address", max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('role', models.CharField(choices=[('', '-----------'), ('GRDN', 'Guardian'), ('MEMB', 'Member Organization'), ('HEAL', 'Healthcare Provider')], max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
