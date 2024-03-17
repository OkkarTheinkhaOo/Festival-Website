# Generated by Django 5.0.2 on 2024-03-01 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_artist_artistbday'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='festivalDate',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=255)),
                ('eventDate', models.DateTimeField()),
                ('artistName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.artist')),
                ('festivalName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.festival')),
            ],
        ),
    ]