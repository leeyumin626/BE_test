# Generated by Django 5.2.3 on 2025-06-26 04:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_remove_book_plot"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="plot",
            field=models.TextField(default="줄거리 없음"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="content",
            field=models.TextField(default="줄거리 없음"),
            preserve_default=False,
        ),
    ]
