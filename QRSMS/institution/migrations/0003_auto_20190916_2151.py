# Generated by Django 2.2.5 on 2019-09-16 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0002_auto_20190916_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='departemnt_name',
            new_name='department_name',
        ),
    ]