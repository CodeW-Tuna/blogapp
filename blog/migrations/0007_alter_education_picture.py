# Generated by Django 4.0.3 on 2023-12-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_description_alter_blog_resim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='picture',
            field=models.ImageField(upload_to='education'),
        ),
    ]
