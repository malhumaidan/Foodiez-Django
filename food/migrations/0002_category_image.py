# Generated by Django 4.1.3 on 2022-12-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]