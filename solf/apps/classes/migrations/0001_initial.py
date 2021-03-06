# Generated by Django 3.1.7 on 2021-04-01 19:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20210401_1930'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='Class name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='About class')),
                ('max_spots', models.PositiveSmallIntegerField(verbose_name='Maximum available spots')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='classes', to='core.category', verbose_name='Class Category')),
                ('fitness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='business.fitness', verbose_name='Fitness')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('weekday', models.PositiveSmallIntegerField(choices=[(1, '??????????????????????'), (2, '??????????????'), (3, '??????????'), (4, '??????????????'), (5, '??????????????'), (6, '??????????????'), (7, '??????????????????????')], verbose_name='Weekday')),
                ('start_time', models.TimeField(default=datetime.time(9, 0), verbose_name='Start time')),
                ('end_time', models.TimeField(default=datetime.time(18, 0), verbose_name='End time')),
                ('max_spots', models.PositiveSmallIntegerField(verbose_name='Maximum available spots')),
                ('class_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='classes.class', verbose_name='Class')),
            ],
            options={
                'verbose_name': 'Class Schedule',
                'verbose_name_plural': 'Classes Schedule',
            },
        ),
        migrations.CreateModel(
            name='ClassScheduleLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='logs', to='classes.classschedule', verbose_name='Schedule')),
            ],
            options={
                'verbose_name': 'Class Schedule Logs',
                'verbose_name_plural': 'Classes Schedule Logs',
            },
        ),
    ]
