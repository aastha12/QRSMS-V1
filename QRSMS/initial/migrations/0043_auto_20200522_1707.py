# Generated by Django 2.2 on 2020-05-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0042_auto_20200519_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmarks',
            old_name='mark_type',
            new_name='marks_type',
        ),
        migrations.AddField(
            model_name='studentmarks',
            name='section',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
