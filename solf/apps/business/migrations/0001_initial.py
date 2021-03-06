# Generated by Django 3.1.7 on 2021-04-01 19:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=20, verbose_name='Amenity name')),
            ],
            options={
                'verbose_name': 'Fitness amenity',
                'verbose_name_plural': 'Fitness amenities',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Business',
                'verbose_name_plural': 'Business',
            },
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('latitude', models.FloatField(null=True, verbose_name='Latitude')),
                ('longitude', models.FloatField(null=True, verbose_name='Longitude')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('website', models.URLField(blank=True, max_length=30, verbose_name='Website')),
                ('email', models.EmailField(blank=True, max_length=30, verbose_name='E-mail')),
                ('name', models.CharField(max_length=100, verbose_name='Fitness name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('amenities', models.ManyToManyField(related_name='fitnesses', to='business.Amenity', verbose_name='Fitness Amenities')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fitnesses', to='business.business', verbose_name='Business')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.city')),
            ],
            options={
                'verbose_name': 'Fitness',
                'verbose_name_plural': 'Fitnesses',
            },
        ),
    ]
