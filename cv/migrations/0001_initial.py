# Generated by Django 4.0.2 on 2022-02-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeDetial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=250)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]