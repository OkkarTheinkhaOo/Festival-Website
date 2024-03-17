# Generated by Django 5.0.2 on 2024-03-01 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_festival_festivaldate_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festival',
            old_name='festivalDate',
            new_name='festivalEndDate',
        ),
        migrations.AddField(
            model_name='festival',
            name='festivalStartDate',
            field=models.DateField(null=True),
        ),
    ]