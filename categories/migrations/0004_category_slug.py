# Generated by Django 5.0 on 2024-01-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]