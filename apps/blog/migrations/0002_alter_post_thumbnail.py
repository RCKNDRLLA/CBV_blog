# Generated by Django 5.1.5 on 2025-01-25 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images/thumbnails/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Изображение записи'),
        ),
    ]
