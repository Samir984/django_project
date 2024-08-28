# Generated by Django 5.1 on 2024-08-28 03:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
