# Generated by Django 4.2 on 2023-05-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_facility_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/dining_images')),
                ('price_range', models.CharField(max_length=50)),
            ],
        ),
    ]
