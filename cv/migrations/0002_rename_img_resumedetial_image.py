# Generated by Django 4.0.2 on 2022-02-17 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumedetial',
            old_name='img',
            new_name='image',
        ),
    ]
