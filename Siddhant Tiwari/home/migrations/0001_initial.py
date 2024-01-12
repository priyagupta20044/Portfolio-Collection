# Generated by Django 5.0 on 2024-01-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=122)),
                ("age", models.CharField(max_length=122)),
                ("place", models.CharField(max_length=122)),
                ("ids", models.TextField()),
                ("date", models.DateTimeField()),
            ],
        ),
    ]
