# Generated by Django 4.0.3 on 2023-12-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]