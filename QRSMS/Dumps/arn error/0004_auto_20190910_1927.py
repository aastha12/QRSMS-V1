# Generated by Django 2.2.5 on 2019-09-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0003_auto_20190910_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='nu_email',
            field=models.CharField(max_length=100),
        ),
    ]