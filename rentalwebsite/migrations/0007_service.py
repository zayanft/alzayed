# Generated by Django 5.0.3 on 2024-03-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalwebsite', '0006_category_equipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='services')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
