# Generated by Django 2.2.4 on 2019-09-17 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20180111_1347'),
        ('document', '0017_document_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='team.Team'),
        ),
    ]
