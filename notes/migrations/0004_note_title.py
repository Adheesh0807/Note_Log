# Generated by Django 5.1.2 on 2024-11-22 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_delete_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
