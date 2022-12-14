# Generated by Django 4.1.3 on 2022-11-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='profile_pics')),
                ('twitter', models.URLField()),
            ],
        ),
    ]
