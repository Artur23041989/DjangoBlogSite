# Generated by Django 5.1.7 on 2025-04-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, null=True, unique=True),
        ),
    ]
