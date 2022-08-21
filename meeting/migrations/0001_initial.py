# Generated by Django 4.1 on 2022-08-21 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Meeting",
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
                ("title", models.CharField(blank=True, max_length=120, null=True)),
                ("subject", models.TextField(blank=True, null=True)),
                ("meeting_date", models.DateField(blank=True, null=True)),
                ("meeting_start_time", models.TimeField(blank=True, null=True)),
                ("meeting_end_time", models.TimeField(blank=True, null=True)),
                ("meeting_created_date", models.DateTimeField(editable=False)),
                ("meeting_modified_date", models.DateTimeField()),
                ("draft", models.BooleanField()),
                (
                    "slug",
                    models.SlugField(
                        default=uuid.uuid1, editable=False, max_length=150, unique=True
                    ),
                ),
                (
                    "meeting_image",
                    models.ImageField(blank=True, upload_to="media/meetings"),
                ),
                (
                    "meeting_members",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="members",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="whoCreate",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]