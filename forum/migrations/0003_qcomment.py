# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_answer_answer_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qcomment_text', models.CharField(max_length=255)),
                ('qcomment_time', models.TimeField(verbose_name='qcomment_time')),
                ('cquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Question')),
            ],
        ),
    ]