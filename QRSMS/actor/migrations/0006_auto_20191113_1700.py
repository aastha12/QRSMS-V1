# Generated by Django 2.2.7 on 2019-11-13 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0005_auto_20191113_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='actor.Employee'),
        ),
    ]