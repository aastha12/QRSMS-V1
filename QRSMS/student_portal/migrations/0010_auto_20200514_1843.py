# Generated by Django 2.2 on 2020-05-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0009_feechallan_challan_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feechallan',
            name='discount',
            field=models.FloatField(default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='feechallan',
            name='financial_aid',
            field=models.FloatField(default=0, max_length=15),
        ),
    ]
