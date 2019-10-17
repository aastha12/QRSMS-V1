# Generated by Django 2.2.6 on 2019-10-15 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_auto_20190916_2151'),
        ('initial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='Semester End Date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='Semester Start Date',
            new_name='semester_year',
        ),
        migrations.RenameField(
            model_name='semester',
            old_name='Semester Year',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='student',
            name='attending_semester',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='current_semester',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='warning_count',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='offered_courses',
            field=models.ManyToManyField(related_name='_offered', to='initial.Course'),
        ),
        migrations.CreateModel(
            name='RegularCourseLoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_season', models.SmallIntegerField(choices=[(1, 'FALL'), (2, 'SPRING'), (3, 'SUMMER')])),
                ('courses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='initial.Course')),
                ('degree', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='institution.Degree')),
            ],
        ),
    ]
