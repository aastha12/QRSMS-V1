# Generated by Django 2.2 on 2020-05-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0041_merge_20200516_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'get_latest_by': 'start_date', 'ordering': ['-semester_code']},
        ),
        migrations.AddField(
            model_name='semester',
            name='co_circular_fee',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='coursestatus',
            name='section',
            field=models.CharField(blank=True, default='Z', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='offeredcourses',
            name='courses_offered',
            field=models.ManyToManyField(related_name='offeredcourses', to='initial.CourseStatus'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='current_semester',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='semester',
            name='fee_per_CR',
            field=models.FloatField(blank=True, default=7400, max_length=10, null=True),
        ),
    ]
