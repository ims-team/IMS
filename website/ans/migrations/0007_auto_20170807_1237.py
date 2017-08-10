# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-07 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0006_auto_20170807_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ansbe',
            old_name='Inst',
            new_name='Instance',
        ),
        migrations.AlterField(
            model_name='ansbe',
            name='Roles',
            field=models.CharField(choices=[('Apache', 'Apache'), ('Ngimix', 'Ngimx'), ('Java', 'Java'), ('Tomcat', 'Tomcat'), ('Comman', 'Comman')], default='Java', max_length=7),
        ),
    ]