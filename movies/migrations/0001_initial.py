# Generated by Django 5.0.2 on 2024-02-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=255)),
                ("release_year", models.IntegerField()),
                ("director", models.CharField(max_length=100)),
                ("runtime", models.CharField(max_length=100)),
                ("plot", models.TextField()),
                ("poster", models.CharField(max_length=255)),
                ("actors", models.ManyToManyField(to="movies.actor")),
            ],
        ),
    ]
