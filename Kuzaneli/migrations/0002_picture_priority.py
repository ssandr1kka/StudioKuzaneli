# Generated by Django 3.1.2 on 2020-11-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kuzaneli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='priority',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
