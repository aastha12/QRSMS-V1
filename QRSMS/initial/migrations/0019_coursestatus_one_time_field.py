# Generated by Django 2.2.7 on 2019-11-23 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0018_coursesection_section_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestatus',
            name='one_time_field',
            field=models.BinaryField(blank=True, default=False, null=True),
        ),
    ]