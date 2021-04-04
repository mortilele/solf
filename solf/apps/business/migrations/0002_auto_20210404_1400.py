# Generated by Django 3.1.7 on 2021-04-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitness',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='fitnesses', to='business.Amenity', verbose_name='Fitness Amenities'),
        ),
    ]