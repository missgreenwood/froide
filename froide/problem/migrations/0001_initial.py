# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-06 17:08
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("foirequest", "0031_auto_20181106_1510"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProblemReport",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            (
                                "bounce_publicbody",
                                "You received a bounce mail from the public body.",
                            ),
                            (
                                "message_not_delivered",
                                "Your message was not delivered.",
                            ),
                            (
                                "attachment_broken",
                                "The attachments don't seem to work.",
                            ),
                            ("redaction_needed", "Information needs to be redacted."),
                            ("foi_help_needed", "I need assistance to reply."),
                            ("other", "Something else..."),
                        ],
                        max_length=50,
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("auto_submitted", models.BooleanField(default=False)),
                ("resolved", models.BooleanField(default=False)),
                ("description", models.TextField(blank=True)),
                ("resolution", models.TextField(blank=True)),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foirequest.FoiMessage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "problem report",
                "verbose_name_plural": "problem reports",
                "ordering": ("-timestamp",),
            },
        ),
    ]
