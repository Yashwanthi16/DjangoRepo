# Generated by Django 5.0.2 on 2024-02-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]