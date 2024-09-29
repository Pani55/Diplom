# Generated by Django 4.2.2 on 2024-09-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicine", "0003_alter_doctors_procedures"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicine",
            name="preview",
        ),
        migrations.AddField(
            model_name="doctors",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фотографию доктора",
                null=True,
                upload_to="doctor_photos",
                verbose_name="Фотография",
            ),
        ),
    ]
