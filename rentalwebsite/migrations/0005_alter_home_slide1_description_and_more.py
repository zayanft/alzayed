# Generated by Django 5.0.3 on 2024-03-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalwebsite', '0004_home_slide1_home_slide2_home_slide3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_slide1',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_slide1',
            name='headiline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='home_slide2',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_slide2',
            name='headiline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='home_slide3',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home_slide3',
            name='headiline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]