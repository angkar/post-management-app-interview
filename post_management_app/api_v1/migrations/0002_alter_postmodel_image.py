# Generated by Django 5.1.3 on 2024-12-24 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name=''),
        ),
    ]
