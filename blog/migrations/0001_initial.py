# Generated by Django 5.1.2 on 2024-11-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('create_at', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
    ]