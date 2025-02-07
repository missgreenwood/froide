# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 10:45
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foirequest", "0010_foimessage_email_message_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryStatus",
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
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("unknown", "unknown"),
                            ("sent", "sent"),
                            ("received", "received"),
                            ("read", "read"),
                            ("deferred", "deferred"),
                            ("bounced", "bounced"),
                            ("expired", "expired"),
                        ],
                        max_length=32,
                    ),
                ),
                ("log", models.TextField(blank=True)),
                ("last_update", models.DateTimeField()),
                (
                    "message",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foirequest.FoiMessage",
                    ),
                ),
            ],
            options={
                "verbose_name": "delivery status",
                "verbose_name_plural": "delivery statii",
                "ordering": ("last_update",),
                "get_latest_by": "last_update",
            },
        ),
    ]
