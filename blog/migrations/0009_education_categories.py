# Generated by Django 4.0.3 on 2023-12-21 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_education_category_blog_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]