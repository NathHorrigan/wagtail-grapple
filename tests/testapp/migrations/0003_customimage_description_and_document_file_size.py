# Generated by Django 5.0.11 on 2025-02-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="customimage",
            name="description",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="description"
            ),
        ),
        migrations.AlterField(
            model_name="customdocument",
            name="file_size",
            field=models.PositiveBigIntegerField(editable=False, null=True),
        ),
    ]
