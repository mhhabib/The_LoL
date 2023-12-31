# Generated by Django 4.2.4 on 2023-08-13 16:50

from django.db import migrations, models
import lensapi.models


class Migration(migrations.Migration):
    dependencies = [
        ("lensapi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="thumbnail_image",
            field=models.ImageField(
                blank=True, upload_to=lensapi.models.Post.thumbnail_image_upload_to
            ),
        ),
    ]
