# Generated by Django 5.0.6 on 2024-06-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='No description available', max_length=255),
        ),
    ]
